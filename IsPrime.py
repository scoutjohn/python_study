def is_divisible(n, divisor):
    return n % divisor == 0


def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, int(number**0.5)+1): # range of square root is better than half
        if is_divisible(number, divisor):
            return False
    return True



if __name__ == '__main__':
    is_num_prime = is_prime(int(input("Enter Number ")))
    if is_num_prime:
        print(f"The number is prime")
    else:
        print(f"The number is not a prime")