def biggest_number_in_array(array_):
    if  not array_:
        return None

    biggest_number = array_[0]
    for i in array_:
        if i > biggest_number:
            biggest_number = i
    return biggest_number



if __name__ == '__main__':
    array_to_check = [8, 2, 3, 4, 5, 1, 7, 9]
    bn=biggest_number_in_array(array_to_check)
    print(f"{bn}")

    array_to_check = [8, 2, 3, 10, 5, 1, 7, 9]
    bn = biggest_number_in_array(array_to_check)
    print(f"{bn}")

    array_to_check = ""
    bn = biggest_number_in_array(array_to_check)
    print(f"{bn}")