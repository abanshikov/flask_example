from flask import Flask
try:
    from config import Configuration
except:
    from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route("/")
def index():
    return f"<h1>Hello from flask!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
