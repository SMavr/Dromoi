from flask import Flask, render_template
import supported_scales

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', items= supported_scales.collection)

@app.route('/scales/<int:scale_id>')
def scale_details(scale_id):
    # Fetch details of the component based on component_id
    # For example, you can retrieve details from a database
    component = next((c for c in supported_scales.collection if c.id == scale_id), None)
    if component:
        return f"Details of {component.name}"
    else:
        return "Component not found"


if __name__ == '__main__':
    app.run(debug=True)

