class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 하늘을 훨훨 날아갑니다~'

class SwimmingMixin:
    def swim(self):
        return f'{self.name}이(가) 수영을 합니다.'


class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print('attack')
    @property
    def name(self):
        print('inside getter')
        return self.name
    @name.setter
    def name(self, new_name):
        print('inside setter')
        self.name = new_name


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados('갸라도스')
c1 = Charizard('리자몽')

print(g1.swim())
print(c1.fly())
Charizard.attack(c1)
print(g1.get_name())
g1.set_name('잉어킹')
print(g1.get_name())