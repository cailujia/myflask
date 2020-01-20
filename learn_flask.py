from flask import Flask,redirect,url_for,request,render_template,make_response

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_word(name):
    return  'hello %s! '%name

@app.route('/admin')
def hello_admin():
    return "hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s as Guest'%guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s'%name

# @app.route('/login',methods=['POST','GET'])
# #def login():
#     print(request)
#     if request.method == 'POST':
#         user = request.form['name']
#         return redirect(url_for('success',name=user))
#     else:
#         user = request.args.get('name')
#         return redirect(url_for('success',name=user))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/compare/<mark>')
def compare(mark):
    return render_template('compare.html',mark=int(mark))


@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result',methods=["POST"])
def result():
    if request.method =='POST':
        result = request.form
        print(result)
        return render_template('result.html',result = result)

@app.route('/index2')
def index2():
    return render_template('index2.html')

#cookie

@app.route('/setcookie',methods=['POST'])
def setcookie():
    user = request.form['nm']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return """'<h1>welcome '&plus;name&plus;'</h1>'"""










if __name__ == '__main__':
    app.run()