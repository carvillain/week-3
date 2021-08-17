#  Exercise 1:  Filter out all of the empty strings from the list

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

new_places = list(filter(lambda name: True if name.strip()  else False, places))

print(new_places)


#  Exercise 2: Write an anonymous function that cosrs this list by last name

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def authsort(authlist):
    authlist.sort(key=lambda x: x.split()[-1].lower())

    return authlist


print(authsort(author))


#  Exercise 3: Convert the list below from Celsius to Farhenheit

# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

def deg(list1):
    return list1[0], (9/5) * list1[1] + 32

farhenheit_places = list(map(deg, places))

farh = list(map(lambda place: (place[0], (9/5) * place[1] + 32), places))

print(farhenheit_places)
print(farh)


# Exercise 4: Write a recursion function to perform the fibonacci sequence up to the number passed in

def fib(num):
    if num <= 1:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)
    
print(f"Iteration 0: {fib(0)}")
print(f"Iteration 1: {fib(1)}")
print(f"Iteration 2: {fib(2)}")
print(f"Iteration 3: {fib(3)}")
print(f"Iteration 4: {fib(4)}")
print(f"Iteration 5: {fib(5)}")