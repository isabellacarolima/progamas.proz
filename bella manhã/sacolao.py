frutas = ("maçã" , "banana" , "cereja")
print("Minha tupla de frutas:", frutas)
print("Priemira fruta:", frutas[0])
print("Segunda fruta:", frutas[1])
print("Terceira fruta:", frutas[2])
print("Número de frutas na tupla:", len(frutas))
print("Listando todas as frutas na tupla:")
for fruta in frutas:
    print(fruta)
if "banana" in frutas:
    print("Banana está na tupla!")
unica_fruta = ("melancia",)
print("Tupla de um único elemento:", unica_fruta)