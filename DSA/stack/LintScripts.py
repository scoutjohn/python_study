from DSA.stack.CodeLinter import CodeLinter

if __name__ == '__main__':
    linter = CodeLinter()
    print("Lint 1")
    return_value = linter.lint("{var x=2;}")
    print(f"{return_value}")

    print("Lint 2")
    return_value =linter.lint("(var x=2;}")
    print(f"{return_value}")

    print("Lint 3")
    return_value =linter.lint("var x=2;}")
    print(f"{return_value}")

    print("Lint 4")
    return_value =linter.lint("{var x=2;")
    print(f"{return_value}")