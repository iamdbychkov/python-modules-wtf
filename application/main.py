import typing

from enumerations import Colour


map: dict[Colour, int] = {}


def get_by_colour(colour: typing.Literal['red' , 'green' , 'blue']) -> int:

    print(f"Current colour map is: {map}")

    if colour == 'red':
        c = Colour(1)
    elif colour == 'green':
        c = Colour(2)
    elif colour == 'blue':
        c = Colour(3)
    else:
        raise ValueError(f'Invalid Value: {colour}')
    return map[c]


if __name__ == '__main__':
    map[Colour(1)] = 100
    map[Colour(2)] = 200
    map[Colour(3)] = 300

    print(get_by_colour('green'))