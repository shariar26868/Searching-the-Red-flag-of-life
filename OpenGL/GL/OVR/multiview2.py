'''OpenGL extension OVR.multiview2

This module customises the behaviour of the 
OpenGL.raw.GL.OVR.multiview2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	
	This extension relaxes the restriction in OVR_multiview that only gl_Position
	can depend on ViewID in the vertex shader.  With this change, view-dependent
	outputs like reflection vectors and similar are allowed.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OVR/multiview2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.OVR.multiview2 import *
from OpenGL.raw.GL.OVR.multiview2 import _EXTENSION_NAME

def glInitMultiview2OVR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION