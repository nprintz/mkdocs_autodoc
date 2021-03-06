The `mkdocs._autodoc` extension will allow you to dynamically generate API documentation from your
Python modules and classes within the [mkdocs](https://github.com/tomchristie/mkdocs) project.

Installation
-------------

You can install the `mkdocs_autodoc` package using `pip` or `easy_install`

    $ pip install mkdocs_autodoc
    $ easy_install mkdocs_autodoc

Dynamic Generation
--------------

To have the content always generated dynamically, without the use of any markdown files, you can use the
`autodoc` page command.  This will allow you to dynamically insert a python module into the page hierarchy
at runtime.

You will need to modify your `mkdocs.yml` to include something similar to:

    mkdocs_extensions:
        - mkdocs_autodoc
    pages:
        - ['api/autodoc:mkdocs', 'API', 'mkdocs']

When this syntax is invoked on load, the `mkdocs` module will be loaded and all of its pages dynamically generated
and added to the server.  This option is nice because you will always get your latest documentation, however, if
you use this remotely you will need to configure a [virtualenv](https://pypi.python.org/pypi/virtualenv) that can load your package.

Markdown Generate
----------------

The second option is to statically build your API documentation as Markdown files that can be loaded anywhere.
This exists as a command-line extension to the `mkdocs` commands, and works similarly, except instead of generating
dynamic HTML content, it will export out *.md files to your documents root.  This method will also require
use of the [mkdocs_tree](https://github.com/erichulser/mkdocs_tree) extension.

You will need to call this whenever you want to re-generate your API documentation, however it will not need access
to your code libraries on remote servers.

You will need to modify your `mkdocs.yml` file to include something simliar to:

    mkdocs_extensions:
        - mkdocs_tree
        - mkdocs_autodoc
    pages:
        - ['tree:api/mkdocs', 'API', 'mkdocs']

To use this, you will need to invoke the command from the command line:

    $> mkdocs autodoc-generate mkdocs

You can specify `--outpath=/path/to/output` which will default to `docs/api` as well as `--basepath=/path/to/base`
which will be the page's base path (defaulting to `api`).

__WARNING: This will *remove* the `outpath` before building, so you should always only keep autogenerated docs in it.__
