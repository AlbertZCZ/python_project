import base64

dict1 = {}
print(type(dict1))

dict2 = {'x':1,'y':'2'}
print(dict2)
dict2[3] = 'z'
print(dict2)


for i in range(10):
    dict1[i] = i

print('dict1......',dict1)

alist = [i * i for i in range(1,11) if i % 2 == 0]
print('alist:'+ str(alist))

def safe_base64_decode(s):
    l = len(s)
    n = l % 4
    while n > 0:
        s = s + '='
        n -= 1
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
