from linkedlist import LinkedList

# example cases of linkedlist

linkedlist = LinkedList()

# adding element to my linkedlist
linkedlist.insertStart(5)
linkedlist.insertStart(12)
linkedlist.insertStart(30)
linkedlist.insertStart(70)

print(" we traverse the list first time...")
linkedlist.traverse()
print(" size at first: {}".format(linkedlist._size()))

# adding element at the end of my linkedlist
linkedlist.insertEnd(42)
linkedlist.insertEnd(22)

print("\n we traverse the list again after adding two elements at end...")
linkedlist.traverse()
print(" after adding more elements size becomes: {}".format(linkedlist._size()))

linkedlist.remove(42)

print("\n we traverse the list one more time after deleting 42...")
linkedlist.traverse()
print(" after removing elements size becomes: {}".format(linkedlist._size()))
