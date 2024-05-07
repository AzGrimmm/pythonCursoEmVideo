nome = str(input('Digite seu nome completo: ')).strip()
upper = nome.upper()
lower = nome.lower()
split = nome.split()
length = len(nome) - nome.count(' ') 
firstName = split[0]
firstNameLength = len(firstName)
lastName = split[len(split) - 1]

print(firstName)
print(lastName)
print(upper)
print(lower)
print(length)
print(firstNameLength)

