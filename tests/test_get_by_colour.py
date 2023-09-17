import pytest

from application.enumerations import Colour
from application.main import get_by_colour, map


@pytest.fixture(autouse=True)
def fill_colour_map():
    map[Colour(1)] = 1
    map[Colour(2)] = 2
    map[Colour(3)] = 3
    yield
    map.clear()


def test_getting_colour():
    assert get_by_colour('red') == 1, 'Неудалось получить значение по строке \'red\''
    assert get_by_colour('green') == 2, 'Неудалось получить значение по строке \'green\''
    assert get_by_colour('blue') == 3, 'Неудалось получить значение по строке \'blue\''