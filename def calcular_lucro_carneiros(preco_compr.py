def calcular_lucro_carneiros(preco_compra, preco_venda, quantidade_carneiros):
    lucro_total = (preco_venda - preco_compra) * quantidade_carneiros
    return lucro_total

preco_compra = 100 
preco_venda = 150  

quantidade_carneiros = 50

lucro_total = calcular_lucro_carneiros(preco_compra, preco_venda, quantidade_carneiros)

print(f"Quantidade de carneiros: {quantidade_carneiros}")
print(f"Lucro total da venda dos carneiros: R${lucro_total}")