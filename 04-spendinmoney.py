expenses = []

def show_expenses(month):
    print(expenses)
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input('Podaj kwotę [zl]'))
    expense_type = input('Typ wydatku')
    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    total_amount_all = sum(expense_amount for expense_amount,_, _ in expenses)
    average_expanse_this_month = total_amount_this_month / number_of_expenses_this_month
    average_expanse_all = total_amount_all / len(expenses)
    print()
    print('Staty')
    print('Wszystkie wydatki w mcu', total_amount_this_month)
    print('Wszystkie wydatki', total_amount_all)
    print('Sredni wydatek / miesiac', average_expanse_this_month)
    print('Sredni wydatek / calosc', average_expanse_all)


while True:
    print()
    month = int(input("Wprowadz miesiac 1-12"))
    if month == 0:
        break
    while True:
        print()
        print('0 - powrot do wyboru miesiaca')
        print('1 - wyswietl wszystkie wydatki ')
        print('2 - dodaj wydatek ')
        print('3- statystyki ')
        choice = int(input('Wyswietl opcję '))

        if choice == 0:
            break

        if choice == 1:
            print('Wszystkie wydatki')
            show_expenses(month)
        if choice == 2:
            print('dodaj wydatek')
            add_expense(month)
        if choice == 3:
            show_stats(month)


#walidacja - czy liczba, z okreslonego przedzialu miesiac 1-12, inne opcje, przedzial 1-3 inne opcja dodatkowo
#rozbudowa statystyk - sortowanie od min do max albo odwrotnie
#definicja miesiecy - dict (1-styczne 2-luty itd)
# typy wydatkow- zdefiniować
