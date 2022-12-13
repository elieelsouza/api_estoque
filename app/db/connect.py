from app.db.configDataBase import engine
from app.models import models


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = """
        mariadb+mariadbconnector://db.development_cra
    """
    models.Base.metadata.create_all(bind=engine)
