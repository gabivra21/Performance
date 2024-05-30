

def inicializar_cache(tamanho_cache: int):
    cache: dict[int,int] = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache:dict[int,int]):
    for posicao, end_mem in cache.items():
        print("|",posicao,"|",end_mem,"|")
        print(10*"-")

def mapeamento_direto(tamanho_cache:int, pos_memoria:list[int]):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)
    print(20*'*')
    for posicao in pos_memoria:
        if posicao > tamanho_cache:
            pos_cache = posicao % tamanho_cache
            cache[pos_cache] = posicao
        else:
            cache[posicao] = posicao
    imprimir_cache(cache)

mapeamento_direto(10, [3,15,7,33,126,1])
            
        

