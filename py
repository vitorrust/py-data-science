

Exercício 01: Análise de notas
notas = [4, 6, 7, 8, 5, 9, 6, 8, 7, 3, 5, 6, 8, 9, 4, 7, 6, 8, 9, 5]

print("Notas iniciais:", notas[:12])
print("Notas finais:", notas[-6:])
print("Total de notas:", len(notas))

# Exercício 02: Análise de filmes

filmes = {
    31: {"nome": "Filme A", "nota": 4},
    32: {"nome": "Filme B", "nota": 5},
    33: {"nome": "Filme C", "nota": 3},
}

# Verificando se o filme com ID=32 é considerado bom
filme_id = 32
if filme_id in filmes and filmes[filme_id]["nota"] > 3:
    print(f"O filme '{filmes[filme_id]['nome']}' é considerado bom.")
else:
    print("Não foi possível encontrar informações sobre este filme.")
