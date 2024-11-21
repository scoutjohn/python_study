from functools import reduce

if __name__ == '__main__':
    '''
        same as 
        def square(x):
            return x**2

    '''
    square = lambda x: x ** 2
    print(square(10))



    lst = [1,2,3,4,5]
    val = list(map(lambda x:x**2,lst))
    print(val)


    val = list(filter(lambda x:x>2,lst))
    print(val)


    val = reduce(lambda x,y:x*y,lst)
    print(val)