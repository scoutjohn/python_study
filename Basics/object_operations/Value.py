class Value:
    def __init__(self, data,_op=''):
        self.data = data
        self._op=_op

    def __repr__(self):
        return f"Value is {self.data}"

    def __add__(self, other):
        out = Value(self.data + other.data,'+')
        return out

    def __sub__(self, other):
        out = Value(self.data - other.data,'-')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data,'*')
        return out

    def __pow__(self, power, modulo=None):
        out = Value(self.data ** power,'**')
        return out
