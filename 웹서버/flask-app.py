from flask import Flask

# app 객체 생성
app = Flask(__name__)

# 라우팅 설정
@app.route('/')
def home():
    return "<h1>안녕, Flask!</h1>"

@app.route('/about')
def about():
    return "<h1>저는 김기용이라고 합니다.</h1>"

@app.route('/products/add')
def add_product():
    return "<h1>제품 등록 페이지입니다.</h1>"

# 애플리케이션 실행
app.run(debug=True)