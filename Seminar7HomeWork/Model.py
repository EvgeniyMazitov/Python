first = 0
second = 0
result = 0
oString = ''
choice = 1


listOperator = {'*': lambda x, y: int(x) * int(y),
                '/': lambda x, y: int(x) / int(y),
                '+': lambda x, y: int(x) + int(y),
                '-': lambda x, y: int(x) - int(y)}


def set_first(number: int):
    global first
    first = number


def set_second(number: int):
    global second
    second = number


def set_result(oper: str):

    # ДЕЛЕНИЕ НА НОЛЬ!!!!
    global result
    global second
    result = listOperator.get(oper)(first, second)


def Set_Ostring(string: str):
    global oString
    oString = string


def get_first():
    global first
    return first


def get_second():
    global second
    return second


def get_result():
    global result
    return result


def get_string():
    global oString
    return oString


def Set_parserString():
    global oString
    global result
    resultString = ''
    resultString = oString .replace(' ', '').strip()
    resultString = resultString .replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    resultString = resultString .split()

    while len(resultString) > 1:
        if '*' in resultString or '/' in resultString:
            for i in range(len(resultString)):
                if operation(resultString, i, '*'):
                    break
                if operation(resultString, i, '/'):
                    break

        elif '+' in resultString or '-' in resultString:
            for i in range(len(resultString)):
                if operation(resultString, i, '+'):
                    break
                if operation(resultString, i, '-'):
                    break
    result = int(resultString[0])
    return result


def deleteElement(string: list, i: int):
    string.pop
    string.pop(i + 1)
    string.pop(i)


def operation(string, i, oper):
    if string[i] == oper:
        string[i-1] = listOperator.get(oper)(int(string[i - 1]),
                                             int(string[i + 1]))
        deleteElement(string, i)
        return True
