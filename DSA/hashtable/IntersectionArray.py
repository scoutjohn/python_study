def get_intersection(array_1, array_2):
    hash_table ={}
    if len(array_1) > len(array_2):
        larger_array = array_1
        smaller_array = array_2
    else:
        larger_array = array_2
        smaller_array= array_1

    for val in larger_array:
        hash_table[val]=True

    intersection = []
    for value in smaller_array:
        if hash_table.get(value):
            intersection.append(value)

    return intersection



if __name__ == '__main__':

    array_1 = ["a","b","c","d","e","f"]
    array_2 = ["j","b","e","f","i"]
    print(f" {array_1} {array_2} is  {get_intersection(array_1, array_2)}")



    array_1 = [1,2,3,9,13,19,6]
    array_2 = [10,9,8,7,6,5,4,3,2,1]
    print(f" {array_1} {array_2} is  {get_intersection(array_1, array_2)}")