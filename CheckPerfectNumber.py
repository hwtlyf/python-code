import os
import sys
import math

def checkPerfectNumber(num):
    """
    完美数：对于一个正整数，如果它和除了它自身意外的所有的正因子之和相等，称之为完美数；
    :param num:
    :return:
    """
    if num == 1:
        return False
    midNum = math.sqrt(num)
    sum, index = 1, 2
    while index < midNum:
        if (num % index == 0):
            sum += index
            sum += num // index
        index += 1
    if midNum ** 2 == num:
        sum += midNum
    #print("sum: %d; num: %d; midsum: %f." % (sum, num, midNum))
    return sum == num

if __name__ == "__main__":
    num = eval(input("please input a number."))
    print(checkPerfectNumber(num))