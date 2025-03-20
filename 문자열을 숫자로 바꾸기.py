# 문자열을 숫자로 바꾸기

output_a=int("52")
output_b=float("65.23")

print(type(output_a), output_a)
print(type(output_b), output_b)

# 숫자 연산 프로그램

input_a=float(input("첫번째 숫자>"))
input_b=float(input("두번째 숫자>"))

print("덧셈의 결과 : ", input_a+input_b)
print("뺄셈의 결과 : ", input_a-input_b)
print("나눗셈의 결과 : ", input_a/input_b)
print("나눗셈의 몫과 나머지 : ", input_a//input_b, input_a%input_b)
print("곱셈의 결과 : ", input_a*input_b)

# 문자열로의 변환

abc=str(52)
efg=str(65.15)

print(type(abc), abc)
print(type(efg), efg)