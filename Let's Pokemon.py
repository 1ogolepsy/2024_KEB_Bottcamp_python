# Pokemon class
#     type class
#     여기에 각 속성마다 어떻게 기술이 있는지, 해당 기술 mp,damage(상대속성마다(for, if구문))
#
#         각 포켓몬 class
#         이름, hp, mp, lv
#
# 실행순서
# 플레이어 이름 받기 (플레이어 class만들고 이름이랑 소지 골드, 소지 포켓몬 속성 만들기)
# 초기 포켓몬 선택하기(피카츄, 꼬부기, 등), 이 때(플레이어가 가지고 있는 포켓몬 리스트도 만들기)
#
# 탐험종류 선택(for구문으로 각 탐험이 끝나면 계속 실행)
# 야생 탐험, 챔피언 리그 도전, 다음 마을 탐험, 게임 종료하기
#     야생 탐험
#     > 야생 포켓몬이 랜덤하게 나옴
#         전투, 도망, 포획, 포켓몬 체인지, 회복 for구문으로 돌리기
#         for구문 마지막에 야생 포켓몬은 hp, mp 등 회복
#     챔피언 리그 도전
#     > 챔피언이 엄청 강한 포켓몬 가지고 있기
#     다음 마을 탐험
#     > 마을 리스트만들고 다음 순번으로 갈 때 발걸음 수도 리스트로 만들어서 if구문으로 현재 마을을 클리어하면 마을을 다음으로 넘기기
#         for구문으로 발걸음 걸어가다가 중간에 랜덤함수로 포켓몬 대결
#         마을 도착하면 포켓몬 전체 회복, 상점 만들기
#     게임 종료
#     > 게임 종료

import random
r=random.Random()
def attack(target, self, damage, skillpoint):
    if self.skill_point >= skillpoint:
        target.hp -= damage
        self.skill_point -= skillpoint
        print(f'''
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        쿠궁 {self.name}이(가) 공격에 성공했습니다.
        총 데미지는 {damage}입니다.
        {target.name}의 HP는 {target.hp}입니다.
        현재 {self.name}의 스킬포인트는 {self.skill_point}남았습니다.
        ''')
    else:
        print(f'''
        ----------------------------------------------
        {self.name}의 스킬포인트가 부족합니다.
        {self.name}의 패배로 간주합니다.
        ''')


def check_target_hp_to_victory(target, self):
    if target.hp <= 0:
        print(f'''
        -----------------------------------------
        {self.name}이(가) 승리하였습니다!!
        -----------------------------------------
        ''')
    else:
        pass

#스토리 중 전투가 시작되는 함수
def Lets_pight(My_pokemon, target):
    while My_pokemon.hp >= 0 and target.hp >= 0:
        My_pokemon.attack(target)
        target.attack(My_pokemon)
My_Pokemon = []
class Pokemon:
    def __init__(self):
        self.ispokemon = True

class Normal(Pokemon):
    def __init__(self):
        self.type = 'normal'
    def attack(self, target):
        random_damege = 0

        # 무슨 스킬을 사용할지 어택에 담음
        if self in My_Pokemon:
            attackkind = input(''' 
    
            -----------------------------------------
            공격하기!
            1) 마구찌르기 : 데미지: 10 스킬 포인트: 5
            2) 마구할퀴기 : 데미지 15 스킬 포인트: 6
            3) 몸통박치기 : 데미지 6 스킬 포인트: 2
            4) 비축하기 : 다음 번 공격에 랜덤하게 데미지를 추가한다. 스킬 포인트: 10
    
            스킬 이름 또는 번호를 입력하세요: ''')
        else:
            attackkind = str(r.randint(1, 4))

        #attack에 담긴대로 스킬 적용
        if attackkind in ('마구찌르기', '1'):
            attack(target, self, 10+random_damege, 5)
            check_target_hp_to_victory(target, self)
            random_damege = 0

        elif attackkind in ('마구할퀴기', '2'):
            attack(target, self, 15+random_damege, 6)
            check_target_hp_to_victory(target, self)
            random_damege = 0

        elif attackkind in ('몸통박치기', '3'):
            attack(target, self, 15+random_damege, 6)
            check_target_hp_to_victory(target, self)
            random_damege = 0

        elif attackkind in ('비축하기', '4'):
            random_damege = r.randint(5, 50)
            print(f'''
            -------------------------------------
            {self.name}이(가) 비축을 완료했습니다.
            -------------------------------------''')
        else:
            print('값을 잘못 입력했습니다.')

class Pikachu(Normal):
    def __init__(self):
        self.name = 'pikachu'
        self.hp = 300
        self.skill_point = 150

class Mouse(Normal):
    def __init__(self):
        self.name = 'mouse'
        self.hp = 150
        self.skill_point = 100

pikachu = Pikachu()
My_Pokemon.append(pikachu)
mouse = Mouse()

Lets_pight(pikachu, mouse)