def print_numbers(_array):

    for val in _array:
        if isinstance(val,list):
            print_numbers(val)
        else:
            print(val)


if __name__ == '__main__':
    array_=[
        1,
        2,
        3,
        [5,6,7,8],
        10,
        [11,
         [12,13,14],
         15],
        16
    ]
    print_numbers(array_)