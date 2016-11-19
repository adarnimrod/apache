def test_apache_service(Service):
    service = Service('apache2')
    assert service.is_running
    assert service.is_enabled


def test_apache_utils(Command):
    assert Command('which htpasswd').rc == 0


def test_apache_modules(Command, Sudo):
    with Sudo():
        assert 'negotiation' in Command('a2query -m').stdout


def test_apache_ssl_group(User, Group):
    if Group('ssl-cert').exists:
        assert 'ssl-cert' in User('www-data').groups


def test_apache_config(Command, Sudo):
    with Sudo():
        assert 'Syntax OK' in Command('apache2ctl configtest').stderr


def test_apache_status(Command):
    assert 'Apache Server Status for' in Command(
        'wget http://localhost/status -qO -').stdout
