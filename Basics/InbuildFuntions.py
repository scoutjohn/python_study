from functools import reduce


def print_positive(num):
    if num > 0:
        return num

def power_of_two(num):
    return num**2

def multiply(num1,num2):
    return num1*num2

if __name__ == '__main__':
    print(f"abs(-5) is {abs(-5)}")

    print()
    print(f"dir([]) is {dir([])}")

    print()
    print(f"divmod(9,2) is {divmod(9, 2)}")

    print()
    print(f"all([1,2,3,4]) is {all([1, 2, 3, 4])}")

    print()
    print(f"all([1,0,3,4]) is {all([1, 0, 3, 4])}")

    # applies on each element
    num_list = range(-5, 5)
    print(list(num_list))
    new_list=list(filter(print_positive, num_list))
    print(new_list)

    print()
    print(isinstance(num_list,list))
    print(type(num_list))

    #applies on each element
    print()
    squared_list=list(map(power_of_two,new_list))
    print(squared_list)

    #rolling computation
    #filter, map and reduce avoids for loop
    #used extensively in data science
    print()
    multiplied_value=reduce(multiply,squared_list)
    print(multiplied_value)


