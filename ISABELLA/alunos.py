alunos = {}
nomes = ["Ana" , "Carlos" , "Bianca" , "Felipe"]
for nome in nomes:
    idade = input(f"Digite a idade de {nome}: ")
    alunos[nome] =  idade
print("\nLista de alunos:")
for nome , idade in alunos.items():
    print(f"{nome}: {idade} anos")