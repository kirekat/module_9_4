first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = (len(i) - len(j) for i, j in zp if len(i) != len(j))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range (len(first)))
print(list(second_result))

