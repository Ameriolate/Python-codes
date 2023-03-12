class Legs:
    def number(self):
        print("It has four legs")
class animal(Legs):
    def type(self):
        print("Its a cow and it mows")
class animal2(Legs):
    def type(self):
        print("Its a cat and it meows")
a1=animal()
a2=animal2()
a1.number()
a1.type()
a2.number()
a2.type()

        
