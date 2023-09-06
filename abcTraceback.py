def a():
    print('Start of a()')
    b() # b() 함수 호출

def b():
    print('Start of b()')
    c() # c() 함수 호출

def c():
    print('Start of c()')
    42 / 0 # 이 식은 0으로 나누기 에러를 발생시킴

a() # a() 함수 호출
