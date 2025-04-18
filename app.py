from flask import Flask
from components.views.router import views  # Blueprintルート登録

app = Flask(__name__)
app.register_blueprint(views)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)