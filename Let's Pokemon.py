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
r = random.Random()
import copy
# 마을 순서 리스트
village = [('태초마을', 0), ('상록시티', 200), ('회색시티', 150), ('블루시티', 300), ('갈색시티', 100), ('보라타운',120), ('무지개시티', 150), ('연분홍시티', 100), ('노랑시티', 50), ('홍련마을', 100), ('석영고원', 50)]

def ispight() -> bool:
    '''
    내 포켓몬들 중에 싸울 수 있는 포켓몬이 하나라도 있어서 내가 싸울 수 있는 상태인지 판단하는 함수
    :return: bool
    '''
    for i in (0, len(me.mypokemon) - 1):
        if me.mypokemon[i].hp > 0:
            return True
    return False

def experience(self, target):
    '''
    self의 경험치를 올려주고, 진화가 가능한지 알려주는 함수
    :param self: 행동의 주체, 클래스 객체
    :param target: 상대, 클래스 객체
    :return:
    '''
    if self in me.mypokemon:
        try:
            self.experience += (target.lv) * 100 + r.randint(1, 50)
            if self.experience >= 1000 * (self.lv):
                print(f'!!!! {self.name}의 진화가 가능합니다.!!!!')
        except AttributeError as error:
            pass

def Lets_go_village(now):
    '''
    마을로 가는 행동을 하는 함수
    마을로 가는 중 발걸음을 옮기는 중에 2%의 확률로 몬스터와 전투
    :param now: me.now_village
    :return: none
    '''
    now_index = village.index(now)
    next_village = village[now_index + 1]
    print(f'''
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    {village[now_index][0]}에서 {next_village[0]}으로 이동합니다.
    ''')

    for i in range(next_village[1]):
        event = r.randint(1, 50)
        if event == 10:
            monster = monster_1[r.randint(0, len(monster_1)-1)]
            my_pokemon = me.mypokemon[0]
            print(f'''
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            {i}번째 발걸음을 옮기던 중,,,,,,,,,
            
            이런!! 야생의 {monster.name}가 나타났다!!!
            나와라! {my_pokemon.name}!!
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            ''')
            Lets_pight(my_pokemon, monster)

    print(f'''
    ------------------------------------
    {next_village}에 무사히 도착했습니다.
    ------------------------------------
    ''')
    Me.now_village = next_village

def In_village(me):
    now_village = me.now_village
    behave = input(f'''
        --------------------------------------------------
        무사히 {now_village}에 도착했습니다.

        마을에서 할 행동을 고르시오.
        1) 나의 포켓몬 회복시키기
        2) 포켓몬 진화시키기
        3) 마을에서 나가기
        --------------------------------------------------
        ''')
    if behave in ('나의 포켓몬 회복시키기', '1'):
        for i in range(0, len(me.mypokemon)):
            me.mypokemon[i].health
    elif behave in ('포켓몬 진화시키기', '2'):
        print('현재 보유한 포켓몬 중, 어떤 포켓몬을 진화시키시겠습니까?')
        for i in range(0, len(me.mypokemon)):
            print(f'{i+1}) {me.mypokemon[i].name}')
        pokemon_name = input('포켓몬 이름을 입력하세요.')
        evolution_pokemon = me.mypokemon[me.mypokemon.index(pokemon_name)]
        if evolution_pokemon.experience >= 1000 * (evolution_pokemon.lv):
            evolution_pokemon.lv += 1
            evolution_pokemon.health()
        elif evolution_pokemon.experience < 1000 * (evolution_pokemon.lv):
            print(f'아직 {evolution_pokemon.name}은 진화할 준비가 안 됐습니다.')
        else:
            print('값을 잘못 입력했습니다.')
    elif behave in ('마을에서 나가기', '3'):
        print('마을에서 나갑니다.')
    else:
        print('값을 잘못 입력했습니다.')

class Me: #player를 정의하는 클래스
    def __init__(self):
        self.ispokemon = False #player가 포켓몬인지 알 수 있는 속성
        self.mypokemon = [] #player가 포켓몬이 들어있는 리스트
        self.now_village = ('태초마을', 0) #player의 현재 마을을 알려주는 속성 (마을이름, 발걸음 수)

def attack(target, self, damage, skillpoint):
    '''
    self가 target을 공격하는 함수
    :param target: target(class 객체)
    :param self: class 객체
    :param damage: 공격하는 데미지
    :param skillpoint: 필요 스킬포인트
    :return:
    '''
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
        def check_target_hp_to_victory(target, self):
            '''
            상대의 hp가 없어서 내가 승리했는지 확인하는 함수
            :param target: 타겟의 클래스 객체
            :param self: 공격하는 대상의 클래스 객체
            :return:
            '''
            if target.hp <= 0:
                print(f'''
                -----------------------------------------
                {self.name}이(가) 승리하였습니다!!
                -----------------------------------------
                ''')
                experience(self, target)

            else:
                pass

        check_target_hp_to_victory(target, self)
    else:
        print(f'''
        ----------------------------------------------
        {self.name}의 스킬포인트가 부족합니다.
        {self.name}의 패배로 간주합니다.
        ''')
    self.plus_damage = 0

#스토리 중 전투가 시작되는 함수
def Lets_pight(self, target):
    keep_pight = True
    def What_kind_of_behave(self, target, pight):

        if self in me.mypokemon:
            behave = input('''
                    ---------------------------------------------------
                    취할 행동을 선택하세요.
                    1) 공격하기
                    2) 도망가기
                    3) 포획하기
                    ---------------------------------------------------
                    ''')
        else:
            behave = str(random.choices(range(1,3), weights=[49,1])[0])


        if behave in ('공격하기', '1'):
            self.attack(target)
            return True

        elif behave in ('도망가기', '2'):
            target_hp_percentage = (target.original_hp / target.hp) / 5
            percentage = random.choices(range(1, 11), weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, target_hp_percentage])
            if percentage == 10:
                target.health()
                print(f'''
                -----------------------------------------
                {self.name}이(가) {target.name}으로부터 성공적으로 도망쳤습니다.
                -----------------------------------------
                ''')
                return False
            else:
                print(f'''
                -----------------------------------------------
               {self.name}이(가) {target.name}으로부터 도망치는 것에 실패했습니다.
                {target.name}의 hp가 적을수록 도망치는 것이 수월합니다.
                -----------------------------------------------
                ''')
                return True
        elif behave in ('포획하기', '3'):
            target_hp_percentage = (target.original_hp / target.hp)*10
            percentage = random.choices(range(1, 11), weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, target_hp_percentage])[0]
            if percentage == 10:
                my_pokemon = copy.deepcopy(target)
                me.mypokemon += [my_pokemon]
                print(f'''
                -----------------------------------------------
                우와! 신난다! {target.name}을 잡았다!
                -----------------------------------------------
                ''')
                return False
            else:
                print(f'''
                -----------------------------------------------
                {percentage}
                {target.name}을 포획하는 것에 실패했습니다.
                {target.name}의 hp가 적을수록 포획하는 것이 수월합니다.
                -----------------------------------------------
                ''')
                return True

    while True:
        if ispight() and target.hp > 0 and keep_pight:
            keep_pight = What_kind_of_behave(self, target, keep_pight)
            if target.hp > 0 and keep_pight:
                keep_pight = What_kind_of_behave(target, self, keep_pight)
        else:
            break

#포켓몬을 정의하는 클래스
class Pokemon:
    def __init__(self):
        self.ispokemon = True

    def health(self):
        self.hp = self.original_hp
        self.skill_point = self.original_skill_point

#Normal 타입을 정의하는 클래스
class Normal(Pokemon):
    def __init__(self):
        self.type = 'normal'
        self.plus_damage = 0
    def attack(self, target):

        # 무슨 스킬을 사용할지 어택에 담음
        if self in me.mypokemon:
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
            attack(target, self, (10+self.plus_damage), 5)

        elif attackkind in ('마구할퀴기', '2'):
            attack(target, self, 15+self.plus_damage, 6)

        elif attackkind in ('몸통박치기', '3'):
            attack(target, self, 15+self.plus_damage, 6)

        elif attackkind in ('비축하기', '4'):
            self.plus_damage = r.randint(5, 50)
            print(f'''
            -------------------------------------
            {self.name}이(가) 비축을 완료했습니다.
            -------------------------------------''')
        else:
            print('값을 잘못 입력했습니다.')


# Normal 타입을 정의하는 클래스
class Electric(Pokemon):
    def __init__(self):
        self.type = 'electric'
        self.plus_damage = 0

    def attack(self, target):

        # 무슨 스킬을 사용할지 어택에 담음
        if self in me.mypokemon:
            attackkind = input(''' 

            -----------------------------------------
            공격하기!
            1) 100만 볼트 : 데미지: 20 스킬 포인트: 15
            2) 방전 : 데미지 15 스킬 포인트: 8
            3) 몸통박치기 : 데미지 6 스킬 포인트: 2
            4) 비축하기 : 다음 번 공격에 랜덤하게 데미지를 추가한다. 스킬 포인트: 10

            스킬 이름 또는 번호를 입력하세요: ''')
        else:
            attackkind = str(r.randint(1, 4))

        # attack에 담긴대로 스킬 적용
        if attackkind in ('100만 볼트', '1'):
            attack(target, self, (20+5*self.lv + self.plus_damage), 15)

        elif attackkind in ('방전', '2'):
            attack(target, self, 15+ 3*self.lv + self.plus_damage, 8)

        elif attackkind in ('몸통박치기', '3'):
            attack(target, self, 15 + 2*self.lv + self.plus_damage, 6)

        elif attackkind in ('비축하기', '4'):
            self.plus_damage = r.randint(5, 50 + 10*self.lv)
            print(f'''
            -------------------------------------
            {self.name}이(가) 비축을 완료했습니다.
            -------------------------------------''')
        else:
            print('값을 잘못 입력했습니다.')


#피카츄 클래스
class Pikachu(Electric):

    def __init__(self):
        super().__init__()
        self.name = 'pikachu'
        self.lv = 3
        self.original_hp = 150*self.lv
        self.hp = 450
        self.original_skill_point = 50*self.lv
        self.skill_point = 150
        self.experience = 0

#몬스터 중 마우스 클래스
# 나중에 몬스터와 플레이어로 클래스를 나누면, 함수들이 더 간단해질듯
class Mouse(Normal):
    def __init__(self):
        super().__init__()
        self.name = 'mouse'
        self.lv = 1
        self.original_hp = 150*self.lv
        self.hp = 150
        self.original_skill_point = 100*self.lv
        self.skill_point = 100

pikachu = Pikachu() #피카츄 생성
mouse = Mouse() #몬스터 마우스 생성
monster_1 = [mouse] #몬스터 리스트에 마우스 넣음
me =Me() #player 생성
me.mypokemon.append(pikachu) #player의 포켓몬 리스트에 피카츄 넣음

#----------------------------------------------------------------------------
#실제 개임 실행부
while ispight(): # 내 포켓몬이 싸움을 할 수 있는 동안에만 게임이 실행됨.
    behave_kind = input(print('''
    --------------------------------------------------
    어떤 행동을 할지 고르세요.
    1) 야생 탐험
    2) 다음 마을로 이동
    3) 챔피언 리그 도전하기
    4) 게임 종료
    --------------------------------------------------
    '''))
    if behave_kind in ('야생 탐험', '1'):
        monster = monster_1[r.randint(0, len(monster_1)-1)]
        print(f'''
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        앗! 야생의 {monster.name}이(가) 나왔다.
        
        나와라!! {me.mypokemon[0].name}!!
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1
            ''')
        Lets_pight(me.mypokemon[0], monster)
        monster.health()

    elif behave_kind in ('다음 마을로 이동', '2'):
        Lets_go_village(me.now_village)
        In_village(me)
    elif behave_kind in ('챔피언 리그 도전하기', '3'):
        pass
    elif behave_kind in ('게임 종료', '4'):
        print('게임을 종료합니다.')
        break
    else:
        print('''
        ----------------------------------------------
        잘못된 값을 입력했습니다.
        ----------------------------------------------''')

# 도망가기 점검
# 몬스터가 도망갔을 때 점검
# 마을에서 하는 것들 추가
# 코드 효율 점검