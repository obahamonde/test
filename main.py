from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if "theme" in request.args:
        theme = request.args["theme"]
    else:
        theme = "light"
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "World"
    return render_template("index.html", theme=theme, name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)