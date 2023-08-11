user_input= float(input("Enter a number: "))
if 0 <= user_input <= 10:
    print("Low Range")
elif 11 <= user_input <= 50:
    print("Medium Range")
elif 51 <= user_input <= 100:
    print("High Range")
else:
    print("Out of Range")

