import pandas as pan
import numpy as np
import sys
from ft_math import *
from math import ceil


def check_col_str(data):
    for element in data:
        if (pan.notna(element) and type(element) is str):
                return (1)
    return (0)

def read_file():
    try:
        data = pan.read_csv(sys.argv[1])
    except:
        sys.exit("File doesn't exist")
    keys = []
    for key in data:
        if (check_col_str(data[key])):
            data.drop([key], axis = 1, inplace = True)
        else:
            keys.append(key)
    data_describe = pan.DataFrame(0.000, index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], columns = keys)
    return (data, data_describe, keys)

def main():
    if (len(sys.argv) <= 1):
        sys.exit("No name file")
    if (len(sys.argv) >= 3):
        sys.exit("too much file")
    data, data_describe, keys = read_file()
    for key in keys:
        sortedData = np.sort(np.array(data[key], dtype=float))
        data_describe[key]['count'] = ft_math.count(data[key])
        data_describe[key]['min'] = ft_math.min(data[key])
        data_describe[key]['max'] = ft_math.max(data[key])
        data_describe[key]['mean'] = ft_math.mean(data[key], data_describe[key]['count'])
        data_describe[key]['std'] = ft_math.std(data[key], data_describe[key]['mean'],data_describe[key]['count'])
        data_describe[key]['25%'] = sortedData[ceil(len(sortedData)/4) - 1]
        data_describe[key]['50%'] = sortedData[ceil(len(sortedData)/2) - 1]
        data_describe[key]['75%'] = sortedData[ceil(3*len(sortedData)/4) - 1]
    print(data_describe)

if __name__ == "__main__":
    main()