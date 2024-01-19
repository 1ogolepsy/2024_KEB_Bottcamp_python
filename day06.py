class Animal:
    def says(self):
        return 'I speak!'

class horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'hee-hae'

class Mule(Donkey, horse):
    def says(self):
        return '노새 노새 젊어서 노새'
class hinny(horse, Donkey):
    def says(self):
        return '버새 버새'

mi = Donkey()
h1 = hinny()
print(Mule.mro())
print(mi.says())