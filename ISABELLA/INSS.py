salario = float(input("Digite o valor do seu salário: R$ "))
if salario <= 1692.72:
    recolhimento = salario * salario * 0.08
elif salario > 1692.72 or salario <= 2822.90:
    recolhimento = salario * 0.09
elif salario > 2822.90 or salario <= 5645.90:
    recolhimento = salario * 0.11
total = salario - recolhimento
print(f"O valor recolhido do seu salário de vai ser de : R${recolhimento:.2f}")
print(f"É você receberá: R${total:.2f}")