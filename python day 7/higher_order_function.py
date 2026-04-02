def process_users(users, func):
    return list(map(func, users))


names = ["vicky", "deva"]

result = process_users(names, lambda x: x.upper())

print(result)