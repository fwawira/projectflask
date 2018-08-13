from flask import Flask, render_template, request,redirect, url_for, make_response

from project import Project

from pygal import Pie


app = Flask(__name__)


@app.route('/')
def dashboard():
    projects  = Project.select()
    pie_chart = Pie()
    pie_chart.title = 'Project Type comparison'
    Internal = 0
    External=0
    for project in projects:
        if (project.type=='Internal'):
            Internal+=1
        else:
            External +=1
    pie_chart.add('External', External)
    pie_chart.add('Internal', Internal)
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    chart = pie_chart.render_data_uri()
    projects = Project.select()


    return render_template('index.html', projects_to_send=projects, chart=chart)


@app.route('/add', methods=['POST'])

def login():
    name = request.form['name_form']
    type=request.form['select_form']
    start_date = request.form['start_date']
    amount = request.form['amount']
    end_date = request.form['end_date']
    description = request.form['description']


    Project.create(name = name, type=type, start_date = start_date, end_date= end_date, amount= amount, description=description)

    return redirect('/')
@app.route('/delete/<int>')
def delete(int):
    Project.delete_by_id(int)
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    name = request.form['name_edit']
    type = request.form['select_edit']
    start_date = request.form['start_date_edit']
    amount = request.form['amount_edit']
    end_date = request.form['end_date_edit']
    description = request.form['description_edit']

    project = Project.get(Project.id ==id )
    project.name= name
    project.type=type
    project.start_date=start_date
    project.amount=amount
    project.description=description
    project.save()
    return redirect('/')



if __name__ == '__main__':

    app.run(debug='true')
