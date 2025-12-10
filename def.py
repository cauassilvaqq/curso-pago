def calculate_love_score():
    
    name1 = input("Digite seu nome: ")
    name2 = input("Digite o nome do seu parceiro(a): ")
    
    combined_names = name1 + name2
    combined_names = combined_names.lower()

    true_score = (
        combined_names.count("v") +
        combined_names.count("e") +
        combined_names.count("r") +
        combined_names.count("d") +
        combined_names.count("a") +
        combined_names.count("d") +
        combined_names.count("e") + 
        combined_names.count("i") +
        combined_names.count("r") +
        combined_names.count("o")
    )
        
    love_score = (
        combined_names.count("a") +
        combined_names.count("m") +
        combined_names.count("o") +
        combined_names.count("r")
    )
        
    score = str(true_score) + str(love_score)
    print("Love Score:", score)


calculate_love_score()
