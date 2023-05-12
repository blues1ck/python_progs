class CardDeck:
    def __init__(self):
        self.suits = ['Пик', 'Треф', 'Бубен', 'Червей']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.index = 0
    
import random

card = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
cards = [i+' бубен' for i in card]
cards = cards + [i+' червей' for i in card]
cards = cards + [i+' треф' for i in card]
cards = cards + [i+ ' пик' for i in card]

players = int(input('how many players? '))
names = list(input('enter names ').split())

def score(cards):
    numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = 0
    t = 11
    for i in cards:
        if i[0] in numb:
            res += int(i[0:1])
        else:
            if i[0] == 'В':
                res += 2
            elif i[0] == 'Д':
                 res += 3
            elif i[0] == 'К':
                res += 4
            else:
                res += 11
    return res                    

print(names)

pl_cards = [[]*players]
pl_score = [0]*players
for i in range(players):
    print(names[i] + 'your turn')
    for _ in range(2):
        num = random.randint(0, 35)
        while cards[num] == 'X':
            num = random.randint(0, 35)
        
        pl_cards[i].append(cards[num])
        cards[num] = 'X'
    
    print('Your cards: ', *pl_cards[i])
    pl_score[i] = score(pl_cards[i])
    if pl_score[i] == 21:
        print('ОЧКО!!!')
        continue

    s = input('Do you want one more card?(y/n) ')
    while s!='y' and s!='n':
        s = input('Do you want one more card?(y/n) ')
    while s == 'y' and pl_score[i] <= 21:
        num = random.randint(0, 35)
        while cards[num] == 'X':
            num = random.randint(0, 35)
        
        pl_cards[i].append(cards[num])
        cards[num] = 'X'
        pl_score[i] = score(pl_cards[i])

        print(*pl_cards[i])

        if pl_score[i] > 21:
            print('перебор')
        elif pl_score[i] == 21:
            print('ОЧКО!!!')
        else:
            s = input('Do you want one more card?(y/n) ')
            while s!='y' and s!='n':
                s = input('Do you want one more card?(y/n) ')
    print(pl_score[i])
        

