def calcule (num1, operator, num2):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Votre opérration est incorrect"

print (calcule(1,"+", 2))
print (calcule(2,"-", 3))
print (calcule(3,"*", 4))
print (calcule(4,"/", 5))
print (calcule(5,"%", 6))
print (calcule(6,"^", 7))