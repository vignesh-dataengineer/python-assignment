votes = {}

while True:
    name = input("Enter candidate: ")

    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

    ch = input("Continue voting? (y/n): ")
    if ch == "n":
        break

winner = max(votes, key=votes.get)
print("Winner:", winner)
print("Votes:", votes[winner])