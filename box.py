class Box:
    def add(self, *items):
        print("Add")

    def empty(self):
        print("Empty")

    def count(self):
        print("Count")

class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Listbox(Box):
    def __init__(self):
        self.items = []

    def add(self, *args):
        self.items.extend(args)

    def empty(self):
        out = self.items
        self.items = []
        return out

    def count(self):
        return len(self.items)

class Dictbox(Box):
    def __init__(self):
        self.items = {}

    def add(self, *args):
        self.items.update(dict((i.name, i) for i in args))

    def empty(self):
        itemsList = self.items.values()
        self.items = {}
        return itemsList

    def count(self):
        return len(self.items)

def repack(*boxes):
    items = []
    print("repacking...")

    for box in boxes:
        items.extend(box.empty())
    
    print("Total Items: ",len(items))
    while items:
        for box in boxes:
            if len(items)> 0:
                box.add(items.pop())

            

def main():
    box1 = Listbox()
    box1.add(Item("1", 123))
    box1.add(Item("2", 1234))
    box3 = Listbox()
    box3.add(Item("3", 12345))
    box3.add(Item("4", 123456))
    box2 = Dictbox()
    box2.add(Item("5", 1234567))

    repack(box1, box2,box3)
    print("First Box Item Count: ",box1.count())
    print("Second Box Item Count: ",box2.count())
    print("Third Box Item Count: ",box3.count())

if __name__=="__main__":
    main()