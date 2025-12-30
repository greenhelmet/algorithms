minsik2num = {'a': 1 , 'b': 2, 'k': 3, 'd': 4, 'e': 5, 'g': 6, 'h': 7, 
          'i': 8, 'l': 9, 'm': 10, 'n': 11, 'z': 12, 'o': 13, 'p': 14, 'r': 15,
          's': 16, 't': 17, 'u': 18, 'w': 19, 'y': 20}

num2minsik = {1: 'a', 2: 'b', 3: 'k', 4 : 'd', 5: 'e', 6: 'g', 7: 'h', 8: 'i',
              9: 'l', 10: 'm', 11: 'n', 12: 'ng', 13: 'o', 14: 'p', 15: 'r',
              16: 's', 17: 't', 18: 'u', 19: 'w', 20: 'y'}

N = int(input())
words = []
for i in range(N):
    a = input()
    words.append(a)
    
list1 = []
for i in words:
    if 'ng' in i:
        i = i.replace('ng', 'z')
    a = []
    for j in i:
        a.append(minsik2num[j])
    list1.append(a)
    
list1.sort()

answer = []
for i in list1:
    ans = ''
    for j in i:
        ans += num2minsik[j]
    answer.append(ans)
    
for i in answer:
    print(i)