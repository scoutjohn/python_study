def sort(unsorted_list):
    print(f"Unsorted Array is {unsorted_list}")
    sorting_index = len(unsorted_list) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(sorting_index):
            print(f"i is {i} now, array is {unsorted_list} length is {sorting_index}")
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                is_sorted = False
                print(f"array inside is {unsorted_list}")
        print("Exit for loop")
        sorting_index -= 1

    print(f"Sorted Array is  {unsorted_list}")


if __name__ == '__main__':
    random_list = [9, 1, 4, 3, 5, 10, 5,2]
    sort(random_list)
