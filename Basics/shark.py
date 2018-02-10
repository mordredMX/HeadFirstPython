class Shark:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def swim(self):
        print(self.name+" is swimming")

    def be_awesome(self):
        print(self.name+" is being awesome")


def main():
    sammy=Shark("Sammy",5)
    ##sammy.swim();
    sammy.be_awesome()
    stevie=Shark("Stevie",3)
    stevie.swim()

if __name__=="__main__":
    main()
