def is_subset(array_1, array_2):
    hash_table ={}
    if len(array_1) > len(array_2):
        larger_array = array_1
        smaller_array = array_2
    else:
        larger_array = array_2
        smaller_array= array_1

    for val in larger_array:
        hash_table[val]=True

    print(f" large array -> {hash_table}")

    is_present = True
    for value in smaller_array:
        if not hash_table.get(value):
            is_present = False

    return is_present



if __name__ == '__main__':

    array_1 = ["a","b","c","d","e","f"]
    array_2 = ["b","e","f"]
    print(f" {array_1} {array_2} is  {is_subset(array_1, array_2)}")

    array_1 = ["a","b","c","d","e","f"]
    array_2 = ["b","g","f"]
    print(f" {array_1} {array_2} is  {is_subset(array_1, array_2)}")

    array_1 = [1,2,3]
    array_2 = [10,9,8,7,6,5,4,3,2,1]
    print(f" {array_1} {array_2} is  {is_subset(array_1, array_2)}")