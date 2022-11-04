import json
import keyword
from typing import List


class ColorizeMixin:
    def __init__(self, color):
        self.repr_color_code = color

    def __init_subclass__(cls, **kwargs):
        cls.__str__ = cls.new_str

    def new_str(self):
        lipstick = self.dict2lst(self.__dict__, [])
        strok = ''
        for i in range(len(lipstick) - 1):
            strok += str(lipstick[i]) + ' | '
        else:
            strok += str(lipstick[i + 1])

        return f'\033[1;{self.repr_color_code}m' + strok


class Json2:

    def __init__(self, x):
        pass

    @staticmethod
    def json2dict(json_file) -> dict:
        if isinstance(json_file, str):
            return json.loads(json_file)
        elif isinstance(json_file, dict):
            return json_file
        else:
            raise NameError('Not JSON file')

    @staticmethod
    def dict2lst(nested_dict, lst=[]) -> List:
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                lst.append(*nested_dict.dict2lst(value, []))
            elif isinstance(value, list):
                lst.extend(value)
            elif key == 'price':
                lst.append(str(value) + ' Руб')
            elif key == 'class_' or key == 'repr_color_code':
                continue
            else:
                lst.append(value)
        return lst


class Advert(ColorizeMixin, Json2):

    def __init__(self, json_file, color=32, first_recursion_layer=True):
        super().__init__(color)
        if first_recursion_layer:
            self.__dict__['price'] = 0

        json_dict = self.json2dict(json_file)
        for key, value in json_dict.items():
            if isinstance(value, dict):
                self.__dict__[key] = Advert(value, color, False)
            else:
                if keyword.iskeyword(key):
                    self.__dict__[key + '_'] = value
                else:
                    if key == 'price' and value < 0:
                        raise ValueError('price < 0')
                    else:
                        self.__dict__[key] = value

        if first_recursion_layer and 'title' not in self.__dict__.keys():
            raise ValueError('No title')

    def __str__(self):
        lipstick = self.dict2lst(self.__dict__, [])
        strok = ''
        for i in range(len(lipstick) - 1):
            strok += str(lipstick[i]) + ' | '
        else:
            strok += str(lipstick[i + 1])
        return strok

    @property
    def price(self, x=0):
        print(self.price)

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__dict__['price'] = value
        else:
            raise ValueError('price < 0')


if __name__ == '__main__':
    lesson_str = """{
    "title": "Python",
    "price": 34,
    "location": {
    "address": "Город Москва, Лесная, 7",
    "metro_stations": ["Белорусская", "Таганская"]
    }
    }"""

    a = Advert(lesson_str, color=32)
    a.price = 10
    print(a)
