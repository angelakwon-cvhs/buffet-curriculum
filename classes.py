# book1 = Book("", "", True)
# user1 = User("", "", "")

# user1.borrow_book("title")

# def borrow_book(self, book):
#     newBook = Book("", "", "")
#     #newBook.borrowed_books

# super AP debugger demo
def sayGoodbye(person_name):
    # really really complicated code
    lambda person_name: [person_name.append("a") for char in person_name]
    # for char in person_name:
    #     person_name.append("a")

def greetEveryone(greeting):
    time = 50
    if time >= 50:
        sayGoodbye("Chris")
    else: 
        greetEveryone("hello")
    # short circuiting
    # True or False
    # False and True

antisocial = False
def greet():
    if not antisocial:
        greetEveryone("hello")
        # breakpoint is on the line above
    else:
        sayGoodbye("Chris")    
 # official start of our program
greet()