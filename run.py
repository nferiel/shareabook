import os



app = create_app(os.getenv('FLASK_CONFIG') or 'default')
