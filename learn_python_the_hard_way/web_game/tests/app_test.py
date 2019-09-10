import nose.tools as nt
from gothonweb.app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    nt.assert_equal(rv.status_code, 200)
