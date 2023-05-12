'''with open("/home/ilya/Рабочий стол/python_progs/control'naya2/text.txt", "r") as file:
    # путь к файлу
    lines = file.readlines()'''

s = open("text.txt", 'r')
lines = s.readlines()
s.close()

new_lines = []
for line in lines:
    words = line.split()
    new_words = []
    for word in words:
        if len(word) >= 2:
            new_word = word[1] + word[0] + word[2:]
        else:
            new_word = word
        new_words.append(new_word)
    new_line = " ".join(new_words) + "\n"
    new_lines.append(new_line)

res = open('result.txt', 'w')
res.writelines(new_lines)
res.close()