'''

PR.2 Logic Box
Develop a Python program called Pattern Generator and Number Analyzer. This project
emphasizes control structures, loops (for and while), the range() function, control
statements (break, continue, pass), and nested loops for generating patterns. This
program allows students to practice these programming concepts and logical problem-solving skills.


'''


while True:
    print("\n\nWelcome to Pattern Generator and Number Analyzer!",end = "\n\n")
    print("Select an option:")
    print("1. Generate a Pattern.")
    print("2. Analyze a Range of Numbers.")
    print("3. Exit")
    choice = int(input("Please enter your choice:- "))
    if choice == 1:
        while True:
            print("\n\nChoose a pattern type:")
            print("1. Right-angled Triangle.")
            print("2. Pyramid.")
            print("3. Left-angled Triangle.")
            choice = int(input("Please enter your choice:- "))
            if choice == 1:
                row = int(input("\n\nEnter the number of rows for the pattern."))
                for i in range(1,row+1):
                    for j in range(1,i+1):
                        print("*",end = "")
                    print()
            elif choice == 2:
                rows = int(input("\n\nEnter the number of rows for the pattern."))
                for i in range(1, rows + 1):
                    print(" " * (rows - i), end="")
                    print("*" * (2 * i - 1))
            elif choice == 3:
                row = int(input("\n\nEnter the number of rows for the pattern."))
                for i in range(1, row + 1):
                    for s in range(row - i):
                        print(" ", end="")
                    for j in range(1, i + 1):
                        print("*", end="")
                    print()
            else:
                print("Please Enter a valid option.")
            break
            
                     
            
    elif choice == 2:
        start = int(input("\n\nPlease enter the start of the range:- "))
        end = int(input("Please enter the end of the range:- "))
        add = 0
        if start < end:
            for i in range(start,end+1):
                add = add + i
                if i%2 == 0:
                    print("Number",i,"is Even.")
                else:
                    print("Number",i,"is Odd.")
            print("Sum from all numbers from",start,"to",end,"is",add)

        elif start > end:
            for i in range(start,end-1,-1):
                add = add + i
                if i%2 == 0:
                    print("Number",i,"is Even.")
                else:
                    print("Number",i,"is Odd.")
            print("Sum from all numbers from",start,"to",end,"is",add)

        else:
            print("Start and end can't be the same.")
                
    elif choice == 3:
        break
    else:
        print("Please enter a valid option.")
print("\n\n\nYou have successfully exited the program:-)")
