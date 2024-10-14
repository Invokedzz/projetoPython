# Importa as bibliotecas e o arquivo functions.py

import functions as functions

import inquirer

import asyncio

from rich.console import Console

console = Console()

# Cria uma classe, e insere as functions "start" e "allChoices"

class main: 
    
    async def start (self):
        
        # Por meio do Inquirer, cria uma mensagem perguntando o nome do usuário
        
        nameQuestion = [
            
            inquirer.Text('name', message="Qual é o seu nome?"),
            
        ]
        
        username = inquirer.prompt(nameQuestion);
        
        # Caso o nome seja vazio, exibe uma mensagem de erro
        
        if username['name'] == "":
            
            console.print("Por favor, digite seu nome.", style="underline red")
            
            # Chama novamente a função
            
            return await self.start() 
        
        # Caso contrário, exibe uma mensagem de bem-vindo
        
        console.print(f"Olá, {username['name']}! Seja bem-vindo(a).", style="bold underline blue")
        

    async def allChoices (self):
     
        # Espera pela function "start" e depois inicia a function "allChoices"

        await self.start()
        
        # Enquanto for verdade, o usuário pode escolher o que deseja fazer
    
        while True:
            
            # Exibe as escolhes possíveis por meio do inquirer
            
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
        
            # Caso selecionar, inicializa emissao_gasolina()
        
            if selected_service['services'] == "Emissão de CO2 para Gasolina":
            
                functions.emissao_gasolina()
            
            # Caso selecionar, inicializa emissao_etanol_anidro()
            
            if selected_service['services'] == "Emissão de CO2 para Etanol (anidro)":
            
                functions.emissao_etanol_anidro()
            
            # Caso selecionar, inicializa emissao_etanol_hidratado()
            
            if selected_service['services'] == "Emissão de CO2 para Etanol (hidratado)":
        
                functions.emissao_etanol_hidratado()
            
            # Caso selecionar, inicializa emissao_diesel()
            
            if selected_service['services'] == "Emissão de CO2 para Diesel":
            
                functions.emissao_diesel()
            
            # Caso selecionar, inicializa emissao_bio_diesel()
            
            if selected_service['services'] == "Emissão de CO2 para Bio Diesel":
            
                functions.emissao_bio_diesel()
            
            # Caso selecionar, inicializa emissao_eletrica()
            
            if selected_service['services'] == "Emissão de CO2 para Eletricidade":
            
                functions.calcular_emissao_eletrica()
            
            # Caso sair, o programa finaliza
            
            if selected_service['services'] == "Sair":
            
                print("Obrigado por utilizar nosso sistema!")
            
                break
        
# Inicializa nossa classe, e nossa função "allChoices"
        
if __name__ == "__main__":
    
    main_instance = main()
    
    asyncio.run(main_instance.allChoices())