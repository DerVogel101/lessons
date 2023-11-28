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
        num1 = request.forms.get('number_1')
        num2 = request.forms.get('number_2')
        operation = request.forms.get('operation')
        result = calculate(num1, num2, operation)
    else:
        result = ''
    return template('''
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">

            <title>Rechner</title>
          </head>
          <body>
            <div class="container">
              <h1>Rechner</h1>
              <form action="/" method="post">
                <div class="mb-3">
                  <label for="number_1" class="form-label">Zahl 1</label>
                  <input type="text" class="form-control" id="number_1" name="number_1">
                </div>
                <div class="mb-3">
                  <label for="number_2" class="form-label">Zahl 2</label>
                  <input type="text" class="form-control" id="number_2" name="number_2">
                </div>
                <button type="submit" class="btn btn-primary" name="operation" value="+">+</button>
                <button type="submit" class="btn btn-primary" name="operation" value="-">-</button>
                <button type="submit" class="btn btn-primary" name="operation" value="*">*</button>
                <button type="submit" class="btn btn-primary" name="operation" value="/">/</button>
              </form>
              <p class="mt-3">Ergebnis: {{result}}</p>
            </div>

            <!-- Optional JavaScript; choose one of the two! -->

            <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"></script>

          </body>
        </html>
    ''', result=result)


run(host='localhost', port=8080)
