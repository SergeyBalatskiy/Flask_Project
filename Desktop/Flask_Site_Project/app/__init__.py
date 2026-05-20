from app.models import app
from app.routes.main import main_bp
from app.routes.registration import registration_bp
from app.routes.profile import profile
from app.routes.auth import authenitication

app.register_blueprint(main_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(profile)
app.register_blueprint(authenitication)
