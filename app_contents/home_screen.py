from flask import Flask, render_template

app = Flask(__name__)

# home
@app.route('/')
def home():
    return render_template('home_screen.html') #routes to html file

@app.route('/get_started', methods=['GET','POST'])
def get_started():
    return render_template('get_started.html') #routes to html file

@app.route('/linear_equations', methods=['GET','POST'])
def linear_equations():
    return render_template('linear_equations.html') #routes to html file

@app.route('/linear_quiz', methods=['GET','POST'])
def linear_quiz():
    return render_template('linear_quiz.html') #routes to html file

@app.route('/incorrect', methods=['GET','POST'])
def incorrect():
    return render_template('incorrect.html') #routes to html file

@app.route('/correct', methods=['GET','POST'])
def correct():
    return render_template('correct.html') #routes to html file

if __name__ == '__main__':
    app.run(debug=True)