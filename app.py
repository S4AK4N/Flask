from flask import Flask
from components.models.db import db
from components.views.router import views  # Blueprintルート登録

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)