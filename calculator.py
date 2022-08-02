# Метод который считает + - * / 
def CalculateSimpleOperations(lst): 
    temp = 0
    # Умножение
    while '*' in lst:
        temp = lst[lst.index('*')-1] * lst[lst.index('*')+1]
        lst.insert(lst.index('*')-1, temp)
        lst.pop(lst.index('*')-1)
        lst.pop(lst.index('*')+1)
        lst.pop(lst.index('*'))
    # Деление
    while '/' in lst:
        temp = lst[lst.index('/')-1] / lst[lst.index('/')+1]
        lst.insert(lst.index('/')-1, temp)
        lst.pop(lst.index('/')-1)
        lst.pop(lst.index('/')+1)
        lst.pop(lst.index('/'))
    # Сложение
    while '+' in lst:
        temp = lst[lst.index('+')-1] + lst[lst.index('+')+1]
        lst.insert(lst.index('+')-1, temp)
        lst.pop(lst.index('+')-1)
        lst.pop(lst.index('+')+1)
        lst.pop(lst.index('+'))
    # Вычитание
    while '-' in lst:
        temp = lst[lst.index('-')-1] - lst[lst.index('-')+1]
        lst.insert(lst.index('-')-1, temp)
        lst.pop(lst.index('-')-1)
        lst.pop(lst.index('-')+1)
        lst.pop(lst.index('-'))
    return lst[0]

# Метод который считает с учетом скобок
def Calculator(lst):
    tempList = []
    if '(' in lst or ')' in lst:
        for item in enumerate(lst):
            if item[1] == '(':
                index_of_first_parenthesis = item[0]

        for item in enumerate(lst):
            if item[1] == ')':
                index_of_second_parenthesis = item[0]

        for i in range(index_of_first_parenthesis+1, index_of_second_parenthesis):
            tempList.append(lst[i])
        lst.insert(index_of_first_parenthesis, CalculateSimpleOperations(tempList))
        # print(lst)
        del lst[index_of_first_parenthesis+1:index_of_second_parenthesis+2]
        # print(lst)
        return CalculateSimpleOperations(lst)
    else:
        return CalculateSimpleOperations(lst)
