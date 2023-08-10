from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitted_json = request.form['json_data']
        try:
            parsed_json = eval(submitted_json) 
            return render_template('result.html', json_data=parsed_json)
        except Exception as e:
            return f"Error parsing JSON: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
