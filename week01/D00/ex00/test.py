from matrix import Vector
from matrix import Matrix

def main():

    v1d = Vector([[0.0], [0.5], [1.0], [1.5]])
    v2d = Vector([[2.0], [0.4], [5.0], [1.7]])
    v1d = Vector(4)
    v4d = Vector((10, 15))
    v2 = Vector([2.0, 4.0, 6.0])
    v1 = Vector([1.0, 3.0, 5.0])
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
    [0.0, 2.0, 4.0, 6.0]])
    print(m1)
    m2 = Matrix([[0.0, 1.0],
    [2.0, 3.0],
    [4.0, 5.0],
    [6.0, 7.0]])
    
    print(m2)
    print("--------------------")
    m1 = m2 + m2
    print(m1)
    # Output:
    # Matrix([[28., 34.], [56., 68.]])

    print(v4d)

    print(v1)
    result = v1.T()
    print("Transpose")
    print('-------')
    print(result)
    print('-------')

    print("dot v2 per v1 ")
    result = v2.dot(v1)
    print(v2)
    print(v1)
    print('-------')
    print(result)
    print('-------')

    print(v1)
    result = v1d * 5
    print("multiplied per 5")
    print('-------')
    print(result)
    print('-------')

    print("div per 2")
    result = v2d / 2.0
    print(v1)
    print('-------')
    print(result)
    print('-------')

    print("div per v2d")
    result = 2.0 / v2d
    print(v1)
    print('-------')
    print(result)
    print('-------')

    print("v2d + v1d")
    result = v2d + v1d
    print(v1)
    print('-------')
    print(result)
    print('-------')

    print(v1)
    result = v2 - v1
    print("v2 - v1")
    print('-------')
    print(result)
    print('-------')


if __name__ == "__main__":
    main()
