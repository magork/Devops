#################
2. What is sphinx 
#################

======
Sphinx
======

It's a parser written in python that allows us to write ``rst`` or ``md`` files that will be compiled into ``html``, ``ePub`` or ``LaTeX``.

.. image:: ../diagrams/sphinx.drawio.png

.. note::

    Sphinx makes it easy to create intelligent and beautiful documentation.

Here are some of Sphinx's major features:

    #. Output formats: HTML (including Windows HTML Help), LaTeX (for printable PDF versions), ePub, Texinfo, manual pages, plain text.
    #. Extensive cross-references: semantic markup and automatic links for functions, classes, citations, glossary terms, and similar pieces of information
    #. Hierarchical structure: easy definition of a document tree, with automatic links to siblings, parents, and children
    #. Automatic indices: general index as well as a language-specific module indices
    #. Code handling: automatic highlighting using the Pygments highlighter
    #. Extensions: automatic testing of code snippets, the inclusion of docstrings from Python modules (API docs) via built-in extensions, and much more functionality via third-party extensions.
    #. Themes: modify the look and feel of outputs by creating themes, and reusing many third-party themes.
    #. Contributed extensions: dozens of extensions contributed by users; most of them installable from PyPI.
    #. Sphinx uses the reStructuredText markup language by default and can read MyST markdown via third-party extensions. Both of these are powerful and straightforward to use and have functionality for complex documentation and publishing workflows. They both build upon Docutils to parse and write documents.