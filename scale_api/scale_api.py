from flask import Flask, render_template
import supported_scales

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', items= supported_scales.collection)

if __name__ == '__main__':
    app.run(debug=True)

