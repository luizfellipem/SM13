salario_fixo = float(input("Digite o salário fixo do vendedor: "))
comissao_por_carro = float(input("Digite a comissão fixa por carro vendido: "))
num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
total_vendas = float(input("Digite o valor total das vendas em reais: "))


if num_carros_vendidos == 0:
    
    salario_final = salario_fixo
elif num_carros_vendidos > 10:
    
    salario_final = salario_fixo + (num_carros_vendidos * comissao_por_carro) + (0.05 * total_vendas) + (0.1 * total_vendas)
else:
    salario_final = salario_fixo + (num_carros_vendidos * comissao_por_carro) + (0.05 * total_vendas)


print(f"O salário final do vendedor é: R$ {salario_final:.2f}")
