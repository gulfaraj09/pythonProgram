def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This a book on Gulfaraj and Gufaraj and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
print("Search Started")
next(search)
search.send("Gulfaraj")
search.close()

# input("press any key")
# search.send("Gulfaraj and")
# input("press any key")
# search.send("this is")
# input("press any key")
# search.send("like this ")
