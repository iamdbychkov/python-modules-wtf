В папке application расположено два файла:

1. **enumerations.py** - здесь расположен `Colour(enum.Enum)`
2. **main.py** - здесь определён словарь `map: dict[Colour, int]`, где ключ - значение `Colour`, а значение - любое число. Здесь же расположена функция `get_by_colour` для получения данных из словаря по строке.

В папке tests расположен файл `test_get_by_colour` тестирующий функцию `get_by_colour`.

Тест оканчивается неудачей, хотя такой `Colour` есть в словаре:

```

E       KeyError: <Colour.RED: 1>

application/main.py:21: KeyError
---------------------------------------------------- Captured stdout call ----------------------------------------------------
Current colour map is: {<Colour.RED: 1>: 1, <Colour.GREEN: 2>: 2, <Colour.BLUE: 3>: 3}
```

Для запуска тестов в корневой директории тестов:

```sh
$ pytest
```

Однако запуск файла main.py напрямую работает как и ожидается:

```sh
$ python main.py
Current colour map is: {<Colour.RED: 1>: 100, <Colour.GREEN: 2>: 200, <Colour.BLUE: 3>: 300}
200
```

Почему? 


