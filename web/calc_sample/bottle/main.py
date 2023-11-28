from bottle import route, run, template, request


def calculate(num_1, num_2, operation):
    try:
        number_1 = float(num_1)
        number_2 = float(num_2)
    except ValueError:
        pass
    try:
        if operation == '+':
            return number_1 + number_2
        elif operation == '-':
            return number_1 - number_2
        elif operation == '*':
            return number_1 * number_2
        elif operation == '/':
            if number_2 != 0:
                return number_1 / number_2
            else:
                return 'Division durch Null ist nicht erlaubt'
        else:
            return 'Unbekannte Operation'
    except UnboundLocalError as e:
        return "Bitte gebe Zahl 1 richtig an" if "number_1" in str(e) else "Bitte gebe Zahl 2 richtig an"

@route('/', method=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = request.forms.get('num1')
        num2 = request.forms.get('number_2')
        operation = request.forms.get('operation')
        result = calculate(num1, num2, operation)
    else:
        result = ''
    return template('''
        <form action="/" method="post">
            Zahl 1: <input name="num1" type="text" />
            Zahl 2: <input name="number_2" type="text" />
            <input name="operation" type="submit" value="+" />
            <input name="operation" type="submit" value="-" />
            <input name="operation" type="submit" value="*" />
            <input name="operation" type="submit" value="/" />
        </form>
        <p>Ergebnis: {{result}}</p>
    ''', result=result)


run(host='localhost', port=8081)

