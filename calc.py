print("პროგრამა შექმნილა Kanti-ის მიერ, ისიამოვნეთ.")
x = "symbols"
x = float(input("შეიტანეთ x: "))


oper = input("აირჩიეთ ოპერაცია: +, -, /, * ...> ")


y = float(input("აირჩიეთ y: "))
    


if oper == "+":
    print(x + y)
elif oper == "-":
    print(x - y)
elif oper == "/":
    print(x / y)
 elif oper == "*":
    print(x * y)
else:
    print("შეცდომა")
