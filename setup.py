from distutils.core import setup

setup(
    # Application name:
    name="flask_puppet",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Matt Cadorette",
    author_email="mattc@puppet.com",

    # Packages
    packages=["webui"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/ipcrm/flask_puppet"

    #
    description="Example App",

    # Dependent packages (distributions)
    install_requires=[
      alembic==0.7.7
      blinker==1.4
      Flask==0.10.1
      Flask-Alembic==1.2.1
      Flask-Login==0.3.0
      Flask-Mail==0.9.1
      Flask-Principal==0.4.0
      Flask-Security==1.7.4
      Flask-SQLAlchemy==2.0
      Flask-Testing==0.4.2
      Flask-WTF==0.12
      Flask-Zurb-Foundation==0.2.1
      itsdangerous==0.24
      Jinja2==2.8
      Mako==1.0.2
      MarkupSafe==0.23
      passlib==1.6.5
      psycopg2==2.6.1
      SQLAlchemy==1.0.8
      Werkzeug==0.10.4
      WTForms==2.0.2
    ],
)
