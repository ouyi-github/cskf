import random

import yaml

# a = yaml.safe_load(open('./addmember.yaml'))
# print(a)

yuan1 = 'abcdefghijklmnokqrstuvwxyz'
yuan2 = 'abcdefghijklmnokqrstuvwxyz0123456789'
yuan3 = '123456789'

lists = []
for i in range(100):
    a = ''
    b = ''
    c = '1311817'
    for s1 in range(10):
        a = a + yuan1[random.randint(0,25)]
    for s2 in range(8):
        b = b + yuan2[random.randint(0,35)]
    for s3 in range(4):
        c = c + yuan3[random.randint(0,8)]

    lists.append((a,b,c))

print(lists)




with open('./addmember.yaml','w') as f:
    yaml.safe_dump(data=lists,stream=f)