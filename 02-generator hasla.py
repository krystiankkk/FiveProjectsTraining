import sys
import random
import string
password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print(f'Liczba malych znakow spoza przedzialu 0 - {characters_left}')
        sys.exit(0)
    else:
        characters_left -= number_of_characters
    print(f'pozostalo {characters_left} znakow')


password_lenght = int(input('Podaj dlugosc hasla'))

if password_lenght< 5:
    print('Haslo za krotkie! Minimalna dlugosc to 5 znakow')
    sys.exit(0)
else:
    characters_left = password_lenght

lowecaser_letters = int(input('Ilosc malych liter ma miec haslo'))
update_characters_left(lowecaser_letters)

uppercase_letters = int(input('Ilosc wielkich liter w hasle'))
update_characters_left(uppercase_letters)

special_characters = int(input('Ilosc znakow specjalnych'))
update_characters_left(special_characters)

digits = int(input('Ilosc cyfr'))
update_characters_left(digits)

if characters_left > 0:
    print('Nie wszystkie znaki zostaly wykorzystane, uzupelnie o male litery')
    lowecaser_letters+=characters_left

print()
print(f'Dlugosc hasla {password_lenght}')
print(f'Male litery {lowecaser_letters}')
print(f'Wielkie litery {uppercase_letters}')
print(f'Znaki specjalne {special_characters}')
print(f'Cyfry {digits}')

for _ in range(password_lenght):
    if lowecaser_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowecaser_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
random.shuffle(password)
print(f'Wygenerowane haslo: {"".join(password)}')


#walidacja do typow znakow - zbyt mala dlugosc -> jeszcze raz
#