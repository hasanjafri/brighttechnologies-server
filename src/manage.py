from flask_script import Manager

from app import create_app

manager = Manager()

@manager.command
def run():
    """ Starts the server on port 8000 """
    create_app()