import calculator
import incoming
import logger
import menu
import sys
import view
import complexCalc

def button_click():
    menuChoice = menu.DrawMainMenu()
    match menuChoice:
        case '1':
            try:
                userInput = input('Введите выражение с вещественными числами, которое хотите посчитать: ')
                result = calculator.Calculator(incoming.StringToList(userInput))
                logger.WriteLog(userInput, result)
                view.view_data(userInput, result)
                button_click()
            except:
                print('\nНЕИЗВЕСТНАЯ ОШИБКА!\n')
                logger.WriteLog(userInput, 'НЕИЗВЕСТНАЯ ОШИБКА!')
        case '2':
            try:
                compNum1Str=input('Введите первое комплексное число. Например, a+bi: ')
                compNum2Str=input('Введите второе комплексное число. Например, с+di: ')
                compNum1=complexCalc.ComplexInput(compNum1Str)
                compNum2=complexCalc.ComplexInput(compNum2Str)
                operation=input('Введите желаюмую операцию (+,-,*,/): ')
                result = complexCalc.ComplexOperations(compNum1,compNum2,operation)
                userInput=compNum1Str+operation+compNum2Str
                logger.WriteLog(userInput, result)
                view.view_data(userInput, result)
                button_click()
            except:
                print('\nНЕИЗВЕСТНАЯ ОШИБКА!\n')
                logger.WriteLog(userInput, 'НЕИЗВЕСТНАЯ ОШИБКА!')
        case '3':
            while True:
              subMenuChoice=menu.DrawSubMenu()
              match subMenuChoice:
                case '1':
                    logger.ReadLog('')
                case '2':
                    logger.ReadLog('day')
                case '3':
                    logger.ReadLog('month')
                case '4':
                    logger.ReadLog('year')
                case '5':
                    button_click()
                    break
        case '4':
            sys.exit

#button_click() 