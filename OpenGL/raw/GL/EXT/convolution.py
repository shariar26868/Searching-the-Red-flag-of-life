'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_convolution'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_convolution',error_checker=_errors._error_checker)
GL_CONVOLUTION_1D_EXT=_C('GL_CONVOLUTION_1D_EXT',0x8010)
GL_CONVOLUTION_2D_EXT=_C('GL_CONVOLUTION_2D_EXT',0x8011)
GL_CONVOLUTION_BORDER_MODE_EXT=_C('GL_CONVOLUTION_BORDER_MODE_EXT',0x8013)
GL_CONVOLUTION_FILTER_BIAS_EXT=_C('GL_CONVOLUTION_FILTER_BIAS_EXT',0x8015)
GL_CONVOLUTION_FILTER_SCALE_EXT=_C('GL_CONVOLUTION_FILTER_SCALE_EXT',0x8014)
GL_CONVOLUTION_FORMAT_EXT=_C('GL_CONVOLUTION_FORMAT_EXT',0x8017)
GL_CONVOLUTION_HEIGHT_EXT=_C('GL_CONVOLUTION_HEIGHT_EXT',0x8019)
GL_CONVOLUTION_WIDTH_EXT=_C('GL_CONVOLUTION_WIDTH_EXT',0x8018)
GL_MAX_CONVOLUTION_HEIGHT_EXT=_C('GL_MAX_CONVOLUTION_HEIGHT_EXT',0x801B)
GL_MAX_CONVOLUTION_WIDTH_EXT=_C('GL_MAX_CONVOLUTION_WIDTH_EXT',0x801A)
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT=_C('GL_POST_CONVOLUTION_ALPHA_BIAS_EXT',0x8023)
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT=_C('GL_POST_CONVOLUTION_ALPHA_SCALE_EXT',0x801F)
GL_POST_CONVOLUTION_BLUE_BIAS_EXT=_C('GL_POST_CONVOLUTION_BLUE_BIAS_EXT',0x8022)
GL_POST_CONVOLUTION_BLUE_SCALE_EXT=_C('GL_POST_CONVOLUTION_BLUE_SCALE_EXT',0x801E)
GL_POST_CONVOLUTION_GREEN_BIAS_EXT=_C('GL_POST_CONVOLUTION_GREEN_BIAS_EXT',0x8021)
GL_POST_CONVOLUTION_GREEN_SCALE_EXT=_C('GL_POST_CONVOLUTION_GREEN_SCALE_EXT',0x801D)
GL_POST_CONVOLUTION_RED_BIAS_EXT=_C('GL_POST_CONVOLUTION_RED_BIAS_EXT',0x8020)
GL_POST_CONVOLUTION_RED_SCALE_EXT=_C('GL_POST_CONVOLUTION_RED_SCALE_EXT',0x801C)
GL_REDUCE_EXT=_C('GL_REDUCE_EXT',0x8016)
GL_SEPARABLE_2D_EXT=_C('GL_SEPARABLE_2D_EXT',0x8012)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter1DEXT(target,internalformat,width,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter2DEXT(target,internalformat,width,height,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glConvolutionParameterfEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glConvolutionParameterfvEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glConvolutionParameteriEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glConvolutionParameterivEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyConvolutionFilter1DEXT(target,internalformat,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyConvolutionFilter2DEXT(target,internalformat,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetConvolutionFilterEXT(target,format,type,image):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetConvolutionParameterfvEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetConvolutionParameterivEXT(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)
def glGetSeparableFilterEXT(target,format,type,row,column,span):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p)
def glSeparableFilter2DEXT(target,internalformat,width,height,format,type,row,column):pass