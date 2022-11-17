import os
import dotenv
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
dotenv.load_dotenv(override=True)

@app.route('/')
def env_page():
    if os.environ.get('LOCATION') == 'home':
        app.config.from_pyfile('config/home.py')
        title = app.config.get('TITLE')
        return title
    else:
        app.config.from_pyfile('config/work.py')
        title = app.config.get('TITLE')
        return title

app.run()