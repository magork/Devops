########
10. TODO
########

======
Task 1
======

Create a script ``wikipython.py`` that:

    - reads a Wikipedia page: ``https://en.wikipedia.org/wiki/Python_(genus)`` (use requests command)
    - extracts Species elements - python name (what kind of pythons are there) (use BeautifulSoup)
    - save the output the to a new file
    - append to the new file the last line that is the count of species

.. code-block:: python
    
    import requests
    from bs4 import BeautifulSoup

    page = requests.get('https://en.wikipedia.org/wiki/Python_(genus)')

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find("table")

======
Task 2 
======

Create script weather that gives you the weather from ``curl`` https://wttr.in/(location)

    - the location will be read from the keyboard - for example ``weather Bucharest``
    - a test that you have the location

======
Task 3
======

Create a health check script ``healthCheck`` that looks at:

    - date and time ``import datetime``
    - the uptime of the machine using ``uptime``
    - how much disk ``df`` and memory usage ``free`` ``import psutil``