Apache
######
.. image:: https://travis-ci.org/adarnimrod/apache.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/apache

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

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

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

Testing requires Python 2.7, Tox, Vagrant and Virtualbox. To test simply run
:code:`tox`. `Pre-commit <http://pre-commit.com/>`_ is also setup for this
project.

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore/.
