ansible-apache
##############

An Ansible role to install and configure Apache2 on Debian Jessie or later.

Requirements
------------

Debian Jessie.
SSL certificate (the self-signed snakeoil cert is valid).

Role Variables
--------------
::

    apache_ocsp_server:

Dependencies
------------

`Common role <https://www.shore.co.il/cgit/ansible-common/>`_

Example Playbook
----------------
::

    - hosts: servers
      roles:
      - role: apache
        apache_ocsp_server: https://ocsp.ca.com/

License
-------

This software is licnesed under the MIT licese (see the ``LICENSE.txt`` file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/cgit/.

TODO
----

- Server health.
- OCSP.
- Collectd metrics.
- Log to syslog.
- Limit requests
  (https://httpd.apache.org/docs/current/misc/security_tips.html#dos and
  https://httpd.apache.org/docs/current/server-wide.html#resource).
- Disable .htaccess
  (https://httpd.apache.org/docs/current/misc/security_tips.html#systemsettings).
- Assertions.
- Wait for server to come online.
