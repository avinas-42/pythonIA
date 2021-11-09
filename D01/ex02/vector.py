
class Vector:
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
            large = 0
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

    def T(self):
        ret = self.init_list(self.shape[1], self.shape[0])
        print(ret)
        if self.shape[1] == 1:
            for x in range(0, self.shape[0]):
                ret[x] = self.values[x][0]
        else:
            for x in range(0, self.shape[1]):
                for y in range(0, self.shape[0]):
                    ret[x][y] = self.values[x]
        return Vector(ret)

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

    def init_list(self, x, y):
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
        ret = self.init_list(self.shape[0], self.shape[1])

        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] + other.values[x]
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = (self.values[y][x] + other.values[y][x])
        return Vector(ret)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.shape != other.shape:
            print('ShapeError("add : only vectors of same dimensions.")')
            return None
        ret = self.init_list(self.shape[0], self.shape[1])

        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] - other.values[x]
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = (self.values[y][x] - other.values[y][x])
        return Vector(ret)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, scalar):
        if scalar == 0:
            print('ValueError("cant div by 0".)')
            return None
        ret = self.init_list(self.shape[0], self.shape[1])
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] / scalar
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = self.values[y][x] / scalar
        return Vector(ret)

    def __rtruediv__(self, other):
        print('ValueError("A scalar cannot be divided by a Vector".)')
        return None

    def __mul__(self, scalar):
        ret = self.init_list(self.shape[0], self.shape[1])
        for x in range(0, self.shape[1]):
            if self.shape[0] == 1:
                ret[x] = self.values[x] * scalar
            else:
                for y in range(0, self.shape[0]):
                    ret[y][x] = self.values[y][x] * scalar
        return Vector(ret)

    def __rmul__(self, other):
        print('ValueError("A scalar cannot be multiplied by a Vector".)')
        return None

    def __repr__(self):
        return "\n" + str(self.values) + \
            "\n" + str(self.shape)

    def __str__(self):
        return "\nvector: " + str(self.values) + \
            "\nshape: " + str(self.shape)
