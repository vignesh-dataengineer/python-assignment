def square_generator(n):
    for i in range(n):
        yield i * i

# Normal list
square_list = [i * i for i in range(5)]
print("\nList:", square_list)
print("Type of list:", type(square_list))

# Generator
gen = square_generator(5)
print("Generator values:", list(gen))
print("Type of generator:", type(gen))