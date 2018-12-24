import sys
a = 'ABC'
b = a
a = 'XYZ'
print(10 / 3)
print(10 // 3)
c = ord('你')
print(c)
print(chr(66))
x = b'abc'
print(x)
print('测试'.encode('utf-8'))
print('%20d-%02d' % (3, 1))
print('hello, %s, you have $%d' % ('neo', 1000))
classList = ['aaa', 'bbb', 'ccc']
print(classList)
print(len(classList))
print(classList[0])
print(classList[-1])
classList.append('xxx')
print(classList)
classList.insert(1, 'yyy')
print(classList)
classList.pop(2)
print(classList)
t = (1,)
print(t)
t1 = (1)
print(t1)
aaa = 31
if aaa < 10:
    print('aaa')
elif aaa > 10:
    print('bbb')
else :
    print('ccc')
s = input('birth :')
birth = int(s)
if birth < 1000:
    print('dui')
else:
    print('cuo')
for classs in classList:
    print(classs)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n -2
print(sum)
d = {'sun': 100, 'qu': 200}
print(d['sun'])
print(classList)
print(classList[1 : 3])
print(classList[-2 :])
print([m + n for m in 'ABC' for n in 'XYZ'])
g =  (x * x for x in range(10))
for n in g:
    print(n)
argv = sys.argv
if len(argv) == 1:
    print('hello, world')
elif len(argv) == 2:
    print('hello, %s!' % argv[1])
else:
    print('too many')