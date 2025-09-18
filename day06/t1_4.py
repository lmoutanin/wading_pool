def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

def prepare_sand(x):
    if type(x) == int :
        for i in range(x) :
            sandwich()
            print()
    else :
        print("I can't do this!")

prepare_sand(2)

