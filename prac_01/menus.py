"""
CP1404/CP5632 - Practical
Menu created using the following pseudocode below:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit)")
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("hello " + name)
    elif choice == 'G':
        print("goodbye " + name)
    else:
        print("Invalid choice!")
    print("(H)ello\n(G)oodbye\n(Q)uit)")
    choice = input(">>> ").upper()
print("Finished")