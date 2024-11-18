if __name__ == '__main__':
    #create dictionary using dict()
    my_dict=dict()
    print(my_dict)
    # create dictionary using dict() from tupple
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
    print(my_dict_3)
    my_dict_3.popitem()
    print(my_dict_3)
    my_dict_3.popitem()
    print(my_dict_3)

    del my_dict_3[3]
    print(my_dict_3)

    my_dict_3.clear()
    print(my_dict_3)
