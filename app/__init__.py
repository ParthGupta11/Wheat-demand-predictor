from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '2bd1295a67a0ef62e2a91ae5331a4cdb'


from app import routes
