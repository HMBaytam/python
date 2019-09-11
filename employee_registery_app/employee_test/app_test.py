from nose.tools import *
from employee.app import app

app.config['TESTING'] = True
web = app.test_client()


def index_test():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)


def index_post_test():
    pass
