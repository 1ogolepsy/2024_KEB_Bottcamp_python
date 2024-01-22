class FlyingBehavior:
    def fly(self):
        return f'하늘을 훨훨 날아갑니다~'

class SwimmingBegavior:
    def swim(self):
        return f'수영을 합니다.'

class NoFly(FlyingBehavior):
    def fly(self):
        return f'하늘을 날 수 없습니다.'

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f'날개로 하늘을 훨훨 날아갑니다.'

class JetPack(FlyingBehavior):
    def fly(self):
        return  f'로켓추진기로 하늘을 날아갑니다.'

class Pokemon:
    def __init__(self, name, hp, fly_behavior):
        self.__name = name
        self.hp =hp
        self.fly = fly_behavior #aggregation (has-a)
    def attack(self):
        print('attack')
    @property
    def name(self):
        print('inside getter')
        return self.__name
    @name.setter
    def name(self, new_name):
        print('inside setter')
        self.__name = new_name

    def __str__(self):
        return self.__name + '입니다.'
    def __add__(self, other):
        return print(f'두 포켓몬스터 체력의 합은{self.hp + " + " + other.hp}입니다.')

    def set_fly_behavior(self, fly):
        self.fly = fly

class Charizard(Pokemon):
    pass

class Pikachu(Pokemon):
    pass

F = FlyWithWings()

no_F = NoFly()
g1 = Pikachu('피카츄', 100, no_F)
c1 = Charizard('리자몽', 120, F)

print(c1.fly.fly())
print(g1.fly.fly())
g1.set_fly_behavior(JetPack())
print(g1.fly.fly())