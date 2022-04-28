from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

from modules import GetUsers, AddUser, CompPw

app = Flask(__name__, static_folder='./templates', static_url_path='')
app.secret_key = 'hoge' # session を暗号化するために必要
app.permanent_session_lifetime = timedelta(minutes=3) # session が維持される時間

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
  msg = request.args.get('msg', '') 
  return render_template('get.html', msg=msg)

@app.route('/post', methods=['GET', 'POST'])
def post():
  if request.method == 'POST':
    name = request.form.get('name')
    passwd = request.form.get('passwd')
    return render_template('post.html', name=name, passwd=passwd)
  else:
    return render_template('post.html')

@app.route('/useradd', methods=['GET', 'POST']) 
def useradd():
  if request.method == "POST":
    name = request.form['name']
    passwd = request.form['passwd']
    if name != "" and passwd != "" : # session に追加
      AddUser(name, passwd)
  return render_template('useradd.html', users=GetUsers())


@app.route('/login', methods=['GET', 'POST'])
def login():
  logined = False
  if 'name' in session : # session に name があるとログイン中
    logined = True
  else : # 未ログイン
    if request.method == "POST" : # POST の時はログイン処理
      uid = request.form['uid']
      passwd = request.form['passwd']
      if uid != "" and passwd != "" : # session に追加
        name = CompPw(uid, passwd)
        if name != "":
          session['name'] = name
          logined = True
  if logined : # ログイン済み
    return redirect(url_for('mypage'))
  else : # GET の時, name と passwd のどちらかが空の場合はログインページ
    return render_template('login.html', users=GetUsers())


@app.route('/mypage')
def mypage():
  if 'name' in session : # ログイン中
    return render_template('mypage.html', name=session['name'])  
  else :
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
  if 'name' in session : # ログイン中
    session.pop('name', None)
    return render_template('logout.html')
  else : # ログイン中でない場合はログインページへ
    return redirect(url_for('login'))


app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
