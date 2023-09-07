def spam(number1, number2):
    return number1 / (number2 - 42)


spam(101, 42)


""" 단락 내부에 역슬래시가 들어가면 단락 주석이 안됨 """
# Traceback (most recent call last):
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\zeroDivideTraceback.py", line 5, in <module>
#     spam(101, 42)
#   File "C:\Users\bangm\OneDrive\바탕 화면\clean_code_python\zeroDivideTraceback.py", line 2, in spam
#     return number1 / (number2 - 42)
#            ~~~~~~~~^~~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero
