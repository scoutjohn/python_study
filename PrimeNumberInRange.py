
def get_prime_in_range(first, second):
    list_=[]
    for number in range(first,second+1):
        if number >1:
            is_p = False
            for val in range(2,int((number**0.5)+1)):
                if number % val ==0:
                    is_p = True
                    break
            if not is_p:
                    list_.append(number)

    print(f"prime numbers between {first} and {second} are {list_}")




if __name__ == '__main__':
    first = int(input("Enter first number "))
    second = int(input("Enter second number "))
    get_prime_in_range(first,second)
