def number_of_path(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return number_of_path(n - 1) + number_of_path(n - 2) + number_of_path(n - 3)


if __name__ == '__main__':
    print(number_of_path(4))
