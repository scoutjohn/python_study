import os


def print_file_in_subdirectories(path_name):
    for filename in os.listdir(path_name):
        path=os.path.join(path_name,filename)
        if os.path.isdir(path):
            print_file_in_subdirectories(path)
        else:
            print(path)


if __name__ == '__main__':
    print_file_in_subdirectories("/Users/scoutjohn13/Documents/Python/pycharm_projects/PythonProject/DSA")