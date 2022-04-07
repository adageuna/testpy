# data라는 변수에 자신의 개인이메일을 집어 넣는다.
data='daeun8202@naver.com'

# data라는 변수 안에서 @부터 .com 전까지의 값을 구한다.
atpos=data.find('@')
sppos=data.find('.',atpos)
host=data[atpos+1:sppos]

# 그 값을 대문자로 바꾼 후 출력한다
s=host.upper()
print(s)

# 대문자로 바뀐 문자열의 마지막 문자를 출력하고 그 문자의 아스키코드 값을 구하여라
last=(s[-1])
print(last)
print(ord(last))
