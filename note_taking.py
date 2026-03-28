note ="random.txt"
print("Welcome to the note-taking program!")

#mini functions to help make the program readable and organized
#define a function to append user input to the file
def file_append(user):    
    with open(note, "a") as file:
        file.write(user + "\n")
        print(f"you just wrote\n\n{user}\n")

#define a function to read the file
def file_read():
    with open(note, "r") as file:
        print("Everything you have written so far is\n")
        print(file.read())

#deftine a function to repeat question 1
def repeat():
    again = input("Do you want to write something else into the computer? (yes or no)\n").lower().strip()
    return again 
     




#write note function
def write_note():
    print("Great! I will put whatever you wrote into this computer")

    while True:
        user = input("What do you want to write?\n")
        file_append(user)
        file_read()

        again = repeat()

        while again not in ["yes", "no"]:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            again = repeat()

        if again == "no":
            break
#read note function
def read_note():
    with open(note, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("The file is empty\n") 
                    
            else:
                print(content)
                print("This is everything you have written so far\n")

#delete note function
def delete_note():     
    with open(note, "w") as file:
                file.write("")
                print("You have deleted everything in this file\n")

#delete a specific line function
def delete_line():
      with open(note, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("The file is empty. Nothing to delete.")
                else:
                    print("The file contains the following lines:")
                    for index, value in enumerate(lines, start=1):
                        print(f"{index}. {value.strip()}")

                    remove = int(input("Which line do you want to delete? (Enter the line number)\n"))
                    while remove < 1 or remove > len(lines):
                        print("Invalid line number. Please enter a valid line number.")
                        remove = int(input("Which line do you want to delete? (Enter the line number)\n"))

                    del lines[remove - 1]

                    with open(note, "w") as file:
                        file.writelines(lines)

                    print("Line deleted successfully. The updated file content is:")
                    with open(note, "r") as file:
                        print(file.read())
    
while True:
    print("1. Write")
    print("2. Read")
    print("3. Delete all")
    print("4. Delete a specific line")
    print("5. Exit\n")

    choose = input("Choose an option: ")

    if choose == "1":
        write_note()
    elif choose == "2":
        read_note()

    elif choose == "3":
        delete_note()

    elif choose == "4":
        delete_line()
    
    elif choose == "5":
        print("Goodbye!")
        break
