def binary_search(list_, value):
    start_index = 0
    end_index = len(list_) - 1
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if value == list_[midpoint]:
            print(f"{value} is present in index {midpoint} of {list_}")
            break
        elif value < list_[midpoint]:
            end_index = midpoint - 1
        elif value > list_[midpoint]:
            start_index = midpoint + 1

    print(f"{value} is not found in {list_}")


if __name__ == '__main__':
    ordered_list = [1, 2, 3, 4, 5]
    search_value = int(input("Enter value to be found"))
    binary_search(ordered_list, search_value)
