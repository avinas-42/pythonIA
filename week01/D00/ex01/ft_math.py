import pandas as pan
import numpy as np
import sys
from math import sqrt
from math import floor


def count(data):
    count = 0
    for element in data:
        if (pan.notna(element)):
            count += 1
    return (count)

def min(data):
    min = sys.float_info.max
    for element in data:
        if (pan.notna(element)):
            if(element < min):
                min = element
    return min

def max(data):
    max = sys.float_info.min
    for element in data:
        if (pan.notna(element)):
            if(element > max):
                max = element
    return max

def mean(data, total):
    somme = 0
    for element in data:
        if (pan.notna(element)):
            somme += element
    return (float(somme / total))

def std(data, mean, total):
    to_div = 0
    for element in data:
        if (pan.notna(element)):
            to_div += (element - mean)**2
    return (float(sqrt(to_div / (total - 1))))


