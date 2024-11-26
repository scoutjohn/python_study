def double_values(_array,index=0):
    if index>=len(_array):
        return _array

    _array[index]*=2
    return double_values(_array,index+1)


if __name__ == '__main__':
    a = [1,2,3,4]
    print(double_values(a))