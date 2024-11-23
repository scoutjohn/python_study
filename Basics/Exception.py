if __name__ == '__main__':
    try:
        val = int(input("Enter number"))
        if val<0:
            raise ValueError("Negative Number ")
    except ValueError as ve:
        print(ve)