def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def sandwich(s = ''):
    if s == 'veg' :
        bread()
        for i in range(2):
            lettuce()
            tomato()
        bread()
    else :
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

def prepare_sand(x,s = ''):
    if type(x) == int :
        for i in range(x) :
            sandwich(s)
            print()
    else :
        print("I can't do this!")

prepare_sand(2,'veg')