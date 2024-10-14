from tabulate import tabulate

from rich.console import Console

import time

from rich.progress import track

console = Console()

def calcular_emissao_eletrica(): 
    
    try:        
        
        kwh_consumidos = float(input("Informe a quantidade de eletricidade consumida (em kWh): \n"))
        
        fator_emissao = float(input("Informe o fator de emissão de carbono (em kg CO₂ por kWh): \n"))
        
        emissoes = kwh_consumidos * fator_emissao 
        
        table = [["kWh consumidos", kwh_consumidos], ["Fator de emissão", fator_emissao]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        if emissoes >= 100:
            
            return console.print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")

        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        console.print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n. Baixo nível de emissão.\n", style="bold underline green")
        
    except ValueError:        
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        

def emissao_gasolina(): 
    
    try:       
         
        distancia = int(input("Qual a distância percorrida em km? \n")) 
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo 
        
        fator_emissao = 2.3
        
        co2_emitido = consumo_por_km * fator_emissao
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))

        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green")

    except ValueError:
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")

        
def emissao_diesel():
    
    try:
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.7
        
        co2_emitido = consumo_por_km * fator_emissao
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        if co2_emitido >= 100: 
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red") 
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green")

    except ValueError:
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")

        
def emissao_bio_diesel():
    
    try:
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.1
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError:        
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        

def emissao_etanol_anidro():  
      
    try:   
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.716
        
        co2_emitido = consumo_por_km * fator_emissao  
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nivel de emissão.\n", style="bold underline red")
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError:
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        
def emissao_etanol_hidratado(): 
    
    try:  
        
        distancia = int(input("Qual a distância percorrida em km? \n"))  
        
        consumo = int(input("Quantos litros foram utilizados? \n")) 
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 1.867
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        table = [["Distância percorrida (km)", distancia], ["Quantidade de litros consumidos", consumo]]
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
        for i in track(range(0,5), description="Calculando..."):
            
            time.sleep(1)
        
        if co2_emitido >= 100:
            
            return console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n", style="bold underline red")
        
        console.print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n", style="bold underline green") 
        
    except ValueError: 
        
        console.print("Por favor, insira valores numéricos válidos.\n", style="underline red")
        
