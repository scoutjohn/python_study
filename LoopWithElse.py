def test_while():
    data = [1,2,3,4]
    i=0
    p=1
    while i < len(data):
        p*=data[i]
        i+=1
    else :
        print(f"while loop is done {p}")
    print(f"product {p}")

if __name__ == '__main__':
    test_while()