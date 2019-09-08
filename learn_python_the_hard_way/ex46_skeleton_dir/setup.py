try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Hassan',
    'url': 'url_here',
    'download': 'download_from_here',
    'author_email': 'privacy_for_now',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'my_project'
}

setup(**config)
