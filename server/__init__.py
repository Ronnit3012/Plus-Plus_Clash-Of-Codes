from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__,
            static_url_path='', 
            static_folder='public')
# app = Flask(__name__)
CORS(app, origins="*", supports_credentials=False)

# app.register_blueprint(cluster_routes.cluster_bp, url_prefix='/api/v1/cluster')
# app.register_blueprint(users_routes.users_bp, url_prefix='/api/v1/user')

app.run(port=os.environ["PORT"], debug=True)
