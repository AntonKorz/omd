import json
import keyword
from typing import List


class ColorizeMixin:
    def __init__(self, color):
        self.repr_color_code = color


class Json2:
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
            elif key == "price":
                lst.append(str(value) + ' Руб')
            elif key == 'class_' or key == 'repr_color_code':
                continue
            else:
                lst.append(value)
        return lst


class Advert(ColorizeMixin, Json2):
    def __init__(self, json_file, color=32, x=0):
        super().__init__(color)
        if x == 0:
            self.__dict__['price'] = 0
        json_dict = self.json2dict(json_file)
        for key, value in json_dict.items():
            if isinstance(value, dict):
                self.__dict__[key] = Advert(value, color, x=1)
            else:
                if keyword.iskeyword(key):
                    self.__dict__[key + '_'] = value
                else:
                    if key == 'price' and value < 0:
                        raise ValueError('price < 0')
                    else:
                        self.__dict__[key] = value

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('price < 0')
        else:
            self.__dict__[key] = value

    def __str__(self):
        lipstick = self.dict2lst(self.__dict__, [])
        strok = ''
        for i in range(len(lipstick) - 1):
            strok += str(lipstick[i]) + ' | '
        else:
            strok += str(lipstick[i + 1])

        return f'\033[1;{self.repr_color_code};40m' + strok


lesson_str = """{
"title": "Python",
"price": 33,
"location": {
"address": "Город Москва, Лесная, 7",
"metro_stations": ["Белорусская", "Таганская"]
}
}"""

a = Advert(lesson_str, 32)
print(a)
