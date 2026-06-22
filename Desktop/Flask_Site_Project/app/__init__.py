from app.models import app
from app.routes.main import main_bp
from app.routes.registration import registration_bp
from app.routes.profile import profile
from app.routes.auth import authenitication
from app.routes.de_auth import de_auth
from app.routes.create_profile import create_pr
from app.routes.about_site import about_site_info
from app.routes.profile_edit import edit_pr
from app.routes.delete_profile import delete_profile
from app.routes.delete_user import delete_user

app.register_blueprint(main_bp, url_prefix = "/")
app.register_blueprint(registration_bp, url_prefix = "/create_user")
app.register_blueprint(profile, url_prefix = "/profile")
app.register_blueprint(authenitication, url_prefix = "/authentication")
app.register_blueprint(de_auth, url_pefix = "/de_auth")
app.register_blueprint(create_pr, url_prefix = "/create")
app.register_blueprint(about_site_info, url_prefix = "/about")
app.register_blueprint(edit_pr, url_prefix = "/edit")
app.register_blueprint(delete_profile, url_for= "/delete")
app.register_blueprint(delete_user, url_prefix = "/delete_user")