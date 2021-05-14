#!/usr/bin/env python3
#
# pixbuf_formats.py
#
# Refer to:
# https://lazka.github.io/pgi-docs/GdkPixbuf-2.0/classes/PixbufLoader.html#GdkPixbuf.PixbufLoader.new_with_mime_type
#
# The list of supported mime types depends on what image loaders are installed, 
# but typically “image/png”, “image/jpeg”, “image/gif”, “image/tiff” and 
# “image/x-xpixmap” are among the supported mime types. 
#
# To obtain the full list of supported mime types, call 
# GdkPixbuf.PixbufFormat.get_mime_types() on each of the GdkPixbuf.PixbufFormat 
# structs returned by GdkPixbuf.Pixbuf.get_formats().

import gi
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf
s = ""
pixbuf_format = GdkPixbuf.Pixbuf.get_formats()
for item in pixbuf_format:
    mime_list = GdkPixbuf.PixbufFormat.get_mime_types(item)
    for mime in mime_list:
        print(mime)
        s += mime + ", "
s = s[:-2] + "."
print(s)

"""
image/x-wmf, application/x-navi-animation, image/bmp, image/x-bmp, 
image/x-MS-bmp, image/gif, image/x-icns, image/x-icon, image/x-ico, 
image/x-win-bitmap, image/vnd.microsoft.icon, application/ico, image/ico, 
image/icon, text/ico, image/jpeg, image/png, image/x-portable-anymap, 
image/x-portable-bitmap, image/x-portable-graymap, image/x-portable-pixmap, 
image/x-quicktime, image/qtif, image/svg+xml, image/svg, image/svg-xml, 
image/vnd.adobe.svg+xml, text/xml-svg, image/svg+xml-compressed, image/x-tga, 
image/tiff, image/x-xbitmap, image/x-xpixmap.

image/x-wmf
application/x-navi-animation
image/bmp
image/x-bmp
image/x-MS-bmp
image/gif
image/x-icns
image/x-icon
image/x-ico
image/x-win-bitmap
image/vnd.microsoft.icon
application/ico
image/ico
image/icon
text/ico
image/jpeg
image/png
image/x-portable-anymap
image/x-portable-bitmap
image/x-portable-graymap
image/x-portable-pixmap
image/x-quicktime
image/qtif
image/svg+xml
image/svg
image/svg-xml
image/vnd.adobe.svg+xml
text/xml-svg
image/svg+xml-compressed
image/x-tga
image/tiff
image/x-xbitmap
image/x-xpixmap
"""
