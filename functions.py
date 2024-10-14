from tabulate import tabulate

def calcular_emissao_eletrica(): 
    
    try:        
        
        kwh_consumidos = float(input("Informe a quantidade de eletricidade consumida (em kWh): \n"))
        
        fator_emissao = float(input("Informe o fator de emissão de carbono (em kg CO₂ por kWh): \n"))
        
        emissoes = kwh_consumidos * fator_emissao 
        
        table = [["kWh consumidos", kwh_consumidos], ["Fator de emissão", fator_emissao]]
        
        if emissoes >= 100:
            
            return print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n")
        
        print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂\n")
        
        print(tabulate(table, tablefmt="fancy_grid"))
        
    except ValueError:        
        
        print("Por favor, insira valores numéricos válidos.\n")
        

def emissao_gasolina(): 
    try:       
         
        distancia = int(input("Qual a distância percorrida em km? \n")) 
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo 
        
        fator_emissao = 2.3
        co2_emitido = consumo_por_km * fator_emissao
        
        if co2_emitido >= 100:
            
            return print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n")
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.\n")

        
def emissao_diesel():
    
    try:
        distancia = int(input("Qual a distância percorrida em km? \n"))
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.7
        
        co2_emitido = consumo_por_km * fator_emissao
        
        if co2_emitido >= 100: 
            
            return print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n") 
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n")

    except ValueError:
        
        print("Por favor, insira valores numéricos válidos.\n")

        
def emissao_bio_diesel():
    
    try:
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.1
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        if co2_emitido >= 100:
            
            return print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n")
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n") 
        
    except ValueError:        
        
        print("Por favor, insira valores numéricos válidos.\n")
        

def emissao_etanol_anidro():  
      
    try:   
        
        distancia = int(input("Qual a distância percorrida em km? \n"))
        
        consumo = int(input("Quantos litros foram utilizados? \n"))
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 2.716
        
        co2_emitido = consumo_por_km * fator_emissao  
        
        if co2_emitido >= 100:
            
            return print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nivel de emissão.\n")
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n") 
        
    except ValueError:
        
        print("Por favor, insira valores numéricos válidos.\n")
        
def emissao_etanol_hidratado(): 
    
    try:  
        
        distancia = int(input("Qual a distância percorrida em km? \n"))  
        
        consumo = int(input("Quantos litros foram utilizados? \n")) 
        
        consumo_por_km = distancia / consumo
        
        fator_emissao = 1.867
        
        co2_emitido = consumo_por_km * fator_emissao 
        
        if co2_emitido >= 100:
            
            return print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n. Considerado um alto nível de emissão.\n")
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂\n") 
        
    except ValueError: 
        
        print("Por favor, insira valores numéricos válidos.\n")
        
