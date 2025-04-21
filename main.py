from waitress import serve
from main import app  # assuming your Flask app is in the main.py file

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
