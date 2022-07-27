
UNKNOWN = -1
NUMBER = -2

PLUS = 1
MINUS = 2
MULTI = 3
DIVI = 4
POW = 5

TOKEN_TYPE = 10
EXECUTION_TYPE = 11

SYMBOL = {
    "+" : PLUS,
    "-" : MINUS,
    "*" : MULTI,
    "/" : DIVI,
    "^" : POW
}

class TOKEN :
    def __init__(self, type = TOKEN_TYPE, symbol = None, value = None) :
        self.__type = type
        self.__symbol = symbol
        self.__value = value
    
    @property
    def type(self) :
        return self.__type

    @type.setter
    def type(self, type) :
        self.__type = type

    @property
    def symbol(self) :
        return self.__symbol

    @property
    def value(self) :
        return self.__value

    @symbol.setter
    def symbol(self, symbol) :
        self.__symbol = symbol

    @value.setter
    def value(self, value) :
        self.__value = value

class EXECUTION :
    def __init__(self, type = EXECUTION_TYPE, command = None, args = None) :
        self.__type = type
        self.__command = command
        self.__args = args

    @property
    def type(self) :
        return self.__type

    @type.setter
    def type(self, type) :
        self.__type = type

    @property
    def command(self) :
        return self.__command

    @property
    def args(self) :
        return self.__args

    @command.setter
    def command(self, command) :
        self.__command = command

    @args.setter
    def args(self, args) :
        self.__args = args

def symbol_to_str(symbol) :
    if symbol == UNKNOWN :
        return "UNKNOWN"

    elif symbol == NUMBER :
        return "NUMBER"
    
    elif symbol == PLUS :
        return "PLUS"

    elif symbol == MINUS :
        return "MINUS"

    elif symbol == MULTI :
        return "MULTI"

    elif symbol == DIVI :
        return "DIVI"

    elif symbol == POW :
        return "POW"


def lex(e) :
    symbols = SYMBOL.keys() 
    token_list = []
    
    temp = None
    
    for i in range(len(e)) :
        char = e[i]
        token = TOKEN()

        if not char.isspace() :
            if char in symbols :
                token.symbol = SYMBOL[char]
                token.value = char

            elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
                if temp == None :
                    temp = i

                if i + 1 == len(e) or e[i + 1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
                    value = ""

                    for j in range(temp, i + 1) :
                        value += e[j]

                    token.symbol = NUMBER
                    token.value = int(value)

                    temp = None

                else :
                    continue

            else :
                token.symbol = UNKNOWN
                token.value = char

            token_list.append(token)

        else :
            continue

    return token_list

def parse(tree, state = 0) :
    # POW > MULTI, DIVI > PLUS, MINUS
    i = 0
    
    while i < len(tree) :
        if i < len(tree) :
            element = tree[i]
            execution = EXECUTION()

            if element.type == TOKEN_TYPE and element.symbol == POW and state == 0 :
                execution.command = element.symbol
                execution.args = (tree[i - 1], tree[i + 1])

                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.insert(i - 1, execution)

                i = i - 1

                continue

            elif element.type == TOKEN_TYPE and (element.symbol == MULTI or element.symbol == DIVI) and state == 1 :
                execution.command = element.symbol
                execution.args = (tree[i - 1], tree[i + 1])

                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.insert(i - 1, execution)

                i = i - 1

                continue

            elif element.type == TOKEN_TYPE and (element.symbol == PLUS or element.symbol == MINUS) and state == 2 :
                execution.command = element.symbol
                execution.args = (tree[i - 1], tree[i + 1])

                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.pop(i - 1)
                tree.insert(i - 1, execution)

                i = i - 1

                continue

            i += 1

        else :
            break

    # print_list = []

    # for e in tree :
    #     if e.type == TOKEN_TYPE :
    #         print_list.append(symbol_to_str(e.symbol))

    #     elif e.type == EXECUTION_TYPE :
    #         print_list.append(symbol_to_str(e.command))

    # print(print_list, state)

    if state <= 2 :
        parse(tree, state + 1)

    else :
        return

    return tree[0] # return top element
        
def execute(input_value, element) :
    if element.type == EXECUTION_TYPE :
        symbol = element.command
        args = element.args

        if symbol == PLUS :
            return execute(input_value, args[0]) + execute(input_value, args[1])

        elif symbol == MINUS :
            return execute(input_value, args[0]) - execute(input_value, args[1])

        elif symbol == MULTI :
            return execute(input_value, args[0]) * execute(input_value, args[1])

        elif symbol == DIVI :
            return execute(input_value, args[0]) / execute(input_value, args[1])

        elif symbol == POW :
            return execute(input_value, args[0]) ** execute(input_value, args[1])

    elif element.type == TOKEN_TYPE :
        symbol = element.symbol

        if symbol == NUMBER :
            return element.value
    
        elif symbol == UNKNOWN :
            return input_value

token_list = lex("x^2  + 8 * x + 16")
element = parse(token_list)
result = execute(1, element)

print(result)