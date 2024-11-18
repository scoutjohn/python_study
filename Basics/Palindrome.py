def palindrome(param):
    left_index = 0
    right_index = len(param) - 1
    while left_index < len(param) // 2:
        if param[left_index] != param[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


if __name__ == '__main__':
    print(f" {palindrome('madam')}")
    print(f" {palindrome("malayalam")}")
    print(f" {palindrome('john')}")
