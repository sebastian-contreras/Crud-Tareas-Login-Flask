from app import create_app
from flask_script import Manager, Shell
from app import db,User,Task
from config import config



config_class = config['development']

app = create_app(config_class)

def make_shell_context():
    return dict(app = app,db=db,User=User,Task=Task)


if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('shell',Shell(make_context=make_shell_context))
    @manager.command
    def test():
        import unittest
        tests = unittest.TestLoader().discover('app/tests')
        unittest.TextTestRunner().run(tests)

    manager.run()