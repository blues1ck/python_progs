def print_field(field):
    # функция вывода в терминал игрового поля
    for i in range(len(field)):
        print(*field[i], sep = ' ')

def enter_pos(string):
    key = False
    while not key:
        try:
            m, n = map(int, input(string).split())
            key = True
        except:
            print('invalid format')
            key = False
    return m, n

def new_pos(m, n, person):
    a = 0
    b = 0
    global field
    key = False
    while not key:
        try:
            a, b = map(int, input(f'enter new position {person} ').split())
            key = True
        except:
            print('invalid format')
            key = False
    if (a > m) or (b > n) or (b<=0) or (a<=0) or (field[a][b] != '[ ]'):
        print('invalid position')
        a, b = new_pos(m, n, person)
    return a, b

m, n = enter_pos('please, enter m and n - size of map(format is: nuber_of srtings-whitespace-number_of_columns) ')
field = [['[ ]']*(n+1)]
for i in range(1, m):
    field = field + [['[ ]']*(n+1)]
field = [[f'[{i}]' for i in range(n+1)]] + field
for i in range(m+1):
    j = i
    field[i][0] =  str('[' + str(j) + ']')
print_field(field)

n_walls = int(input('how many walls will it be on the field '))
for i in range(n_walls):
    key = True
    while key:
        try:
            a, b = map(int, input('enter wall position ').split())
            if (a<=m) and (a>0) and (b<=n) and (b>0):
                key = False
        except:
            print('invalid wall position')
    field[a][b] = '[X]'
    print_field(field)

is_exit = input('Will there be an exit from the field? (y/n) ')
while True:
    if is_exit == 'y':
        break
    if is_exit == 'n':
        break
    print('invalid answer')
    is_exit = input('Will there be an exit from the field? (y/n) ')
if is_exit == 'y':
    exit_str, exit_column = new_pos(m, n, 'exit')
    field[exit_str][exit_column] = '[E]'
    print_field(field)

p_str_0, p_column_0 = new_pos(m, n, 'policeman')
field[p_str_0][p_column_0] = '[P]'
print_field(field)

t_str_0, t_column_0 = new_pos(m, n, 'theif')
field[t_str_0][t_column_0] = '[T]'
print_field(field)

def change_policman_pos(m, n):
    global field
    for i in field:
        if '[P]' in i:
            cur_string_pos = field.index(i)
            break
    cur_column_pos = field[cur_string_pos].index('[P]')
    a = 0
    b = 0
    key = False
    while not key:
        try:
            a, b = map(int, input(f'enter new position policeman ').split())
            key = True
        except:
            print('invalid format')
            key = False
    if field[a][b] == '[P/E]':
        return a, b
    elif field[a][b] == 'E' and (abs(cur_column_pos-b))<=1 and cur_string_pos(abs(cur_string_pos)-a)<=1:
        field[cur_string_pos][cur_column_pos] = '[ ]'
        field[a][b] = '[P/E]'
        return a, b
    elif (a > m) or (b > n) or (b<=0) or (a<=0) or abs(cur_column_pos - b) > 1 or abs(cur_string_pos - a) > 1 or field[a][b] == '[X]':
        print('invalid position')
        a, b = change_policman_pos(m, n)
    else:
        field[cur_string_pos][cur_column_pos] = '[ ]'
        field[a][b] = '[P]'
        return a, b
    
def is_policeman_win(field):
    key_no_theif = True
    key_no_exit = True
    for i in field:
        if '[T]' in i:
            key_no_theif = False
        if '[E]' in i or '[P/E]' in i:
            key_no_exit = False
    if key_no_exit:
        print('no exit for theif')
        return True
    if key_no_theif:
        print('policeman eated theif')
        return True
    else:
        return False

def change_theif_pos(m, n):
    global field
    for i in field:
        if '[T]' in i:
            cur_string_pos = field.index(i)
            break
    cur_column_pos = field[cur_string_pos].index('[T]')
    a = 0
    b = 0
    key = False
    while not key:
        try:
            a, b = map(int, input(f'enter new position theif ').split())
            key = True
        except:
            print('invalid format')
            key = False
    if field[a][b] == 'E' and (((abs(cur_column_pos-b))<=1 
                                and cur_string_pos(abs(cur_string_pos)-a)==0) or (abs(cur_string_pos-a)<=1 and abs(cur_column_pos-b)==0)):
        field[cur_string_pos][cur_column_pos] = '[ ]'
        field[a][b] = '[T]'
        return a, b
    if field[a][b] == '[P]':
        print('invalid move')
        change_theif_pos(m, n)
    elif not((a <= m) and (b <= n) and (b>0) and (a>0) and ((abs(cur_column_pos - b) <= 1
                                and abs(cur_string_pos - a) == 0) or (abs(cur_column_pos - b) == 0 and abs(cur_string_pos - a) <= 1)) and field[a][b]!='[X]'):
        print('invalid position')
        a, b = change_theif_pos(m, n)
    else:
        field[cur_string_pos][cur_column_pos] = '[ ]'
        field[a][b] = '[T]'
        return a, b


def is_theif_win(field):
    key_no_exit = True
    for i in field:
        if '[E]' in i:
            key_no_exit = False
    if key_no_exit:
        print('theif exited')
        return True
    else:
        return False
    
key = True
while key == True:
    print("policman's move")
    change_policman_pos(m, n)
    print_field(field)
    if is_policeman_win(field):
        key = False
        print('gameover, policeman wins')
        break
    print("theif's move")
    change_theif_pos(m, n)
    print_field(field)
    if is_theif_win(field):
        key = False
        print('gameover, theif wins')
        break
