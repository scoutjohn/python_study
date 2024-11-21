import os


def create_file(filename):
    """
    Creates File
    :param filename:
    :return:
    """

    try:
        with open(filename, 'w') as f:
            f.write("this is a new file")
            f.close()
    except IOError:
        print("file cannot be written")


def read_file(filename):
    """
    Reads file
    :param filename:
    :return:
    """
    try:
        with open(filename, 'r') as f:
            print(f.read())
            f.close()
    except FileNotFoundError:
        print("File not found", filename)
    except IOError:
        print("IO error", filename)


def append_file(filename):
    """
    Append content to file
    :param filename:
    :return:
    """
    try:
        with open(filename, 'a') as f:
            f.write("\nnew data input")
            f.close()
    except FileNotFoundError:
        print("File not found", filename)
    except IOError:
        print("IO error", filename)


def rename_file(filename, new_filename):
    """
    Rename file with a new name
    :param filename:
    :param new_filename:
    :return:
    """
    try:
        os.rename(filename, new_filename)
    except IOError:
        print("file rename error", filename)


def remove_file(filename):
    """
    Removes file
    :param filename:
    :return:
    """
    try:
        os.remove(filename)
    except IOError:
        print("File cannot be removed")


if __name__ == '__main__':

    cwd = os.getcwd()
    print(cwd)
    os.chdir("../")
    cwd = os.getcwd()
    print(cwd)

    file_name = cwd + "/test.txt"
    new_file_name = cwd + "/test_new.txt"

    create_file(file_name)
    read_file(file_name)
    append_file(file_name)
    read_file(file_name)
    rename_file(file_name,new_file_name)
    read_file(new_file_name)
