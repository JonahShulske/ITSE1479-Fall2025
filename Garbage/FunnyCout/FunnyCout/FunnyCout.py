class Cout:
    def __lshift__(self, other):
        print(other, end="")
        return self

    def __rrshift__(self, other):
        print(other, end="")
        return self


class Endl:
    def __rshift__(self, other):
        return other + "\n"

    def __str__(self):
        return "\n"

class Ref:
    def __init__(self):
        self.value = None

class Cin:
    def __rshift__(self, other):
        other.value = input()
        return self

cout = Cout()
endl = Endl()
cin = Cin()

name = Ref()
cin >> name
cout << name.value << endl
