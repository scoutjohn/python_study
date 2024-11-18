if __name__ == '__main__':
    #create dictionary using dict()
    my_dict=dict()
    print(my_dict)
    # create dictionary using dict() from tuple
    my_dict_1 = dict([(1,"abc"),(2,"def")])
    print(my_dict_1)

    my_dict_2 = {1:"test"}
    print(my_dict_2)
    # add new value
    my_dict_2[2]="new_value"
    print(my_dict_2)

    # remove value
    print(my_dict_1.pop(1))
    print(my_dict_1)

    my_dict_3 = {1: "abc",2: "def",3: "ghi",4: "jkl",5: "mno"}
    my_dict_4 = my_dict_3.copy()

    print(my_dict_3)
    my_dict_3.popitem()
    print(my_dict_3)
    my_dict_3.popitem()
    print(my_dict_3)

    del my_dict_3[3]
    print(my_dict_3)

    my_dict_3.clear()
    print(my_dict_3)

    print(f"my_dict_4 {my_dict_4}")

    my_dict_5={}.fromkeys(["a","b"],0)
    print(f"my_dict_5 {my_dict_5}")

    print(my_dict_4.items())
    print(my_dict_4.values())
    print(my_dict_4.keys())

    print("all the methods and attributes for dictionary")
    print(dir(my_dict))

    #make dictionary from another
    my_dict_6={k:v for k,v in my_dict_4.items() if k >3}
    print(f"my_dict_6 {my_dict_6}")

    my_dict_7={k**2:v+'...z' for k,v in my_dict_4.items()}
    print(f"my_dict_7 {my_dict_7}")

    #list items
    print("list items in a dictionary")
    for i in my_dict_7.items():
        print(i)