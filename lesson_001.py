
# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

from array import *

def sum_array(a: array) -> float:
    sum: float = 0
    if len(a) == 0:
        return 0
    for element in a:
        if isinstance(element, float) or isinstance(element, int):
            sum += element

    return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_array('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
