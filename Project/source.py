from flask import Flask, render_template, redirect, url_for, request, abort
import json
import fact
import main
app = Flask('app')

@app.route('/')
def root():
    return render_template('Index'+'.html')

@app.route('/submit', methods=['POST'])
def sumbit():
    resp = request.get_json()
    res = str(fact.fact(resp['n']))
    resp = json.dumps({'res': res})
    print(resp)
    return resp


@app.route('/submit1', methods=['POST'])
def solve():
    resp=request.get_json()
    rez =str(main.nsp(resp['s'], resp['n']))
    resp = json.dumps({'res': rez})
    print(resp)
    return resp
@app.route('/CalculatorI')
def CalI():
    return render_template('CalculatorI'+'.html')

@app.route('/CalculatorM')
def CalM():
    return render_template('CalculatorM'+'.html')

@app.route('/EgeInf')
def EgeInf():
    return render_template('EgeInf'+'.html')

@app.route('/EgeMath')
def EgeMath():
    return render_template('EgeMath'+'.html')

@app.route('/Index')
def Index():
    return render_template('Index'+'.html')


app.run(host='127.0.0.1', port = 55557)
