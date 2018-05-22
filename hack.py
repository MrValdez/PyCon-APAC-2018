'''
This file contains hacks to fix some issues with Arcade. Hopefully, I can make a cleaner version of these,
but for now, let's just copypasta the affected code
'''

######
'''
Hack fix for blurry texture images in a 2D world.

arcade.draw_commands.load_texture() uses GL_LINEAR_MIPMAP_LINEAR
>    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER,
                       gl.GL_LINEAR_MIPMAP_LINEAR)
>    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAX_FILTER,
                       gl.GL_LINEAR_MIPMAP_LINEAR)

This causes the texture to be blurry. Instead, let's try GL_NEAREST/GL_LINEAR.

references:
    https://gamedev.stackexchange.com/questions/19075/how-can-i-make-opengl-textures-scale-without-becoming-blurry
'''
import helper
import arcade
from arcade.draw_commands import Texture
import ctypes
import PIL
import pyglet
import pyglet.gl as gl
from pyglet.gl import glu as glu

def load_texture(file_name: str, x: float=0, y: float=0,
                 width: float=0, height: float=0,
                 mirrored: bool = False,
                 flipped: bool = False,
                 scale: float=1) -> arcade.Texture:
    """
    Load image from disk and create a texture.

    Args:
        :filename (str): Name of the file to that holds the texture.
        :x (float): X position of the crop area of the texture.
        :y (float): Y position of the crop area of the texture.
        :width (float): Width of the crop area of the texture.
        :height (float): Height of the crop area of the texture.
        :scale (float): Scale factor to apply on the new texture.
    Returns:
        The new texture.
    Raises:
        None

    >>> import arcade
    >>> arcade.open_window(800,600,"Drawing Example")
    >>> name = "arcade/examples/images/meteorGrey_big1.png"
    >>> texture1 = load_texture(name, 1, 1, 50, 50)
    >>> texture2 = load_texture(name, 1, 1, 50, 50)

    >>> texture = load_texture(name, 200, 1, 50, 50)
    Traceback (most recent call last):
    ...
    ValueError: Can't load texture starting at an x of 200 when the image is only 101 across.

    >>> texture = load_texture(name, 1, 50, 50, 50)
    Traceback (most recent call last):
    ...
    ValueError: Can't load texture ending at an y of 100 when the image is only 84 high.

    >>> texture = load_texture(name, 1, 150, 50, 50)
    Traceback (most recent call last):
    ...
    ValueError: Can't load texture starting at an y of 150 when the image is only 84 high.

    >>> texture = load_texture(name, 0, 0, 400, 50)
    Traceback (most recent call last):
    ...
    ValueError: Can't load texture ending at an x of 400 when the image is only 101 wide.

    >>> arcade.close_window()
    """

    # See if we already loaded this file, and we can just use a cached version.
    cache_name = "{}{}{}{}{}{}{}{}".format(file_name, x, y, width, height, scale, flipped, mirrored)
    if cache_name in load_texture.texture_cache:
        return load_texture.texture_cache[cache_name]

    source_image = PIL.Image.open(file_name)

    source_image_width, source_image_height = source_image.size

    if x != 0 or y != 0 or width != 0 or height != 0:
        if x > source_image_width:
            raise ValueError("Can't load texture starting at an x of {} "
                             "when the image is only {} across."
                             .format(x, source_image_width))
        if y > source_image_height:
            raise ValueError("Can't load texture starting at an y of {} "
                             "when the image is only {} high."
                             .format(y, source_image_height))
        if x + width > source_image_width:
            raise ValueError("Can't load texture ending at an x of {} "
                             "when the image is only {} wide."
                             .format(x + width, source_image_width))
        if y + height > source_image_height:
            raise ValueError("Can't load texture ending at an y of {} "
                             "when the image is only {} high."
                             .format(y + height, source_image_height))

        image = source_image.crop((x, y, x + width, y + height))
    else:
        image = source_image

    # image = _trim_image(image)
    if mirrored:
        image = PIL.ImageOps.mirror(image)

    if flipped:
        image = PIL.ImageOps.flip(image)

    image_width, image_height = image.size
    image_bytes = image.convert("RGBA").tobytes("raw", "RGBA", 0, -1)

    texture = gl.GLuint(0)
    gl.glGenTextures(1, ctypes.byref(texture))

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)

    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S,
                       gl.GL_REPEAT)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T,
                       gl.GL_REPEAT)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER,
                       gl.GL_NEAREST)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER,
                       gl.GL_NEAREST)
    glu.gluBuild2DMipmaps(gl.GL_TEXTURE_2D, gl.GL_RGBA,
                          image_width, image_height,
                          gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, image_bytes)

    image_width *= scale
    image_height *= scale

    result = Texture(texture, image_width, image_height)
    load_texture.texture_cache[cache_name] = result
    return result

load_texture.texture_cache = dict()

class Image(helper.Image):
    def __init__(self, left, top, filename, transition=None, scale=1):
        super().__init__(left, top, filename, transition)

        #copypasted from arcade.sprite.Sprite.__init__
        self.texture = load_texture(filename, scale=scale)

        self.textures = [self.texture]
        self.width = self.texture.width * self.scale
        self.height = self.texture.height * self.scale