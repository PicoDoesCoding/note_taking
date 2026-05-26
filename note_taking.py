NOTE_FILE = "random.txt"

print("Welcome to the note-taking program!")


def file_append(user):
    with open(NOTE_FILE, "a") as file:
        file.write(user + "\n")
    print(f"You just wrote:\n\n{user}\n")


def file_read():
    with open(NOTE_FILE, "r") as file:
        print("Everything you have written so far:\n")
        print(file.read())


def get_line_number(max_lines):
    while True:
        try:
            num = int(input("Which line do you want to delete? (Enter the line number)\n"))
            if 1 <= num <= max_lines:
                return num
            print(f"Enter a number between 1 and {max_lines}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def repeat():
    while True:
        again = input("Do you want to write something else? (yes or no)\n").lower().strip()
        if again in ["yes", "no"]:
            return again
        print("Invalid input. Please answer with 'yes' or 'no'.")


def write_note():
    print("Great! I will put whatever you write into this file.")
    while True:
        user = input("What do you want to write?\n")
        file_append(user)
        file_read()
        if repeat() == "no":
            break


def read_note():
    try:
        with open(NOTE_FILE, "r") as file:
            content = file.read()
        if content.strip() == "":
            print("The file is empty.\n")
        else:
            print(content)
            print("This is everything you have written so far.\n")
    except FileNotFoundError:
        print("No notes file found. Write something first!\n")


def delete_note():
    open(NOTE_FILE, "w").close()
    print("You have deleted everything in this file.\n")


def delete_line():
    try:
        with open(NOTE_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No notes file found. Write something first!\n")
        return

    if not lines:
        print("The file is empty. Nothing to delete.\n")
        return

    print("The file contains the following lines:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")

    remove = get_line_number(len(lines))
    del lines[remove - 1]

    with open(NOTE_FILE, "w") as file:
        file.writelines(lines)

    print("Line deleted successfully. Updated file:")
    print("".join(lines) if lines else "(empty)\n")


if __name__ == "__main__":
    while True:
        print("1. Write")
        print("2. Read")
        print("3. Delete all")
        print("4. Delete a specific line")
        print("5. Exit\n")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            write_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            delete_line()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–5.\n")