import time

def contagem_regressiva(tempo):
    contagem = []
    
    while tempo > 0:
        contagem.append(tempo)
        time.sleep(0.5)
        tempo -= 1
    
    print(", ".join(map(str, contagem)))
    
tempo_inicial = 10
contagem_regressiva(tempo_inicial)