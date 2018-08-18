""" Provides a simple starter module for creating new Python projects.

You can use this project to create new modules quickly. The process for
creating a new module is to simply fork this project, rename the
*project_module* package, change it's content to and explain your project by
replacing any current documentation.

TODO: This docstring should be in standard PEP8 style, with a short description
of the module on the first line as seen above. The short line should be
followed by a long-form description of your module similar to the one which you
are currently reading.

"""

__all__ = (
    '__version__',
    'version',
    'prjoect_name',
)


__version__ = (0, 0, 0, 'alpha')


def version_string(version=__version__):
    """ Provides the version string for this project """

    version_string = '.'.join(map(str, version[:3]))

    if len(version) > 3:
        version_string += '-' + '-'.join(version[3:])

    return version_string


def name():
    """ Provides a user-friendly name of the projec.t

    This can be used to get the name wherever it may be useful. One example
    case is that this is used to determine the name of the package in the
    Python package index. This is defined as a function so that the behavior
    can be easily overridden if necessary, but usually can remain as is.
    
    """

    return __name__


def long_description(content=' '.join(__doc__.split('\n')[1:])):
    """ Provides a human-readable description for this project """

    return content


def short_description():
    """ Provides a summarized project desription """

    return long_description(content=__doc__.split('\n', 1)[0])
