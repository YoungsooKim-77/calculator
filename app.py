import streamlit as st
import re

def is_valid_number(num):
    # 숫자 유효성 검사를 위한 정규 표현식
    return re.match(r'^-?\d*\.?\d+$', num) is not None

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            st.error("Error: Division by zero!")
            return None
        return num1 / num2

st.title("Simple Calculator")

# 입력 필드
num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

# 연산 선택
operation = st.selectbox("Choose operation:", ['+', '-', '*', '/'])

if st.button("Calculate"):
    # 입력값 유효성 검사
    if not num1 or not num2:
        st.warning("Please enter both numbers.")
    elif not is_valid_number(num1) or not is_valid_number(num2):
        st.error("Please enter valid numbers.")
    else:
        num1 = float(num1)
        num2 = float(num2)
        
        # 계산 수행
        result = calculate(num1, num2, operation)
        
        if result is not None:
            st.success(f"Result: {result}")

# 사용 설명
st.markdown("---")
st.write("How to use this calculator:")
st.write("1. Enter two numbers in the input fields.")
st.write("2. Select an operation from the dropdown menu.")
st.write("3. Click the 'Calculate' button to see the result.")
st.info("Note: This calculator supports basic arithmetic operations (+, -, *, /).")