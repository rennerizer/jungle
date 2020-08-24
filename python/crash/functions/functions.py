def favorite_book(title):
    print(f"Your favorite book is {title.title()}")

favorite_book("game of thrones")


def make_shirt(front_message, size='L'):
    print(f"You have selected a {size} shirt with the message: {front_message}")

make_shirt("Eat it, baby!")
make_shirt("I learned Python and all I got was this lousy shirt...", 'S')
