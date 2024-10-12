import inquirer

def main():

    nameQuestion = [
        
        inquirer.Text('name', message="Qual é o seu nome?"),
        
    ]

    username = inquirer.prompt(nameQuestion)

    print(f"Olá, {username['name']}! Seja bem-vindo(a).")
    
    servicesQuestionList = [
        
        inquirer.List('services', message="O que gostaria de calcular hoje?", 
                      
                      choices=["Emissão de CO2 para Gasolina", "Emissão de CO2 para Etanol", "Emissão de CO2 para Diesel", "Emissão de CO2 para Bio Diesel", "Emissaão de CO2 para Eletricidade"],),
        
    ]
    
    list = inquirer.prompt(servicesQuestionList)
    
    print(list)
    


if __name__ == "__main__":

    main()
