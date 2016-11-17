Apache
######

Provision Apache with minimal common configuration (just package installation
and copy configuration templates, if any). Templates can be placed inside
:code:`templates/apache/conf-enabled` and :code:`templates/apache/sites-enabled`
(for configuration and virtualhosts respectibily) either relative to the
playbook or inside the role. The rational is to have the bare minimum of
configuration in the role and use user-provided templates to extend the role in
a way that's best for the user. Therefore configuration such as XSS, OCSP or
even SSL that is not always relevant is outside the scopre of this role.

Requirements
------------

See :code:`meta/main.yml`, :code:`tests/requirements.yml` and assertions at
the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Virtualbox and Vagrant and Python 2.7. Install the Python
dependencies, add pre-commit hooks by running:

.. code:: shell

    pip install -r tests/requirements.txt
    pre-commit install

To run the full test suite:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule test --platform all
    pre-commit run --all-files

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.

TODO
----

- Server health.
- Limit requests
  (https://httpd.apache.org/docs/current/misc/security_tips.html#dos and
  https://httpd.apache.org/docs/current/server-wide.html#resource).
