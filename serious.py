# class EmptyClass:
#     For creating an empty class
#     pass


class NewClass:

    name = None
    surname = None

    #Constructor of NewClass
    def __init__(self, name, surname):
        print("This is the constructor")
        self.name = name
        self.surname = surname


    def __repr__(self):
        return self.surname


    def __str__(self):
        return self.name
        

    def hello(self):
        print("Hello, world!")


class MarksCalc(NewClass):

    def __init__(self):
        print("Hello from MarksCalc()")


    def marks(self):
        self.hello()


# Object of NewClass
obj = NewClass("Mayank", "Soni")
obj.hello()

obj2 = MarksCalc()
obj2.marks()

