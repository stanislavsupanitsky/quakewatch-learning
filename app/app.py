from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/info")
def info():
    return {
        "name": "quakewatch-learning",
        "version": "1.0.0",
        "description": "Simple Flask application for DevOps course project"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
