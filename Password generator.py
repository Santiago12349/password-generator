import random

letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers =['0','1','2','3','4','5','6','7','8','9']

symbols =['!', '#', '$', '%', "&", '(', ')', '*', '+']

pnumber_1 = []
pnumber_s = []
pnumber_n = []

print("PyPassword generator")
number_l=int(input("How many letters would you like in your password?\n"))
number_s=int(input("How many symbols would you like?\n"))
number_n=int(input("How many numbers would you like?\n"))

if number_l > 1:
    for nletters in range(1,number_l+1):
        pnumber_1.append(letters[random.randint(1,len(letters)-1)])

if number_s > 1:
    for nsymbols in range(1,number_s+1):
        pnumber_s.append(symbols[random.randint(1,len(symbols)-1)])

if number_n > 1:
    for nnumbers in range(1,number_n+1):
        pnumber_n.append(numbers[random.randint(1,len(numbers)-1)])

print(pnumber_1)
print(pnumber_s)
print(pnumber_n)

# number_of_characters = number_l + number_s + number_n

t = pnumber_1 + pnumber_s + pnumber_n

random.shuffle(t)

password = ''.join(t)

print(password)
print(len(password))








