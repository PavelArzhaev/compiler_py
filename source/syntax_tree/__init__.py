from .base import *
from .declarations import *
from .expressions import *
from .grammar import *
from .printer import *
from .statements import *
from .types import *

"""
В данном модуле описаны все классы абстрактного синтаксического дерева (AST).
В файле base определены классы Visitor и Visitable - базовые классы для всех
визиторов дерева и всех узлов дерева.
В файле printer определен класс Printer - обходит дерево и генерирует файл .gv
на его основе.
В остальных файлах описаны остальные узлы дерева AST (разделены по группам:
declarations, expressions, statements, types, grammar.
В комментариях к классам есть краткие пояснения по поводу того, за что конкретно
они отвечают
"""
