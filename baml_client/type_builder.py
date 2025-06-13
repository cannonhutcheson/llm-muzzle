###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import typing
from baml_py.baml_py import FieldType, EnumValueBuilder, EnumBuilder, ClassBuilder
from baml_py.type_builder import TypeBuilder as _TypeBuilder, ClassPropertyBuilder, ClassPropertyViewer, EnumValueViewer
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME


class TypeBuilder(_TypeBuilder):
    def __init__(self):
        super().__init__(classes=set(
          ["CompletionHalt","ContextBlock","Error","InitBlock","Punctuate","Response","SentenceResponse",]
        ), enums=set(
          []
        ), runtime=DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME)


    @property
    def CompletionHalt(self) -> "CompletionHaltAst":
        return CompletionHaltAst(self)

    @property
    def ContextBlock(self) -> "ContextBlockAst":
        return ContextBlockAst(self)

    @property
    def Error(self) -> "ErrorAst":
        return ErrorAst(self)

    @property
    def InitBlock(self) -> "InitBlockAst":
        return InitBlockAst(self)

    @property
    def Punctuate(self) -> "PunctuateAst":
        return PunctuateAst(self)

    @property
    def Response(self) -> "ResponseAst":
        return ResponseAst(self)

    @property
    def SentenceResponse(self) -> "SentenceResponseAst":
        return SentenceResponseAst(self)





class CompletionHaltAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("CompletionHalt")
        self._properties: typing.Set[str] = set([ "reason", ])
        self._props = CompletionHaltProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "CompletionHaltProperties":
        return self._props


class CompletionHaltViewer(CompletionHaltAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class CompletionHaltProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def reason(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("reason"))

    

class ContextBlockAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("ContextBlock")
        self._properties: typing.Set[str] = set([ "prompt",  "limit",  "generated", ])
        self._props = ContextBlockProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ContextBlockProperties":
        return self._props


class ContextBlockViewer(ContextBlockAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ContextBlockProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def prompt(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("prompt"))

    @property
    def limit(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("limit"))

    @property
    def generated(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("generated"))

    

class ErrorAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Error")
        self._properties: typing.Set[str] = set([ "reason", ])
        self._props = ErrorProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ErrorProperties":
        return self._props


class ErrorViewer(ErrorAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ErrorProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def reason(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("reason"))

    

class InitBlockAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("InitBlock")
        self._properties: typing.Set[str] = set([ "prompt",  "limit", ])
        self._props = InitBlockProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "InitBlockProperties":
        return self._props


class InitBlockViewer(InitBlockAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class InitBlockProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def prompt(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("prompt"))

    @property
    def limit(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("limit"))

    

class PunctuateAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Punctuate")
        self._properties: typing.Set[str] = set([ "reason", ])
        self._props = PunctuateProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "PunctuateProperties":
        return self._props


class PunctuateViewer(PunctuateAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class PunctuateProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def reason(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("reason"))

    

class ResponseAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Response")
        self._properties: typing.Set[str] = set([ "word", ])
        self._props = ResponseProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ResponseProperties":
        return self._props


class ResponseViewer(ResponseAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ResponseProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def word(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("word"))

    

class SentenceResponseAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("SentenceResponse")
        self._properties: typing.Set[str] = set([ "sentence", ])
        self._props = SentenceResponseProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "SentenceResponseProperties":
        return self._props


class SentenceResponseViewer(SentenceResponseAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class SentenceResponseProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def sentence(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("sentence"))

    




__all__ = ["TypeBuilder"]