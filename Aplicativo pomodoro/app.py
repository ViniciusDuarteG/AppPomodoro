import tkinter as tk 
#from main import contagem_regressiva, contador_ciclo, descanso

#INTERFACE
janela = tk.Tk()
janela.title("App de estudos")
janela.geometry("300x300")

time_set = 0
time_count = 0
time_rest = 0

titleLabel = tk.Label(janela,text="Pomodoro")
titleLabel.pack()

SetTimeLabel = tk.Label(janela,text="Informe o tempo desejado.")
SetTimeLabel.pack()

SetTimeInput = tk.Entry(janela)
SetTimeInput.pack()

def pegar_tempo():
    global time_set, time_count, time_rest
    time_set = int(SetTimeInput.get())
    time_count = time_set *60
    time_rest = time_count // 4

    minutes = time_count // 60
    seconds = time_count % 60
    
    timeLabel.config(text=f"{minutes:02}:{seconds:02}")
    
buttonTakeTime = tk.Button(janela, text="Ok", command=pegar_tempo)
buttonTakeTime.pack()

timeLabel = tk.Label(janela, text="00:00", font=("Arial", 40))
timeLabel.pack() 

cicloLabel = tk.Label(janela, text="Ciclo Nº ")
cicloLabel.pack()
NcicloLabel = tk.Label(janela, text="1")
NcicloLabel.pack()

ciclo = 1
time_id = None

def iniciar():
    global time_count, ciclo, time_id 
    
    if time_count > 0:
        time_count -=1
    
        minutes = time_count // 60
        seconds = time_count % 60

        timeLabel.config(text=f"{minutes:02}:{seconds:02}")

        time_id = janela.after(1000, iniciar)
    
    else:
        iniciar_descanso()

def iniciar_descanso():
    global ciclo, time_rest, time_count,time_id 
    if ciclo < 4: 
        if time_rest > 0:
            time_rest -= 1
            minutes = time_rest // 60
            seconds = time_rest % 60

            timeLabel.config(text=f"{minutes:02}:{seconds:02}")

            time_id = janela.after(1000, iniciar_descanso)

        else: 
            time_count = time_set * 60
            time_rest = time_count // 4
            iniciar()
            ciclo=contador_ciclo(ciclo)
            NcicloLabel.config(text=f"{ciclo}")

def contador_ciclo(ciclo):
    return ciclo +1 
    
def reset():
    global ciclo, time_rest, time_count,time_id 

    if time_id != None:
        janela.after_cancel(time_id)
        time_count = time_set * 60
        time_rest = time_count // 4
        ciclo = 1
        NcicloLabel.config(text=f"{ciclo}")

        minutes = time_count // 60
        seconds = time_count % 60

        timeLabel.config(text=f"{minutes:02}:{seconds:02}")


buttonStart = tk.Button(janela, text="Iniciar", command=iniciar)
buttonReset = tk.Button(janela, text="Resetar", command=reset)
buttonStart.pack()
buttonReset.pack()

janela.mainloop()