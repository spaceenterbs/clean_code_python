def a():
    print("Start of a()")
    b()  # b() 함수 호출


def b():
    print("Start of b()")
    c()  # c() 함수 호출


def c():
    print("Start of c()")
    42 / 0  # 이 식은 0으로 나누기 에러를 발생시킴


a()  # a() 함수 호출

# Start of a()
# Start of b()
# Start of c()
# Traceback (most recent call last):
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\abcTraceback.py", line 13, in <module>
#     a() # a() 함수 호출
#     ^^^
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\abcTraceback.py", line 3, in a
#     b() # b() 함수 호출
#     ^^^
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\abcTraceback.py", line 7, in b
#     c() # c() 함수 호출
#     ^^^
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\abcTraceback.py", line 11, in c
#     42 / 0 # 이 식은 0으로 나누기 에러를 발생시킴
#     ~~~^~~
# ZeroDivisionError: division by zero
