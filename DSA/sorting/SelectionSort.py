def sort_array(array_):
    for i in range(len(array_) - 1):
        smallest_numbers_index = i
        for j in range(i + 1, len(array_)):
            if array_[j] < array_[smallest_numbers_index]:
                smallest_numbers_index = j
        if smallest_numbers_index != i:
            array_[i], array_[smallest_numbers_index] = array_[smallest_numbers_index], array_[i]
    return array_


if __name__ == '__main__':
    unsorted_array = [10, 5, 9, 1, 4, 3, 2]
    print(f" {sort_array(unsorted_array)}")
