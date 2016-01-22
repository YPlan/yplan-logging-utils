===================
yplan-logging-utils
===================

.. image:: https://img.shields.io/pypi/v/yplan-logging-utils.svg
        :target: https://pypi.python.org/pypi/yplan-logging-utils

.. image:: https://img.shields.io/travis/YPlan/yplan-logging-utils.svg
        :target: https://travis-ci.org/YPlan/yplan-logging-utils

Utilities we use for logging throughout our projects.

* Free software: ISC license

Features
--------

* ``PlainJSONFormatter`` - a formatter that turns logging records into ``dict``s in our (somewhat in-house) format.
  Note it returns a ``dict`` which is somewhat non-standard but compatible with the ``fluent-logger`` package.
* ``JSONFormatter`` - a subclass of the above that does ``json.dumps`` so you get the stringified version of the
  dictionary.
