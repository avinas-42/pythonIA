
class Matrix:
    def __init__(self, values):
        valideMatrix = True
        self.values = []
        self.shape = (-1, -1)
        shape0 = -1
        shape1 = -1
        if isinstance(values, tuple):
            if len(values) == 2:
                if isinstance(values[0], int) and isinstance(values[1], int):
                    if values[0] > 1 and values[1] > 1:
                        self.values = Matrix.init_list(values[0], values[1])
                        self.shape = values
        elif isinstance(values, list):
            shape0 = len(values)
            for float_or_list in values:
                if isinstance(float_or_list, list)\
                    and len(float_or_list) > 1:
                    if shape1 == -1:
                        shape1 = len(float_or_list)
                    elif shape1 != len(float_or_list):
                        valideMatrix = False
                    for elem in float_or_list:
                        if not isinstance(elem, float):
                            valideMatrix = False
                else:
                    valideMatrix = False
        else:
            valideMatrix = False
        
        if valideMatrix:
            
            self.values = values
            self.shape = (shape0, shape1)
        if len(self.values) < 1:
            print("wrong data format")
            quit()
    @staticmethod
    def is_v(first, second):
        if second is None:
            if isinstance(first, Vector):
                return True
            return False
        elif isinstance(first, Vector) or isinstance(second, Vector) :
            return True
        return False

    def T(self):
        ret = Matrix.init_list(self.shape[1], self.shape[0])
        print(ret)
        if self.shape[1] == 1:
            for x in range(0, self.shape[0]):
                ret[x] = self.values[x][0]
        else:
            for x in range(0, self.shape[1]):
                for y in range(0, self.shape[0]):
                    ret[x][y] = self.values[x]
        if Matrix.is_v(self, None):
            return Vector(ret)
        else:
            return Matrix(ret)

    def dot(self, other):
        if self.shape != other.shape:
            print('ShapeError("dot : only vectors of same dimensions.")')
            return None
        ret = 0
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret += self.values[x] * other.values[x]
            else:
                for y in range(0, self.shape[0]):
                    ret += (self.values[y][x] * other.values[y][x])
        return ret
    @staticmethod
    def init_list(x, y):
        ret = []
        if x == 1:
            ret = [0.0] * y
        else:
            for i in range(x):
                ret.append([0.0] * y)

        return ret

    def __add__(self, other):
        if self.shape != other.shape:
            print('ShapeError("add : only vectors of same dimensions.")')
            return None
        ret = Matrix.init_list(self.shape[0], self.shape[1])

        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] + other.values[x]
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = (self.values[y][x] + other.values[y][x])
        if Matrix.is_v(self, other):
            return Vector(ret)
        else:
            return Matrix(ret)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.shape != other.shape:
            print('ShapeError("add : only vectors of same dimensions.")')
            return None
        ret = Matrix.init_list(self.shape[0], self.shape[1])

        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] - other.values[x]
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = (self.values[y][x] - other.values[y][x])
        if Matrix.is_v(self, other):
            return Vector(ret)
        else:
            return Matrix(ret)


    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, scalar):
        if scalar == 0:
            print('ValueError("cant div by 0".)')
            return None
        ret = Matrix.init_list(self.shape[0], self.shape[1])
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] / scalar
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = self.values[y][x] / scalar
        if Matrix.is_v(self, None):
            return Vector(ret)
        else:
            return Matrix(ret)


    def __rtruediv__(self, scalar):
        print('ValueError("A scalar cannot be divided by a Vector".)')
        return None

    def __mul__(self, other):
        ret = Matrix.init_list(self.shape[0], self.shape[1])
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] * scalar
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = self.values[y][x] * scalar
        if Matrix.is_v(self, None):
            return Vector(ret)
        else:
            return Matrix(ret)
    
    def __repr__(self):
        return "\n" + str(self.values) + \
            "\n" + str(self.shape)
    
    def __str__(self):
        return "\nmatrix: " + str(self.values) + \
            "\nshape: " + str(self.shape)

class Vector(Matrix):
    def __init__(self, values):
        valideRow = True
        valideColumn = True

        length = 0
        self.values = []
        self.shape = (0, 0)
        if isinstance(values, tuple):
            if len(values) == 2:
                if isinstance(values[0], int) and isinstance(values[1], int):
                    if values[0] != values[1]:
                        for i in range(values[0], values[1]):
                            self.values.append([float(i)])
                        self.shape = (len(self.values), 1)

        elif isinstance(values, int):
            if values > 0:
                for i in range(0, values):
                    self.values.append([float(i)])
                self.shape = (values, 1)

        elif isinstance(values, list):
            length = len(values)
            if length > 0:
                for float_or_list in values:
                    if valideRow:
                        if not isinstance(float_or_list, float):
                            valideRow = False
                    if valideColumn:
                        if not isinstance(float_or_list, list):
                            valideColumn = False
                        else:
                            for elem in float_or_list:
                                if valideColumn:
                                    if not isinstance(elem, float):
                                        valideColumn = False
            if valideRow:
                self.values = values
                self.shape = (1, length)
            if valideColumn:
                self.values = values
                self.shape = (length, len(values[0]))
            if len(self.values) < 1:
                print("wrong data format")
                quit()

    def __mul__(self, scalar):
        ret = Matrix.init_list(self.shape[0], self.shape[1])
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] * scalar
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = self.values[y][x] * scalar
        if Matrix.is_v(self, None):
            return Vector(ret)
        else:
            return Matrix(ret)


    def __rmul__(self, scalar):
        print('ValueError("A scalar cannot be multiplied by a Vector".)')
        return None

    def __repr__(self):
        return "\n" + str(self.values) + \
            "\n" + str(self.shape)

    def __str__(self):
        return "\nvector: " + str(self.values) + \
            "\nshape: " + str(self.shape)
