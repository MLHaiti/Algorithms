from stack import Stack

# back button on a web browser use stack datastructure
lastVisitedPages = Stack()

lastVisitedPages.push("www.facebook.com")
lastVisitedPages.push("www.youtube.com")
lastVisitedPages.push("www.fds.edu.ht")
lastVisitedPages.push("www.dokla.ht")

# return the number of pages
print("The number of pages: {}".format(lastVisitedPages.sizeStack()))

# return the last page we have visited
print(f"last page : {lastVisitedPages.pop()}")

print(f"last page : {lastVisitedPages.pop()}")

# return the number of pages
print("The number of pages: {}".format(lastVisitedPages.sizeStack()))
