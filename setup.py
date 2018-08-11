from setuptools import setup

setup(
    # Application name:
    name='flaskr',
 
    # Version number (initial):
    version="0.1.0",

    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_migrate',
        'flask_sqlalchemy',
        'flask_restplus',
        'flask_login'
    ],
)