from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'
a1='templates/load.mp4'
code='123123'
id=1
@app.route('/load',methods=['GET','POST'])
def test():
    fail=0
    if (request.form):
        res1 = request.form['user']
        res2 = request.form['password']
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            charset='utf8',
            db='test',
            #Table='mylogin'
        )
        cursor = conn.cursor()
        sql = 'SELECT* FROM mylogin WHERE user=\'%s\''
        cursor.execute(sql % res1)
        re = cursor.fetchall()
        print(re)
        if(re is None):
            fail=1
            return render_template('test.html',fail=fail)
        else:
            for i in re:
                print(i[2],res2)
                if(i[2]==res2):
                    return redirect('/setu')
            fail=2
            return render_template('test.html',fail=fail)
        return render_template('test.html')
    return render_template('test.html')
@app.route('/vue.js')
def vue():
    return render_template('vue.js')
@app.route('/load.css')
def css():
    return render_template('load.css')
@app.route('/setu')
def new():
    return render_template('new.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if(request.form):
        res1 = request.form['author']
        res2 = request.form['code']
        res3 = request.form['agree']
        print(res1, res2, res3)
        if(res3==code):
            ans=1
            global id
            id+=1
            conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='',
                charset='utf8',
                db='test'
                # Table='paper'
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO mylogin(id,user,password)\
                                VALUE (%s,%s,%s)", (id, res1,res2))
            conn.commit()
        else:
            ans=0
        return render_template('register.html',ans=ans)
    return render_template('register.html')
app.run(host='0.0.0.0',debug=True);
