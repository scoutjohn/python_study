def transpose_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    print(len(matrix))
    transpose = []
    for index in range(3):
        temp_list = []
        for row in matrix:
            temp_list.append(row[index])
        transpose.append(temp_list)
    print(transpose)


def basic_list_operations():
    lst = [1, 2, 3, 4, 5]
    lst2 = [7, 8, 9, 10]
    print(lst)
    lst.append(6)
    lst.insert(0, 8)
    sorted(lst)
    print(lst)
    print(f"sorted {sorted(lst)}")
    lst.extend(lst2)
    print(lst)
    lst.remove(8)
    print(lst)
    lst.pop()
    print(lst)
    print(f"Hello {lst[-1::1]}")
    lst.clear()
    print(lst)


if __name__ == '__main__':
    basic_list_operations()

    transpose_matrix()