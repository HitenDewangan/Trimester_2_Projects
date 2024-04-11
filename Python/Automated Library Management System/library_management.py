from datetime import date, timedelta

books = {
  1: {
    "title": "The Lord of the Rings: The Fellowship of the Ring",
    "author": "J.R.R. Tolkien",
    "quantity": 2,
    "checked_out_by": None,
    "checkout_date": None
  },
  2: {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "quantity": 1,
    "checked_out_by": None,
    "checkout_date": None
  },
  3: {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "quantity": 3,
    "checked_out_by": None,
    "checkout_date": None
  },
  4: {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "quantity": 1,
    "checked_out_by": None,
    "checkout_date": None
  },
  5: {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "quantity": 4,
    "checked_out_by": None,
    "checkout_date": None
  },
  6: {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "quantity": 2,
    "checked_out_by": None,
    "checkout_date": None
  },
  7: {
    "title": "1984",
    "author": "George Orwell",
    "quantity": 1,
    "checked_out_by": None,
    "checkout_date": None
  },
  8: {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "quantity": 2,
    "checked_out_by": None,
    "checkout_date": None
  },
  9: {
    "title": "Frankenstein",
    "author": "Mary Shelley",
    "quantity": 1,
    "checked_out_by": None,
    "checkout_date": None
  },
  10: {
    "title": "The Handmaid's Tale",
    "author": "Margaret Atwood",
    "quantity": 3,
    "checked_out_by": None,
    "checkout_date": None
  }
}

users = {
  100: {
    "name": "Alice",
    "books_checked_out": [],  # List to store IDs of checked out books
    "fines" : 0
  },
  101: {
    "name": "Bob",
    "books_checked_out": [],
    "fines" : 0
  },
  102: {
    "name": "Charlie",
    "books_checked_out": [],
    "fines" : 0
  },
  103: {
    "name": "David",
    "books_checked_out": [],
    "fines" : 0
  },
  104: {
    "name": "Eve",
    "books_checked_out": [],
    "fines" : 0
  }
}


def list_books():
    """
    Prints information about all available books in the library.
    """
    print("-" * 50)
    print("** Books Available in the Library **")
    print("-" * 50)
    for book_id, book_info in books.items():
        availability = "Available" if book_info["quantity"] > 0 else "Unavailable"
        print(f"ID: {book_id}")
        print(f"Title: {book_info['title']}")
        print(f"Author: {book_info['author']}")
        print(f"Quantity: {book_info['quantity']} ({availability})")
        print("-" * 20)


def register_user():
    """
    Prompts the user for information and registers them with a unique ID.
    """
    new_id = max(users.keys()) + 1 if users else 100
    name = input("Enter your name: ")
    users[new_id] = {"name": name, "books_checked_out": [], "fines": 0.0}
    print(f"User registered successfully! Your ID is {new_id}")


def checkout_book(user_id, book_id):
    """
    Attempts to check out a book for a user. Updates book and user data if successful.
    """
    if user_id not in users:
        print(f"User with ID {user_id} not found.")
        return

    if book_id not in books:
        print(f"Book with ID {book_id} not found.")
        return

    if books[book_id]["quantity"] == 0:
        print(f"Sorry, there are no copies of '{books[book_id]['title']}' available.")
        return

    if len(users[user_id]["books_checked_out"]) >= 3:
        print(f"You cannot check out more than 3 books at a time.")
        return

    # Update book data
    books[book_id]["quantity"] -= 1
    books[book_id]["checked_out_by"] = user_id
    books[book_id]["checkout_date"] = str(date.today())

    # Update user data
    users[user_id]["books_checked_out"].append(book_id)

    print(f"Successfully checked out '{books[book_id]['title']}' for {users[user_id]['name']}.")
    print("Checkout Day : ", books[book_id]["checkout_date"])


def return_book(user_id, book_id):
    """
    Attempts to return a book for a user. Updates book and user data if successful,
    calculating overdue fines if applicable.
    """
    if user_id not in users:
        print(f"User with ID {user_id} not found.")
        return

    if book_id not in books:
        print(f"Book with ID {book_id} not found.")
        return

    if book_id not in users[user_id]["books_checked_out"]:
        print(f"User {users[user_id]['name']} has not checked out book with ID {book_id}.")
        return


    # Calculate overdue fine (if any)
    if "checkout_date" in books[book_id]:
      checkout_date = date.fromisoformat(books[book_id]["checkout_date"])
    else:
      print(f"Book with ID {book_id} has not been checked out.")
      return
    
    today = date.today()
    overdue_days = (today - checkout_date).days
    fine = max(0, overdue_days) * 1.0  # $1 fine per day

    #show all the details as a receit
    print("Book borrowed on", books[book_id]["checkout_date"])
    print("Book returned on", today)
    
    # Apply fine only if there are overdue days
    if overdue_days > 0:
        users[user_id]["fines"] += fine
        print(f"Overdue fine of ${fine:.2f} applied for book '{books[book_id]['title']}'.")
    else:
        print(f"Thank you for returning '{books[book_id]['title']} on time!")


    # Update book data
    books[book_id]["quantity"] += 1
    books[book_id]["checked_out_by"] = None
    books[book_id]["checkout_date"] = None

    # Update user data
    users[user_id]["books_checked_out"].remove(book_id)




#================================__MAIN__=================================#
print('='*50)
print("Remember !!!, For YES enter 'Y', For NO enter 'N'")
print('='*50)
print('='*50)
print("Welcome to library Management System")
print('='*50)

for i in range(0, 100):
    
    ans = input("Do you wanna explore library ? ")
    if(ans == 'Y'):
      
      print("A : Book Catalog\nB : User Registration\nC : Book Checkout\nD : Return Book")
      print('='*50)
      ans = input("Select an option (A/B/C/D) : ")

      if ans == 'A':
        list_books()
      elif ans == 'B':
        register_user()
      elif ans == 'C':
        user_id = int(input("Enter user id : "))
        book_id = int(input("Enter book id : "))
        checkout_book(user_id, book_id)
      elif ans == 'D':
        user_id = int(input("Enter user id : "))
        book_id = int(input("Enter book id : "))
        return_book(user_id, book_id)
      else:
        print("Invalid Input")
        break

    else:
       print('='*50)
       print("Thank you for visiting library (^_^)")
       print('='*50)
       break
        


