from flask import Flask
from flask_mongoengine import MongoEngine
import os
from flask_caching import Cache

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = os.environ.get('DB_CONFIG') or {'DB': "my_bulletin"}
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or "Thi5_i5_my_5ecret_k33p_it_5afe"
app.config["CACHE_TYPE"] = 'redis'
app.config["CACHE_DEFAULT_TIMEOUT"] = 300
app.config["CACHE_REDIS_HOST"] = os.environ.get('CASH_HOST') or '127.0.0.1'
app.config["CACHE_REDIS_PORT"] = os.environ.get('CASH_PORT') or '6379'


db = MongoEngine(app)
mycache = Cache(app)

def register_blueprints(app):
    # Prevents circular imports
    from bulletin.routes import adverts
    app.register_blueprint(adverts)

register_blueprints(app)


if __name__ == '__main__':
    app.run()