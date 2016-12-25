from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_apache_service(Service):
    service = Service('apache2')
    assert service.is_running
    assert service.is_enabled


def test_apache_utils(Command):
    assert Command('which htpasswd').rc == 0


def test_apache_modules(Command, Sudo):
    with Sudo():
        assert 'negotiation' in Command('a2query -m').stdout


def test_apache_config(Command, Sudo):
    with Sudo():
        assert 'Syntax OK' in Command('apache2ctl configtest').stderr


def test_apache_status(Command):
    assert 'Apache Server Status for' in Command(
        'curl http://localhost/status').stdout
