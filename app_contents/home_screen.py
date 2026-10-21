from flask import Flask, render_template

app = Flask(__name__)

# home
@app.route('/')
def home():
    return render_template('home_screen.html') #routes to html file

@app.route('/get_started', methods=['GET','POST'])
def get_started():
    return render_template('get_started.html') #routes to html file

if __name__ == '__main__':
    app.run(debug=True)