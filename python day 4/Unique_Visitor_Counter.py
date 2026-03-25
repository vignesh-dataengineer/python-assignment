visitors = set()

while True:
    name = input("Enter visitor name: ")
    visitors.add(name)

    print("Total unique visitors:", len(visitors))

    ch = input("Continue? (y/n): ")
    if ch == "n":
        break