# p35: a simple login simulation: break and continue, @20170108;

while True:
    print('Who are you?')
    name = input()
    if name != 'Haoran':
        continue
    else:
        break

while True:
    print('Hello, Haoran. What is the password?')
    password = input()
    if password == 'swordfish':
        break
    else:
        continue

print('Access granted.')
