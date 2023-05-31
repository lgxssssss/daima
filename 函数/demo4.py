def mul(x,*y):
    num=x
    for n in y:
      num*=n
    return num
print(mul(2,3))