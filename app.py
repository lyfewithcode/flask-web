from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL
from pymysql import cursors

app = Flask(__name__)

# setting mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db_pegawai'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

# route atau alamat url-nya
@app.route('/')
def index():
    # ambil data
    sql = "SELECT * FROM pegawai"
    cursor = conn.cursor()
    cursor.execute(sql)
    hasil = cursor.fetchall()

    return render_template('index.html', data = hasil)

@app.route('/pegawai', methods = ['GET', 'POST'])
def pegawai():
    if request.method == 'POST': #simpan data
        _nama = request.values.get('nama')
        sql = "INSERT INTO pegawai(nama) VALUES(%s)"
        data = (_nama)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return redirect('/') #kembali ke halaman Index
    else: #tampilkan data
        return render_template('pegawai.html')