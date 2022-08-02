from datetime import datetime as dt
import view

def WriteLog(data, result):
    timeStamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.csv', 'a+') as file:
            file.write('{};{};=;{}\n'.format(timeStamp, data, result))
    
def ReadLog(period =''):
    date=0
    match period:
        case 'day':
            date=dt.today().day
            print("\n"+"Логи за текущий день:"+"\n")
            start=8
            end=10
        case 'month':
            date=dt.today().month
            print("\n"+"Логи за текущий месяц:"+"\n")
            start=5
            end=7
        case 'year':
            date=dt.today().year
            print("\n"+"Логи за текущий год:"+"\n")
            start=0
            end=4
    if 0<date<10:
        date='0'+str(date)
    else:
        date=str(date)
    with open('log.csv', 'r') as file:
        if period=='':
            view.viewLog(file.read())
        else:
            counter=0
            while True:
                tempStr=file.readline()
                if tempStr.find(date,start,end) != -1:
                   counter=counter+1
                   view.viewLog(tempStr)
                if not tempStr and counter==0:
                    print("Логи отсутствуют.")
                    break
                if not tempStr:
                    break
    print()
