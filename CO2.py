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
                               "Emissão de CO2 para Etanol", 
                               "Emissão de CO2 para Diesel", 
                               "Emissão de CO2 para Bio Diesel", 
                               "Emissão de CO2 para Eletricidade"]),
    ]
    
    selected_service = inquirer.prompt(servicesQuestionList)
    

    if selected_service['services'] == "Emissão de CO2 para Gasolina":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Gasolina.")
        
    if selected_service['services'] == "Emissão de CO2 para Etanol":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Etanol.")
        
    if selected_service['services'] == "Emissão de CO2 para Diesel":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Diesel.")
        
    if selected_service['services'] == "Emissão de CO2 para Bio Diesel":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Bio Diesel.")
        
    if selected_service['services'] == "Emissão de CO2 para Eletricidade":
        print(f"{username['name']} escolheu calcular a emissão de CO2 para Eletricidade.")

if __name__ == "__main__":
    main()
