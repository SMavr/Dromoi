from flask import Flask, render_template

app = Flask(__name__)
items = ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple']

@app.route('/')
def index():
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

