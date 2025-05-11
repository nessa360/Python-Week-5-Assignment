# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def move(self):
        return "Animal is moving."
        
class Millipede(Animal):
    def move(self):
        return  "Crawling."
    
class Dolphin(Animal):
    def move(self):
        return "Swimming."

if __name__ == "__main__":
    walkerPede = Millipede()
    print(walkerPede.move())

    my_dolphin = Dolphin()
    print(my_dolphin.move())    
