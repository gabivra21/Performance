

def inicializar_cache(tamanho_cache: int):
    cache: dict[int,int] = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache:dict[int,int], opcional=None):
    if opcional is not None:
        print("Pos Cache|Pod Memória","---->",opcional)
    else:
        print("Pos Cache|Pod Memória")
    for posicao, end_mem in cache.items():
        print(6*' ',posicao,"|  ",end_mem)

def validar_miss_hit(pos_cache:int, pos_mem:int):
    if pos_cache != pos_mem:
        print("Status: MISS")
        global misses, mem_acess
        misses += 1
        mem_acess += 1
        return True
    else:
        print("Status: HIT")
        global hits, tx_hits
        hits += 1
        tx_hits += 1
        return False

def mapeamento_direto(tamanho_cache:int, pos_memoria:list[int]):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache, "INICIAL")
    print(20*'-')
    global hits, misses, mem_acess, tx_hits
    hits, misses, mem_acess, tx_hits = 0, 0, 0, 0
    for posicao in pos_memoria:
        print("Posição desejada:",posicao)
        if posicao >= tamanho_cache:
            pos_cache = posicao % tamanho_cache
            if validar_miss_hit(cache[pos_cache], posicao):
                cache[pos_cache] = posicao
                imprimir_cache(cache)
            else:
                imprimir_cache(cache)
                continue
        else:
            if validar_miss_hit(cache[posicao], posicao):
                cache[posicao] = posicao
                imprimir_cache(cache)
            else:
                imprimir_cache(cache)
                continue
    print("RESUMO")
    print("Memórias Acessadas:", mem_acess)
    print("Total de Misses:", misses)
    print("Total de Hits:", hits)
    print("Taxa de Hits:", f"{((tx_hits*100)/len(pos_memoria)/100):.2%}")


mapeamento_direto(5, [33,3,11,5])
            
        

