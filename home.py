from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure "index.html" is in the "templates" folder

if __name__ == "__main__":
    app.run()