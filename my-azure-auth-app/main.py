from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import auth, credentials
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Inisialisasi Firebase
cred = credentials.Certificate("path/to/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

# Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        
        try:
            # Verifikasi user via Firebase
            user = auth.get_user_by_email(email)
            # Simulasikan pengecekan password (gunakan Firebase Auth sebenarnya)
            session['user'] = email
            return redirect(url_for('protected'))
        except:
            return "Login Gagal"
    return render_template('login.html')

# Halaman Terproteksi
@app.route('/protected')
def protected():
    if 'user' in session:
        return render_template('protected.html')
    return redirect(url_for('login'))

# Halaman Home
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)