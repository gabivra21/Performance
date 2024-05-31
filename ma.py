from collections import deque

def inicializar_cache_associativo(tamanho_cache, tamanho_conjunto):
    num_conjuntos = tamanho_cache // tamanho_conjunto
    cache = {i: deque(maxlen=tamanho_conjunto) for i in range(num_conjuntos)}
    return cache

def imprimir_cache_associativo(cache):
    print("Estado atual da cache (Set Associative):")
    for conjunto, blocos in cache.items():
        print(f"Conjunto {conjunto}: {list(blocos)}")

def mapeamento_associativo_lru(tamanho_cache, tamanho_conjunto, pos_memoria):
    cache = inicializar_cache_associativo(tamanho_cache, tamanho_conjunto)
    num_conjuntos = tamanho_cache // tamanho_conjunto
    
    hits = 0
    misses = 0

    for posicao in pos_memoria:
        conjunto = (posicao // tamanho_conjunto) % num_conjuntos
        blocos = cache[conjunto]
        
        if posicao in blocos:
            hits += 1
            blocos.remove(posicao)
            blocos.append(posicao)
            status = "HIT"
        else:
            misses += 1
            blocos.append(posicao)
            status = "MISS"
        
        print(f"Posição de memória {posicao} -> Conjunto {conjunto} -> {status}")
        imprimir_cache_associativo(cache)

    total_acessos = len(pos_memoria)
    taxa_hits = hits / total_acessos * 100

    print("\nResumo")
    print(f"Total de acessos: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de hits: {taxa_hits:.2f}%")

# Função principal para interagir com o usuário
def main():
    tamanho_cache = int(input("Digite o tamanho da cache: "))
    tamanho_conjunto = int(input("Digite o tamanho do conjunto (blocos por conjunto): "))
    pos_memoria = list(map(int, input("Digite as posições de memória a serem acessadas (separadas por espaço): ").split()))
    
    mapeamento_associativo_lru(tamanho_cache, tamanho_conjunto, pos_memoria)

# Executar a função principal
if __name__ == "__main__":
    main()
