#words = 'When God Close One Door, He Opens Another.'의 
#문자열 속 대문자는 몇 번째 인덱스에 있는지 모두 구하시오.

words='When God Close One Door, He Opens Another.'
for i in words :
    if i >= 'A' and i <= 'Z' :
        print(words.index(i), end=' ')
