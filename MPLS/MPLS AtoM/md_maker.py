import os



with open("bullets.txt", "w") as file:
    line = input("- ")
    while line != "":
        file.write("- " + line + "\n")
        line = input("- ")

    
