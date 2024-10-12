def calcular_emissao_eletrica(): 
    
    try:        
        
        kwh_consumidos = float(input("Informe a quantidade de eletricidade consumida (em kWh): "))
        
        fator_emissao = float(input("Informe o fator de emissão de carbono (em kg CO₂ por kWh): "))
        
        emissoes = kwh_consumidos * fator_emissao 
        
        print(f"A emissão total de carbono é: {emissoes:.2f} kg CO₂")
        
    except ValueError:        
        
        print("Por favor, insira valores numéricos válidos.")
        

def emissao_gasolina(): 
    
    try:        
        
        distancia = int(input("Qual a distância percorrida em km? ")) 
        
        consumo = int(input("Quantos litros foram utilizados? "))
        
        con = consumo / 100
        
        litros_usados = (distancia / 100) * con
        
        fator_emissao = 2.3/litros_usados
        
        co2_emitido = litros_usados * fator_emissao
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂")

    except ValueError:
        
        print("Por favor, insira valores numéricos válidos.")
        
def emissao_diesel():

    try:        
        
        distancia = int(input("Qual a distância percorrida em km? "))
        
        consumo = int(input("Quantos litros foram utilizados? "))
        
        con = consumo / 100 
        
        litros_usados = (distancia / 100) * con
        
        fator_emissao = 2.7 / litros_usados
        
        co2_emitido = litros_usados * fator_emissao
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂")
        
    except ValueError:
        
        print("Por favor, insira valores numéricos válidos.")
        
def emissao_bio_diesel():
    
    try:
        
        distancia = int(input("Qual a distância percorrida em km? "))
        
        consumo = int(input("Quantos litros foram utilizados? "))
        
        con = consumo / 100 
        
        litros_usados = (distancia / 100) * con 
        
        fator_emissao = 2.1/litros_usados 
        
        co2_emitido = litros_usados * fator_emissao 
        
        print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂") 
        
    except ValueError:        
        
        print("Por favor, insira valores numéricos válidos.")
        

emissao_bio_diesel()
        
emissao_diesel()
        
emissao_gasolina()
        
calcular_emissao_eletrica()