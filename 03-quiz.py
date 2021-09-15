import json
points = 0


def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question['a'])
    print("b:", question['b'])
    print("c:", question['c'])
    print("d:", question['d'])
    print()
    answer = input('Ktora odpowiedz wybierasz?')

    if answer == question["prawidlowa_odpowiedz"]:
        points+=1
        print('prawildowa odpow')
    else:
        print(f"blad, prawidlowa odpowiedz to: {question['prawidlowa_odpowiedz']}")


with open("quiz.json") as json_file:
    questions = json.load(json_file)
    for i in range(0, len(questions)):
        show_question(questions[i])

print(f'Punkty: {points}')
