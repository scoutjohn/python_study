def sum_of_numbers(array):
    if not array:
        return 0
    # this statement is not needed because , a[1:] on an array with one value will give empty array
    #if(len(array))==1:
        #return array[0]
    return array[0]+sum(array[1:])


if __name__ == '__main__':
    arr = [1,2,3,4]
    print(f"sum of {arr} is {sum_of_numbers(arr)}")

    arr = [10,20,3,14]
    print(f"sum of {arr} is {sum_of_numbers(arr)}")
