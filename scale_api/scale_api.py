from flask import Flask, render_template
import supported_scales

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', items= supported_scales.collection)

if __name__ == '__main__':
    app.run(debug=True)

