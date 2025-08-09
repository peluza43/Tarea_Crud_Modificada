from flask import Flask
from flask_cors import CORS
from routes import api

app = Flask(__name__)
CORS(app)                  # permite que el frontend (otro origen) consuma la API
app.register_blueprint(api)

@app.get("/api/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
