import streamlit as st
st.title ("Simple Calculator ")
num1 = st.number_input("Enter first number ")
num2 = st.number_input ("Enter second number")
operation = st.selectbox("Select Operation",("+","-","/","/","%"))
def calculate (num1, num2,operation):
    if operation=="+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation== "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    elif operation == "%":
        return num1%num2
    else :
        print ("Invalid Operation")

if st.button("Calculate"):
    result = calculate(num1,num2, operation)
    st.success(f"The result is : {result}")