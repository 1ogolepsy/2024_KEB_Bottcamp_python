
class Poketmon:
    def __init__(self, name):
        self.name =name
        print(f'{name} 포켓몬스터 생성')

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')


pikachu = Poketmon('피카츄')
squirtle = Poketmon('꼬부기')
charizard = Poketmon('리자몽')
charizard.attack(squirtle)
