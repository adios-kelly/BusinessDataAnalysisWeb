from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simple_calc')
def simple_calc():
    return render_template('simple_calc.html')

    
if __name__ == '__main__':
    app.run(debug=True)
