#class to lint java based scripts

from DSA.stack.Stack import Stack

class CodeLinter:
    def __init__(self):
        self.stack=Stack()

    def lint(self,text):
        #ensure the stack is empty
        # remove anything that is previously present
        while self.stack.read():
            self.stack.pop()

        matching_braces = {"(":")","[":"]","{":"}"}

        for char in text:
            #push every opening brace to stack
            if char in matching_braces:
                self.stack.push(char)
            #if the character in the text is available in the key:value
            elif char in matching_braces.values():
                #check if stack is empty, if empty throw error
                if not self.stack.read():
                    return char + "in "+ text+ " does not have an opening brace"
                else:
                    #compare the top value in the stack
                    popped_opening_brace=self.stack.pop()
                    if char!= matching_braces.get(popped_opening_brace):
                        return char + "in "+ text+ " has mismatched opening brace"
        #if we reach to the end of the line and there is an entry in the stack
        if self.stack.read():
            return self.stack.read() + "in "+ text+ " does not have a closing brace "

        return text + " is properly linted"
