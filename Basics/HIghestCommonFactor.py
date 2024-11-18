def get_hcf(number_1, number_2):
    """
    Compute hcf for given two numbers
    :param number_1
    :param number_2
    :return hcf
    """
    smallest = number_2 if number_1 > number_2 else number_1
    #print(f"smallest : {smallest}")
    hcf = 1
    for i in range(1, smallest + 1):
        if number_1 % i == 0 and number_2 % i == 0:
            hcf = i

    return hcf


if __name__ == '__main__':
    print(get_hcf.__doc__)
    val = get_hcf(10, 20)
    print(f"{val}")

    val = get_hcf(40, 20)
    print(f"{val}")

    val = get_hcf(15, 20)
    print(f"{val}")
