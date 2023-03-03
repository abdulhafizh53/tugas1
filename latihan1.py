#for i in range(1, 101):
    #print(i)


'''for i in range(1, 101):
  if(i%2 == 0):
    continue
  else:
    print(i)'''

def is_odd(num):
    return num % 2 == 1

for i in range(1, 101):
    if is_odd(i):
        print(i)