# Pomodoro Study Timer

Aplicativo simples de Pomodoro Timer feito em Python com Tkinter para ajudar a organizar sessões de estudo.

O app permite definir o tempo de foco, iniciar ciclos de estudo e executar pausas automáticas entre os ciclos.

## Funcionalidades

Definir o tempo de estudo manualmente

Contador regressivo em tempo real

Pausas automáticas entre sessões

Controle de ciclos de estudo

Reset do timer

Interface simples usando Tkinter

# Como funciona

O aplicativo segue o método Pomodoro:

Você define o tempo de estudo.

O contador inicia.

Ao terminar o tempo de foco:

inicia automaticamente um descanso curto.

Após 4 ciclos, o timer para.

## Interface

O aplicativo possui:

Campo para definir o tempo de estudo

Botão Iniciar

Botão Resetar

Contador visual

Contador de ciclos

## Tecnologias utilizadas

Python 3

Tkinter (interface gráfica)

## Como executar

Clone o repositório:

git clone https://github.com/seu-usuario/pomodoro-app.git

Entre na pasta:

cd pomodoro-app

Execute o aplicativo:

python app.py

## Gerar executável

Para gerar um .exe:

Instale o PyInstaller:

pip install pyinstaller

Depois execute:

pyinstaller --onefile --windowed app.py

O executável será criado em:

dist/app.exe
📂 Estrutura do projeto
pomodoro-app
│
├── app.py
├── README.md
📌 Melhorias futuras

Descanso longo após 4 ciclos

Sons de notificação

Barra de progresso

Escolha de tempo de descanso

Interface aprimorada

Estatísticas de estudo

### Licença

Este projeto é open-source e pode ser usado livremente para fins de estudo e aprendizado.
