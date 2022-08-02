
# Метод, который преобразовывает текст в список

def StringToList(text):
    text = ' ' + text
    tempList = []
    temp = ''
    for i in range(0, len(text)):
        # склейка цифр
        if text[i].isdigit() and not text[i-1].isdigit():
            temp = text[i]
            try:
                for j in range(1, 100):
                    temp = temp + str(int(text[i+j]))
            except:
                tempList.append(temp)
                temp = ''
        elif text[i] == '+' or text[i] == '-' or text[i] == '*' or text[i] == '/' or text[i] == '(' or text[i] == ')':
            tempList.append(text[i])

    resultList = []
    for i in tempList:
        try:
            resultList.append(int(i))
        except:
            resultList.append(i)

    return resultList


def NeedIntNumber(text):  # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            needTrue = True
            return number
        except:
            print('Ошибка ввода. Введите целое число: ')