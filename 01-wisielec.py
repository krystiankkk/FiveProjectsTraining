import sys
attempts = 5
word = 'kamila'


def show_state_of_game():
    print()
    print(user_word)
    print(f'ozostalo prob{attempts}')
    print(used_letters)
    print()


def find_indexes(word, letter):
    indexes =[]
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes


user_word = []
used_letters = []

for _ in word:
    user_word.append("_")

while True:
    letter = input('Podaj jakas literę')
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print('nie ma takiej litery')
        attempts -= 1

        if attempts == 0:
            print('Koniec gry')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        temp = "".join(user_word)
        if temp == word :
            print('Wygrales chuju')
            sys.exit(0)
    show_state_of_game()


##mozliwosc restaru po przegranej/wygranej
## walidacja czy podaje dobry znak (char, nie int czy float i in)
## baza slow - z api / listy
## jezeli juz podano litere to kolejna szansa
## lista słów - losowanie tych ktorych nie wykorzystano
## ile szans chcesz miec // poziom trudnosci 1/3/5 attempts
##