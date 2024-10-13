import inquirer

def main():

    nameQuestion = [
        inquirer.Text('name', message="Qual é o seu nome?"),
    ]
    
    username = inquirer.prompt(nameQuestion)
    
    if username['name'] == "":
        print("Por favor, digite seu nome.")
        main()
    
    print(f"Olá, {username['name']}! Seja bem-vindo(a).")
    

    servicesQuestionList = [
        
        inquirer.List('services', message="O que gostaria de calcular hoje?", 
                      
                      choices=["Emissão de CO2 para Gasolina", 
                               "Emissão de CO2 para Etanol (anidro)",
                               "Emissão de CO2 para Etanol (hidratado)", 
                               "Emissão de CO2 para Diesel", 
                               "Emissão de CO2 para Bio Diesel", 
                               "Emissão de CO2 para Eletricidade"]),
    ]
    
    selected_service = inquirer.prompt(servicesQuestionList)
    

    if selected_service['services'] == "Emissão de CO2 para Gasolina":
        
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
            
        emissao_gasolina()
        
    if selected_service['services'] == "Emissão de CO2 para Etanol (anidro)":
        def emissao_etanol_anidro():  
      
            try:   
        
                distancia = int(input("Qual a distância percorrida em km? "))
        
                consumo = int(input("Quantos litros foram utilizados? "))
        
                con = consumo / 100  
        
                litros_usados = (distancia / 100) * con 
        
                fator_emissao = 2.716/litros_usados
        
                co2_emitido = litros_usados * fator_emissao  
        
                print(f"A emissão total de carbono é: {co2_emitido:.2f} kg CO₂") 
        
            except ValueError:
        
                print("Por favor, insira valores numéricos válidos.")
                
        emissao_etanol_anidro()
        
    if selected_service['services'] == "Emissão de CO2 para Etanol (hidratado)":
        
    if selected_service['services'] == "Emissão de CO2 para Diesel":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Diesel.")
        
    if selected_service['services'] == "Emissão de CO2 para Bio Diesel":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Bio Diesel.")
        
    if selected_service['services'] == "Emissão de CO2 para Eletricidade":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Eletricidade.")

if __name__ == "__main__":
    main()
