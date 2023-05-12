from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
    return render_template('home.html')

#app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True)