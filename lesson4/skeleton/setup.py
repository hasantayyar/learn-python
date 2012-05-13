try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'Learn Python',
    'author': 'John Doe',
    'url': 'http://python.org',
    'download_url': 'http://www.python.org/',
    'author_email': 'tayyar.besik@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'learnpython'
}

setup(**config)
