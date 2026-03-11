#passo 1 - logica do pomodoro, definir quantidade de tempo, e o aplicativo define um tempo de descanso
#passo 2 - após um ciclo de 4 tempos ele da um descanso maior 
import time 

#BACKEND 
definirTempo = int(input("Defina o tempo: "))
ciclo = 4

#Função de contagem regressiva
def contagem_regressiva(definirTempo, ciclo):
    while ciclo > 0:

        ContadorTempo = definirTempo
        tempoDescanso = int(definirTempo /5)
        descansoLongo = int(definirTempo /2)
        print("Ciclo Nº:", ciclo)
        while ContadorTempo >= 0:        
            print(ContadorTempo)
            ContadorTempo -= 1 
            time.sleep(1)

        time.sleep(0.5)
        print("Hora do descanso")
        time.sleep(0.5)
        
        descanso(ciclo, descansoLongo, tempoDescanso)
        ciclo = contador_ciclo(ciclo)

def descanso(ciclo, descansoLongo, tempoDescanso):
    if ciclo == 1:
        while descansoLongo >=0 :
            print(descansoLongo)
            descansoLongo-= 1
            time.sleep(1)
        
        print("Fim dos estudos")

    else:
        while tempoDescanso >= 0:
            print(tempoDescanso)
            tempoDescanso -= 1
            time.sleep(1)

            
        time.sleep(0.5)
        print("Fim do descanso")
        time.sleep(0.5)

def contador_ciclo(ciclo):
    return ciclo -1 

contagem_regressiva(definirTempo, ciclo)
   
