import random
while True:
    length_password=int(input("Que tan larga quieres tu contrasena?"))
    if length_password==0:
        print("Genio! como voy a generarte una contrasena con 0 caracteres me crees mago?")
    else:
        break
    possible_characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    generated_password=""
    for i in range(length_password):
        generated_password+=random.choice(possible_characters)
print(generated_password)
