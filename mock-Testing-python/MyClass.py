class User:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        return "hi my name is: {}".format(self.name)

# instantiates MyClass and calls a method on the object
def function_b():
    param1 = User("foo")

    # returns "hi my name is: foo"
    return param1.sayhi()
