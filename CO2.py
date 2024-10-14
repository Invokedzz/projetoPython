import functions 

import inquirer

import asyncio

class main: 
    
    async def start ():
        
        nameQuestion = [
            
            inquirer.Text('name', message="Qual é o seu nome?"),
            
        ]
        
        username = inquirer.prompt(nameQuestion);
        
        if username['name'] == "":
            
            print("Por favor, digite seu nome.")
            
            return main.start() 
        
        print(f"Olá, {username['name']}! Seja bem-vindo(a).")
        

    async def allChoices ():
     
        
        await main.start()
    
    while True:
            
        servicesQuestionList = [
            
            inquirer.List('services', message="O que gostaria de calcular hoje?", 
                          choices=[
                              
                                   "Emissão de CO2 para Gasolina",
                                    
                                   "Emissão de CO2 para Etanol (anidro)",
                                   
                                   "Emissão de CO2 para Etanol (hidratado)",
                                    
                                   "Emissão de CO2 para Diesel", 
                                   
                                   "Emissão de CO2 para Bio Diesel", 
                                   
                                   "Emissão de CO2 para Eletricidade",
                                   
                                   "Sair",
                                   
                                   ]),
            
        ]
        
        selected_service = inquirer.prompt(servicesQuestionList);
        
        if selected_service['services'] == "Emissão de CO2 para Gasolina":
            
            functions.emissao_gasolina()
            
        if selected_service['services'] == "Emissão de CO2 para Etanol (anidro)":
            
            functions.emissao_etanol_anidro()
            
        if selected_service['services'] == "Emissão de CO2 para Etanol (hidratado)":
        
            functions.emissao_etanol_hidratado()
            
        if selected_service['services'] == "Emissão de CO2 para Diesel":
            
            functions.emissao_diesel()
            
        if selected_service['services'] == "Emissão de CO2 para Bio Diesel":
            
            functions.emissao_bio_diesel()
            
        if selected_service['services'] == "Emissão de CO2 para Eletricidade":
            
            functions.calcular_emissao_eletrica()
            
        if selected_service['services'] == "Sair":
            
            print("Obrigado por utilizar nosso sistema!")
            
            break
        
if __name__ == "__main__":
    
    asyncio.run(main.allChoices())