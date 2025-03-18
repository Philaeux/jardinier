FastAPI
========

Periodic Tasks
---------------

It's possible to create periodic tasks. Use this function decorator:
    
.. autofunction:: templates.utils.repeat_every.repeat_every

And then call this function in the lifespan function.

GraphQL
--------

Schema
^^^^^^^

Schema defined for the GraphQL endpoint:

.. automodule:: templates.graphql.schema
    :members:

Types Input & Output
^^^^^^^^^^^^^^^^^^^^^^

I recommend creating files to store Input and Output types of the GraphQL endpoints, in files like ``src/template/graphql/types/a.py``.

These types are used:

.. automodule:: templates.graphql.types.generic
    :members:


Generated Types
^^^^^^^^^^^^^^^^

These types are generated from ORM objects. When a query/mutation return an ORM type, it's automatically turned into a GraphQL type.

.. automodule:: templates.graphql.types.generated
    :members:

REST API
----------

It is possible to create classic REST endpoints instead of using the GraphQL endpoint. A demonstration function is the hello_world.

I recommend using REST for the OAuth process, using 2 functions ``oauth_login`` and ``oauth_callback`` per provider (Google, Reddit...).
