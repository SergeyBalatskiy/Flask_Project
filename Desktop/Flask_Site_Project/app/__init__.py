from flask import Flask
from app.routes.main import main_bp
from app.routes.registration import registration_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(registration_bp)
