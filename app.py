from flask import Flask
from api import init_bp, items_bp, user_bp
from pages import pages_bp, main_bp, other_bp

app = Flask("__name__")

app.register_blueprint(init_bp)
app.register_blueprint(items_bp)
app.register_blueprint(user_bp)

app.register_blueprint(pages_bp)
app.register_blueprint(main_bp)
app.register_blueprint(other_bp)


if __name__ == "__main__":
    app.run(debug=True)
