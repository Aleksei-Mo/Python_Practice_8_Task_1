def ComplexInput(userStr):
    lenght=len(userStr)
    strRe=''
    strIm=''
    flagIm=False
    for i in range(lenght):
        if userStr[i].isdigit() or userStr[i]=='-': 
            if flagIm==False and userStr[i+1]!="i":
                strRe=strRe+userStr[i]
                if userStr[i+1]=="+" or userStr[i+1]=="-":
                    flagIm=True
            else:
                strIm=strIm+userStr[i]
    if strIm=='':
        strIm='1'
    if strRe=='':
        strRe='0'
    return [int(strRe),int(strIm)]
    
def ComplexOperations(num1,num2,oper):
    match oper:
        case '+':
            if (num1[1]+num2[1])>=0:
                result=str(num1[0]+num2[0])+'+'+str(num1[1]+num2[1])+'i'
            else:
                result=str(num1[0]+num2[0])+str(num1[1]+num2[1])+'i'
        case '-':
            if (num1[1]+num2[1])>=0:
                result=str(num1[0]-num2[0])+'+'+str(num1[1]-num2[1])+'i'
            else:
                result=str(num1[0]-num2[0])+str(num1[1]-num2[1])+'i' 
        case '*':
            if (num1[0]*num2[1]+num1[1]*num2[0])>=0:
                result=str(num1[0]*num2[0]-num1[1]*num2[1])+'+'+str(num1[0]*num2[1]+num1[1]*num2[0])+'i'
            else:
                result=str(num1[0]*num2[0]-num1[1]*num2[1])+str(num1[0]*num2[1]+num1[1]*num2[0])+'i'
        case '/':
            if ((num1[1]*num2[0]-num1[0]*num2[1])/(num2[0]**2+num2[1]**2))>=0:
                result=str((num1[0]*num2[0]+num1[1]*num2[1])/(num2[0]**2+num2[1]**2))+'+'+str((num1[1]*num2[0]-num1[0]*num2[1])/(num2[0]**2+num2[1]**2))+'i'
            else:
                result=str((num1[0]*num2[0]+num1[1]*num2[1])/(num2[0]**2+num2[1]**2))+str((num1[1]*num2[0]-num1[0]*num2[1])/(num2[0]**2+num2[1]**2))+'i'
    return result
