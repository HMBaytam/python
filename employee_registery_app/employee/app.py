from flask import Flask, request, redirect, url_for
from flask import render_template
from employee.employee import Employee
app = Flask(__name__)

names = []
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        first = request.form.get('first')
        last = request.form.get('last')
        pay = request.form.get('pay')

        emp = Employee(first, last, pay)
        names.append(emp)
    return render_template('form.html', title='Add Employee')


@app.route('/employee_list')
def list():
    return render_template('list.html', names=names)


@app.route('/employee_list/<name>/', methods=['POST', 'GET'])
def employee_info(name):
    info = ''
    for nme in names:
        if name == nme.first:
            info = nme
            return render_template('info.html', info=info)

    return render_template('info.html', message='Employee not found')


@app.route('/employee_list/<name>/raise', methods=['POST', 'GET'])
def update_salary(name):
    if request.method == 'POST':
        for nme in names:
            if name == nme.first:
                nme.apply_raise()
    return redirect(url_for('employee_info', name=name))


if __name__ == '__main__':
    app.run()
