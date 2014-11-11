class SpecialStack:
    '''
    This is a special stack class to answer the interview question to design
    and implement a special stack data structure that supports push(), pop(),
    isEmpty() and the addiitonal getMin() which returns the
    minimum element from the SpecialStack
    '''

    def __init__(self):
        self.stack = []
        self.minStack = []

    def isEmpty(self):
        return len(self.stack) + len(self.minStack) == 0

    def push(self, data):
        if self.isEmpty() == True:
            self.stack.append(data)
            self.minStack.append(data)
        else:
            self.stack.append(data)     
            y = self.minStack.pop()
            self.minStack.append(y)

            # Only push when the new data of the stack is smaller or equal to teh
            # top of the minStack
            if (data <= y):
                self.minStack.append(data)
        
    # Special version of pop
    def pop(self):
        if self.isEmpty() == True:
            raise Exception("stack is empty")
        
        x = self.stack.pop()
        y = self.minStack.pop()

        # Push the popped data element y back only if it is not equal to x
        if (y != x):
            self.minStack.append(x)

        return x


    def getMin(self):
        if self.isEmpty() == True:
            raise Exception("stack is empty")
        
        x = self.minStack.pop()
        self.minStack.append(x)
        return x

# Test the class        
sp = SpecialStack()
print sp.isEmpty()
sp.push(10)
sp.push(15)
sp.push(20)
print sp.getMin()
sp.push(5)
print sp.getMin()
sp.pop()
print sp.getMin()


