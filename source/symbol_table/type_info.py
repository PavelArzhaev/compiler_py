from enum import Enum
from typing import Optional

from syntax_tree import Type, ClassType


class TypeEnum(Enum):
    """
    Перечисление существующих типов (UserClass для пользовательского класса)
    Используется в st и далее (т.е. кроме ast)
    """
    INT = 1
    INT_ARRAY = 2
    BOOLEAN = 3
    USER_CLASS = 4


class TypeInfo:
    """
    Хранит информацию о типе, в случае пользовательского класса - его название
    """

    def __init__(self, type_enum: TypeEnum, user_class_name: Optional[str]):
        """
        Конструктор
        :param type_enum: Один из возможных вариантов типов
        :param user_class_name: Название пользовательского класса в случае (UserClass)
        """
        self.type_enum = type_enum
        if self.type_enum == TypeEnum.USER_CLASS:
            self.user_class_name = user_class_name
        else:
            self.user_class_name = None

    def get_type_string(self):
        """
        Отвечает за получение "человеческого" представления типа
        :return:
        """
        if self.type_enum == TypeEnum.INT:
            return 'int'
        if self.type_enum == TypeEnum.INT_ARRAY:
            return 'int []'
        if self.type_enum == TypeEnum.BOOLEAN:
            return 'boolean'
        if self.type_enum == TypeEnum.USER_CLASS:
            return self.user_class_name
        raise KeyError()

    @classmethod
    def from_type(cls, type_of: Type):
        """
        Отвечает за конвертацию из AST Type в ST TypeInfo
        :param type_of:
        :return:
        """
        if isinstance(type_of, ClassType):
            obj = cls(TypeEnum.USER_CLASS, type_of.label)
        elif type_of.label == 'int_array':
            obj = cls(TypeEnum.INT_ARRAY, 'int []')
        elif type_of.label == 'int':
            obj = cls(TypeEnum.INT, 'int')
        elif type_of.label == 'boolean':
            obj = cls(TypeEnum.BOOLEAN, 'bool')
        else:
            raise Exception
        return obj

    def __eq__(self, other):
        """
        Отвечает за сравнение типов (не по ссылке, а по значению)
        :param other:
        :return:
        """
        if self.type_enum == other.type_enum and self.type_enum != TypeEnum.USER_CLASS:
            return True
        if self.type_enum == TypeEnum.USER_CLASS and \
                other.type_enum == TypeEnum.USER_CLASS and \
                self.user_class_name == other.user_class_name:
            return True
        return False
