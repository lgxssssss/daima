def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))


def per(name,age,**ss):
    print('name,',name,'age:',age,'other:',ss)
print(per('lgx',23,higth='1.77',weight='62'))

LGX={'higth':'1.77','weight':'62'}
print(per('lgx',23,**LGX))