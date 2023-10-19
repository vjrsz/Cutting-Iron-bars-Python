from cib import cib
from cib_bottomup import cib_bottomup
from cib_topdown import cib_topdown

if __name__ == '__main__':
    bars = [10, 15, 20, 25, 30, 35]

    print("Cib : ")
    print(cib(2, bars))
    print(cib(3, bars))
    print(cib(5, bars))
    print()

    print("Cib TopDown: ")
    print(cib_topdown(2, bars))
    print(cib_topdown(3, bars))
    print(cib_topdown(5, bars))
    print()

    print("Cib BottomUp: ")
    print(cib_bottomup(2, bars))
    print(cib_bottomup(3, bars))
    print(cib_bottomup(5, bars))
    print()



