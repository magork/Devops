#########################
4. Libraries and modules
#########################

A Python library is a collection of related modules, contains code that can be reused in different programs.

Using libraries 
----------------

.. code-block:: python
    
    import datetime
 
    today = datetime.datetime.today()
    print(f"{today:%B %d, %Y}")