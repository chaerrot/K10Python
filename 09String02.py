'''
서식문자로 문자열, 정수, 실수 표현
    형식]
        '문자열' % 변수 및 문자열
        서식 문자는 Java와 거의 동일하고 자리 수 지정 시 %10d, %5.3f와 같이 사용한다.
'''
# 문자열 사용
str = '내 이름은 %s 입니다.' % '칸'
print("str1= ", str)

# 리스트 사용
names = ['유미', '간우', '쟝비']
for n in names: # for문에서 리스트의 크기만큼 반복하므로
    print('이름: %s' % n) # 하나의 원소가 매칭된다.
    
# 정수: %d
money = 10000
str = '마우스 가격은 %d원입니다.' % money
print(str)

# 실수: %f
pi = 3.141592
print('원주율은 %f'  % pi)

# 문자열: %s
str = '이름: %s. 나이: %d' % ('홍길동', 99) # 2개 이상의 변수는 콤마로 구분
print(str)

# 여러 개의 변수를 초기화 시 좌측항과 우측항으로 나눠서 기술한다.
phone, age, height = "010-1234-5678", 28, 181.5
str2 = '전화번호: %s, 나이: %d, 키: %f' % (phone, age, height)
print("str2= ", str2)

