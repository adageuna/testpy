data = [32,14,55,23,12,67,44]


# 30 이상인 수 출력
for x in data:
    if x>= 30:
        print(x, end=', ')
print('끝')


# 40보다 크고 50보다 작은 수 출력
for x in data:
    if x>40 and x<50 :
        print(x, end=', ')
print('끝')


# 20보다 작거나 50 이상인 수 출력
for x in data:
    if x < 20 or x >= 50 :
        print(x, end=', ')
print('끝')


# 홀수 출력
for x in data:
    if x % 2==1 :
        print(x, end=', ')
print('끝')
        

# 30 이상인 수의 개수 출력
i=0
for x in data :
    if x >= 30 :
        i=i+1
print(i)
