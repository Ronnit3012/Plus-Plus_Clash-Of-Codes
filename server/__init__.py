from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from api.analysis import routes as analysis_routes

load_dotenv()

app = Flask(__name__,
            static_url_path='', 
            static_folder='./public')
# app = Flask(__name__)
CORS(app, origins="*", supports_credentials=False)


app.register_blueprint(analysis_routes.analysis_bp, url_prefix='/api/v1/analysis')


app.run(port=os.environ["PORT"], debug=True)
