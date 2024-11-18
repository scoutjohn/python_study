def find_duplicates(array_):
    existing_numbers = [0] * 9
    for i in range(len(array_)):
        if existing_numbers[array_[i]] == 1:
            print(f"True {i} : {existing_numbers}")
            return True
        else:
            existing_numbers[array_[i]] = 1
            print(f"{i} : {existing_numbers}")

    return False


if __name__ == '__main__':
    array_to_check = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"{find_duplicates(array_to_check)}")

    array_to_check = [8, 2, 3, 4, 5, 1, 7, 8]
    print(f"{find_duplicates(array_to_check)}")
