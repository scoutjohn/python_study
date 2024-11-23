import numpy as np

if __name__ == '__main__':
    a = np.array([1, 2, 3, 4, 5])
    print(a)
    print(np.arange(5))
    print("number of attributes and functions in numpy : {0}".format(len(dir(np))))
    print(f"Array Dimension : {a.ndim}")
    print(f"Shape (number of elements)  : {a.shape}")
    print()

    b = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
    print(b)
    print(f"Array Dimension : {b.ndim}")
    print(f"Shape (number of elements)  : {b.shape}")
    print(f"length  : {len(b)}")
    print()

    c = np.array([[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 13, 14]])
    print(c)
    print(f"Array Dimension : {c.ndim}")
    print(f"Shape (number of elements)  : {c.shape}")
    print(f"length  : {len(c)}")
    print()

    d = np.array([[[1, 2, 0], [3, 4, 0]], [[4, 5, 0], [6, 7, 0]], [[4, 5, 0], [6, 7, 0]]])
    print(d)
    print(f"Array Dimension : {d.ndim}")
    print(f"Shape (number of elements)  : {d.shape}")
    print(f"length  : {len(d)}")
    print()

    print("array from 1 to 10 with step 2")
    e = np.arange(1,10,2)
    print(e)
    print()

    print("divide 1 to 10 by 6 equal space np.linspace(1,10,6)")
    e = np.linspace(1,10,6)
    print(e)
    print()

    print("2D array of 1s")
    e = np.ones((3,3))
    print(e)
    print()

    print("2D array of 0s")
    e = np.zeros((3,3))
    print(e)
    print()

    print("identity matrix")
    e=np.eye(3)
    print(e)
    print()

    print("identity matrix")
    e=np.eye(3,2)
    print(e)
    print()


