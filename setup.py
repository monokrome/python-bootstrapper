import setuptools

# TODO: Rename `project_module` and adjust these line to import the new name
import project_module as project
from project_module import __main__


# setup.cfg is a new-ish standard, so we need to check this for now
if int(setuptools.__version__.split('.', 1)[0]) < 38:
    raise EnvironmentError(
        'Please upgrade setuptools. This package uses setup.cfg, which requires '
        'setuptools version 38 or higher. If you use pip, for instance, you can '
        'upgrade easily with ` pip install -U setuptools `'
    )


# Defines a few pieces of metadata here. We could use attr: in setup.cfg for
# most of these, but it  is cleaner to keep anything that refers to the module
# in here because it means we need to change less if we decide to rename our
# module. setup.cfg also - for some peculiar reason - doesn't let you use
# `attr:` syntax on `name` or console scripts even though it seems to work
# nearly everywhere else.

setuptools.setup(
    description=project.short_description(),
    long_description=project.long_description(),
    name=project.name(),
    version=project.version_string(),

    entry_points={
        'console_scripts': getattr(__main__, 'console_scripts', list)(),
    }
)
