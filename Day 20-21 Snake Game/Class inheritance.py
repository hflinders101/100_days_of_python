class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale')


class Fish(Animal):

    def __init__(self):
        super().__init__() #I now have access to everyhting in Animal class
    def swim(self):
        print('move in water')

    def breathe(self):
        super().breathe()
        print('Doing this under water') #adds unique thing to breath that an animal does

nemo = Fish()
nemo.swim()
nemo.breathe()
