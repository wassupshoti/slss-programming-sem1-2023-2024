# Functions Practice
# Author: Ubial
# 24 November 2023

def area_of_square(sidelength: float) -> None:
    """""Calculates the area of a square.
    Results are in units squared.

    Params:
    sidelength - length of on side of the square"""""

    area = sidelength ** 2

    print(f"The area of a square with side length = {sidelength} is: {area} square units")


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength 

    Params:

    sidelength - length of one side of a square
    """

    area = sidelength ** 2

    return area


def stars(num_stars: int) -> str:
    """Return out the number of stars of a given number
    
    Params:
    
    num_stars - the number of stars to return"""

    return "*" * num_stars

def pyramid(num_layers: int) -> None:
    """Print out a pyramid of stars that is
    the given height.
    
    Params:
    
    num_layers - how many rows are in the pyramid
    """

    for current_layer in range(1, num_layers+1):
        print("*" * current_layer)
        # print(stars(current_layer))

def pyramid_mirror(layers: int) -> None:
    
    for current_layer_two in range(1, layers+1):
        spaces = " " * (layers - current_layer_two)
        
        print(spaces + stars(layers))

pyramid_mirror(5)