from flask import Blueprint, jsonify, render_template
import platform
import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@main.route('/api/info')
def info():
    return jsonify({
        'app': 'Jenkins Flask Pipeline',
        'python_version': platform.python_version(),
        'platform': platform.system(),
        'build': 'Advanced CI/CD Demo'
    })

@main.route('/api/greet/<name>')
def greet(name):
    if not name or not name.isalpha():
        return jsonify({'error': 'Invalid name'}), 400
    return jsonify({'message': f'Hello, {name}! Pipeline is running 🚀'})