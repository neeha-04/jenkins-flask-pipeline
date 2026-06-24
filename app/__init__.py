from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'jenkins-pipeline-secret-key'
    app.config['TESTING'] = False
    
    if config:
        app.config.update(config)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app