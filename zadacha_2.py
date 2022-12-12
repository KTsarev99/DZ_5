# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно 
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random

def dice(): # 
    a="player 1 turns first"
    b="player 2 turns first"
    turn = random.randint(1,2)
    if turn == 1:
        return a
    else:
        return b

player1=0
player2=0

def choice1(): # сколько берёт игрок 1 
    for i in range(1):
        player1= int(input("первый игрок введите число :"))
        print(player1)
        if player1 > 28:
            player1=int(input("число не должно быть больше 28, введите правильное число :"))
        
    return player1

def choice2():  # сколько берёт игрок 2
    player2 = int(input("второй игрок введите число :"))
    print(player2)
    if player2 > 28:
        player2=int(input("число не должно быть больше 28,введите правильное число :"))
    return player2

sum = 100

hhh = dice()
print(hhh)

print(f'всего осталось :{sum}')
while sum>=0:
    if hhh == "player 1 turns first":  
        sum= sum -choice1()
        print(f'всего осталось :{sum}')
        if sum <= 0:
            print('первый игрок победил')
            break
    
    
        sum-=choice2()
        print(f'всего осталось :{sum}')
        if sum <= 0:
            print('второй игрок победил')
            break
    else:
        sum-=choice2()
        print(f'всего осталось :{sum}')
        if sum <= 0:
            print('второй игрок победил')
            break
        sum= sum -choice1()
        print(f'всего осталось :{sum}')
        if sum <= 0:
            print('первый игрок победил')
            break   
