import random 
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Introduzca la longitud de  el pase"))

contraseña = ""

for  i in range(pass_length):
    contraseña += random.choice(caracteres)

print(contraseña)    
