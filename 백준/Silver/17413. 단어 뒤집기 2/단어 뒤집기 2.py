s = input()

list1 = []
a = s[0]

for i in s[1:]:
    if i == '<':
        list1.append(a)
        a = ''
    a += i
    if i == '>':
        list1.append(a)
        a = ''
        
list1.append(a)

answer = ''
for i in list1:
    if '<' in i:
        answer += i
    elif i == '':
        pass
    else:
        list2 = i.split()
        for j in list2:
            answer += j[::-1]
            answer += ' '
        answer = answer[:-1]
    
print(answer)