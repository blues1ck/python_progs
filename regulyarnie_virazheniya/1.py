import re

'''
n = int(input('how many sentances?'))

sentences = []
for i in range(n):
    sentence = input(f'{i+1} sentence: ')
    sentences.append(sentence)
'''
# тестовый ввод из задания почему то не учел, что "слово" и "с" начинаются с одной буквы
sentences = [
             "Здесь все слова начинаются с разных букв.",
             "А в этом предложении есть слова, которые всё-таки начинаются на одну и ту же букву.",
             "А здесь совсем интересно: символ «а» однобуквенный."]

for sentence in sentences:
    words = re.findall(r'\b\w', sentence, flags=re.I) # находим первую букву каждого слова
    if len(words) == len(set(words)): # если все буквы уникальны
        print("Метод Довлатова соблюдён")
    else:
        print("Вы расстроили Сергея Донатовича")