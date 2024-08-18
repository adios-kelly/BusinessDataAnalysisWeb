from flask import Flask, render_template
from flask import request
from mcalc import m_simple_calc,m_std_calc


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simple_calc', methods=['POST','GET'])
def simple_calc():
    return m_simple_calc()

@app.route('/std_calc', methods=['POST','GET'])
def std_calc():
    return m_std_calc()

    
if __name__ == '__main__':
    app.run(debug=True)
