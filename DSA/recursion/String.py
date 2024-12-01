def reverse(s):
    if not s:
        return ""
    return reverse(s[1:])+s[0]

def count_specific_char_in_string(s,_char):
    if not s:
        return 0
    if s[0]==_char:
        return 1 + count_specific_char_in_string(s[1:],_char)
    else:
        return count_specific_char_in_string(s[1:],_char)


if __name__ == '__main__':
    print(f"!NataSha = {reverse('!NataSha')}")

    str = "axbxcx"
    c = "x"
    print(f"{c} in {str} is repeated {count_specific_char_in_string(str,c)} times")
