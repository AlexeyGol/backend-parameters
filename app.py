"""Example of flask main file."""
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read configuration files
application_properties_from_configmap = None
application_secret_properties_from_secret = None

try:
    with open('/config/application.properties', 'r') as f:
        application_properties_from_configmap = f.read()
except FileNotFoundError:
    application_properties_from_configmap = 'File not found'
except Exception as e:
    application_properties_from_configmap = f'Error reading file: {str(e)}'

try:
    with open('/secret-config/application.secret.properties', 'r') as f:
        application_secret_properties_from_secret = f.read()
except FileNotFoundError:
    application_secret_properties_from_secret = 'File not found'
except Exception as e:
    application_secret_properties_from_secret = f'Error reading file: {str(e)}'


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


@app.route('/env')
def get_env():
    """Returns all environment variables including config files."""
    env_vars = dict(os.environ)
    env_vars['application.properties.from.configmap'] = application_properties_from_configmap
    env_vars['application.secret.properties.from.secret'] = application_secret_properties_from_secret
    return jsonify(env_vars)


if __name__ == '__main__':
    app.run()
