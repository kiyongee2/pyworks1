from flask import Flask, render_template
import os

# app 객체 생성
app = Flask(__name__)

# 라우팅 설정
@app.route('/')
def home():
    return render_template('web.html')

@app.route('/style')
def style():
    return render_template('style.html')

@app.route('/gallery')
def gallery():
    photos_dir = os.listdir('static/photos')
    return render_template('gallery.html', photos=photos_dir)

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)