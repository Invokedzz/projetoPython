import inquirer

def main():

    questions = [
        inquirer.Text('name', message="Qual é o seu nome?"),
    ]

    answers = inquirer.prompt(questions)

    print(f"Olá, {answers['name']}! Sua cor favorita é {answers['favorite_color']}.")


if __name__ == "__main__":

    main()
