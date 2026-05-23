from app.models import app
from app.routes.main import main_bp
from app.routes.registration import registration_bp
from app.routes.profile import profile
from app.routes.auth import authenitication
from app.routes.de_auth import de_auth

app.register_blueprint(main_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(profile)
app.register_blueprint(authenitication)
app.register_blueprint(de_auth)
