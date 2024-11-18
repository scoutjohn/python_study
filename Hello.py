import keyword
from array import array


def hello():
    print("hello")
    print(keyword.kwlist)

if __name__ == '__main__':
    hello()
    new_array = [1,2,3,4]
    for i,j in enumerate(new_array):
        print(f"index: {i} , value {j}")