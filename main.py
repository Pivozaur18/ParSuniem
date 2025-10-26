from flask import Flask, render_template

app = Flask(__name__, template_folder="pages", static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aksesauri')
def aksesauri():
    return render_template('aksesauri.html')

if __name__ == "__main__":
    app.run(debug=True)