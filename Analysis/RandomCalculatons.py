import numpy as np
import math


def Spread(radial_error_list):
    """
    This will create 10 evenly spaced bins
    :param radial_error_list:
    :return:
    """
    number = 11
    # Max and Min of radial error

    max_error = math.ceil(np.max(radial_error_list))
    min_error = math.floor(np.min(radial_error_list))
    # Difference between maximum and minimum
    # diff = max_error - min_error
    # If value is prime add one

    return np.linspace(min_error, max_error, 10)
    # if IsPrime(diff):
    #     diff += 1
    # while True:
    #     if diff % number == 0:
    #         try:
    #             return np.arange(0, max_error + diff / number, diff/number)
    #         except ZeroDivisionError:
    #             return np.array([0, 1])
    #     else:
    #         number -= 1


def IsPrime(value):
    if value < 0:
        print("Value should not negative. Will perform calculation on absolute value.")
        return None
    if value == 2 or value == 3:
        return True
    if value < 2 or value % 2 == 0 or value % 3 == 0:
        return False
    if value < 9:
        return True
    r = int(value ** .5)
    f = 5
    while f <= r:
        print(f)
        if value % f == 0:
            return False
        if value % (f + 2) == 0:
            return False
        f += 6
    return True


