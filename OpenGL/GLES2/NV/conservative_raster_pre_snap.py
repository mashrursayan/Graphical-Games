'''OpenGL extension NV.conservative_raster_pre_snap

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.conservative_raster_pre_snap to provide a more 
Python-friendly API

Overview (from the spec)
	
	NV_conservative_raster_pre_snap_triangles provides a new mode to achieve
	rasterization of triangles that is conservative w.r.t the triangle at 
	infinite precision i.e. before it is snapped to the sub-pixel grid.  This
	extension provides a new mode that expands this functionality to lines and 
	points.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/conservative_raster_pre_snap.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.conservative_raster_pre_snap import *
from OpenGL.raw.GLES2.NV.conservative_raster_pre_snap import _EXTENSION_NAME

def glInitConservativeRasterPreSnapNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION