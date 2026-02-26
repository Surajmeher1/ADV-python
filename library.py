users = {"alice": "alice@1", "bob": "secure456"}

books = {
    "The Great Gatsby": 5,
    "1984": 4,
    "The Catcher in the Rye": 6,
    "Brave New World": 2,
    "To Kill a Mockingbird": 3,
    "Moby Dick": 5,
    "Pride and Prejudice": 4,
    "The Hobbit": 7,
    "Harry Potter": 10,
    "The Alchemist": 8
}

logged_in_user = None


def login(): 
    global logged_in_user
    while True:
        print("=== LOGIN ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if users.get(username) == password:
            logged_in_user = username
            print(f"\nWelcome {username}! Login successful.\n")
            break
        else:
            print("Invalid username or password. Try again.\n")
def show_books():
    print("\nAvailable Books:")
    for title, qty in books.items():
        print(f"{title} --> {qty} copies")
    print()
def borrow_book():
    book_title = input("Enter book title to borrow: ")

    if book_title in books:
        if books[book_title] > 0:
            books[book_title] -= 1
            print(f"You borrowed '{book_title}'.")
            print(f"Remaining copies: {books[book_title]}\n")
        else:
            print("Book is out of stock.\n")
    else:
        print("Book does not exist.\n")
def return_book():
    book_title = input("Enter book title to return: ")
    if book_title in books:
        books[book_title] += 1
        print(f"You returned '{book_title}'.")
        print(f"Available copies: {books[book_title]}\n")
    else:
        print("Book does not exist.\n")
def library_menu():
    while True:
        print("=== Library Management ===")
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")



login()          
library_menu()   