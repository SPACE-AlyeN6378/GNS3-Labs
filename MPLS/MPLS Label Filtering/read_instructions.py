with open("readme.md", "r", encoding='utf-8') as file:
    instructions = file.read().split("\n- ")

for step in instructions:
    print(step)
    input("")

    
