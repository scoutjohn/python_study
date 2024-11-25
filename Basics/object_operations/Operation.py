from Basics.object_operations.Value import Value

if __name__ == '__main__':
    a = Value(3)
    b = Value(2)
    c = a + b
    print(c)

    c = a ** 4
    print(c)

    d = Value(4)
    e= a**2 - (b-d)
    print(e)
