from flask import Flask
from routes.main_routes import MainRoutes


def test_web_homepage():
    app = Flask(__name__, template_folder="../templates/")
    MainRoutes.configure_routes(app)
    with app.test_client() as client:
        result = client.get("/")
        assert "home bal" in str(result.data)
