import random



def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

print(gen_pass(8))