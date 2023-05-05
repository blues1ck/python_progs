'''
Реализуйте итератор колоды карт (52 штуки) CardDeck. Каждая карта представлена в виде строки типа «2 Пик».
При вызове функции next() будет представлена следующая карта. По окончании перебора всех элементов возникнет ошибка StopIteration.

'''
class CardDeck:
    def __init__(self):
        self.suits = ['Пик', 'Треф', 'Бубен', 'Червей']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.suits) * len(self.ranks):
            raise StopIteration
        suit = self.suits[self.index // len(self.ranks)]
        rank = self.ranks[self.index % len(self.ranks)]
        self.index += 1
        return f'{rank} {suit}'
    
deck = CardDeck()
for card in deck:
    print(card)
print(next(deck))  

