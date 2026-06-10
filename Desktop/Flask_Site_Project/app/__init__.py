from app.models import app
from app.routes.main import main_bp
from app.routes.registration import registration_bp
from app.routes.profile import profile
from app.routes.auth import authenitication
from app.routes.de_auth import de_auth
from app.routes.create_profile import create_pr

app.register_blueprint(main_bp, url_prefix = "/")
app.register_blueprint(registration_bp, url_prefix = "/create_user")
app.register_blueprint(profile, url_prefix = "/profile")
app.register_blueprint(authenitication, url_prefix = "/authentication")
app.register_blueprint(de_auth, url_pefix = "/de_auth")
app.register_blueprint(create_pr, url_prefix = "/create")