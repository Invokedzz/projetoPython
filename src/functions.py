# Faz a importação das bibliotecas

from tabulate import tabulate

from rich.console import Console

import time

from rich.progress import track

console = Console()

def calcular_emissao_eletrica(): 
    
    try:        
        
        # Usuario informa os valores (kwh_consumidos e fator_emissao)
        
        kwh_consumidos = float(input("Informe a quantidade de eletricidade consumida (em kWh): \n"))
        
        fator_emissao = float(input("Informe o fator de emissão de carbono (em kg CO₂ por kWh): \n"))
        
        # Multiplica os valores fornecidos
        
        emissoes = kwh_consumidos * fator_emissao 
        
        # Por meio da lib tabulate, imprime a tabela com os valores fornecidos
        
        table = [["kWh consumidos", kwh_consumidos], ["Fator de emissão", fator_emissao]]
        
        # Exibe essa tabela para o usuario
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        # Caso o valor for maior ou igual a 100, exibe uma mensagem de alerta
        
        if emissoes >= 100:
            
            return console.print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")

        # Exibe uma barra de carregamento por meio da lib Rich

        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        # Exibe esta mensagem caso o valor seja menor que 100
        
        console.print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n. Baixo nível de emissão.\n", style="bold underline green")
        
    except ValueError:        
        
        # Exibe essa mensagem caso o valor não seja numérico
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        

def emissao_gasolina(): 
    
    try:       
         
         # Recebe os valores por meio do input
         
        distancia = int(input("Qual a distância percorrida em km? \n")) 
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        # Divide os valores, e insere em uma variável
        
        consumo_por_km = distancia / consumo 
        
        fator_emissao = 2.3
        
        # Multiplica os valores fornecidos
        
        co2_emitido = consumo_por_km * fator_emissao
        
        # Por meio da lib tabulate, imprime a tabela com os valores fornecidos
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))

        # Prepara a barra de carregamento por meio da lib Rich

        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        # Exibe esta mensagem caso o valor seja maior ou igual a 100
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        # Exibe uma barra de carregamento por meio da lib Rich
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green")

    except ValueError:
        
        # Exibe essa mensagem caso o valor não seja numérico
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")

        
def emissao_diesel():
    
    try:
        
        # Recebe os valores
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        # Divide os valores, e insere em uma variável
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.7
        
        # Multiplica os valores fornecidos
        
        co2_emitido = consumo_por_km * fator_emissao
        
        # Por meio da lib tabulate, imprime a tabela com os valores fornecidos
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        # Prepara a barra de carregamento por meio da lib Rich
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        # Exibe esta mensagem caso o valor seja maior ou igual a 100
        
        if co2_emitido >= 100: 
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red") 
        
        # Exibe uma outra mensagem caso o valor seja menor que 100
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green")

    except ValueError:
        
         # Exibe essa mensagem caso o valor não seja numérico
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")

        
def emissao_bio_diesel():
    
    try:
        
        # Recebe os valores
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        # Divide os valores, e insere em uma variável
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.1
        
        # Multiplica os valores fornecidos
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        # Por meio da lib tabulate, imprime a tabela com os valores fornecidos
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        # Prepara a barra de carregamento por meio da lib Rich
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        # Exibe esta mensagem caso o valor seja maior ou igual a 100
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        # Exibe uma outra mensagem caso o valor for menor que 100
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError:   
        
         # Exibe essa mensagem caso o valor não seja numérico     
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        

def emissao_etanol_anidro():  
      
    try:   
        
        # Recebe os valores
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        # Divide os valores fornecidos, e insere numa variável
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.716
        
        # Multiplica os valores fornecidos
        
        co2_emitido = consumo_por_km * fator_emissao  
        
        # Por meio da lib tabulate, imprime a tabela com os valores fornecidos
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        # Exibe essa tabela para o usuario
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        # Prepara a barra de carregamento por meio da lib Rich
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
            
            # Caso o valor for maior ou igual a 100, exibe uma mensagem de alerta
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nivel de emissão.\n", style="bold underline red")
        
        # Caso o valor for menor que 100, exibe uma outra mensagem
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError:
        
         # Exibe essa mensagem caso o valor não seja numérico
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        
def emissao_etanol_hidratado(): 
    
    try:  
        
        # Recebe os valores por meio do input
        
        distancia = int(input("Qual a distância percorrida em km? \n"))  
        
        consumo = int(input("Quantos litros foram utilizados? \n")) 
        
        # Divide os valores, e insere em uma variável
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 1.867
        
        # Calcula a emissão e insere em uma variável
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        # Prepara uma tabela por meio da lib tabulate
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        # Exibe a tabela com as informações fornecidas
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        # Prepara a barra de carregamento por meio da lib Rich
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        # Caso o valor for maior ou igual a 100, exibe uma mensagem
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        # Caso o valor for menor que 100, exibe uma outra mensagem
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError: 
        
         # Exibe essa mensagem caso o valor não seja numérico
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        
