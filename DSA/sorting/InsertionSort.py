def insertion_sort(unsorted):
    for index in range(1, len(unsorted)):
        temp_value = unsorted[index]
        left_of_index = index - 1
        print(f"Temp value {temp_value} from array {unsorted}")
        while left_of_index >= 0:
            if unsorted[left_of_index] > temp_value:
                unsorted[left_of_index + 1] = unsorted[left_of_index]
                left_of_index = left_of_index - 1
                print(f"array with GAP {unsorted} ")
            else:
                break
        unsorted[left_of_index + 1] = temp_value
        print(f"Array after fixing the GAP {unsorted}")
    return unsorted


if __name__ == '__main__':
    # array_ = [4, 2, 7, 1, 3]
    # print(f" {insertion_sort(array_)}")
    #
    # array_ = [9, 2, 7, 5, 3]
    # print(f" {insertion_sort(array_)}")
    #
    # array_ = [0,1, 2, 7, 5, 3]
    # print(f" {insertion_sort(array_)}")


    array_ = [10,9,8,7,6,5,3,2,1,0]
    print(f" {insertion_sort(array_)}")