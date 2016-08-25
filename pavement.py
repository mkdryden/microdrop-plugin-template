import sys

from paver.easy import task, needs, path
from paver.setuputils import setup, install_distutils_tasks

sys.path.insert(0, path('.').abspath())
import version

setup(name='microdrop-plugin-template',
      version=version.getVersion(),
      description='Microdrop plugin template',
      keywords='',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='https://github.com/wheeler-microfluidics/microdrop-plugin-template',
      license='GPL',
      packages=['microdrop_plugin_template'],
      install_requires=['microdrop-plugin-manager', 'path-helpers',
                        'pip-helpers>=0.5.post8', 'rename-package-files'],
      # Install data listed in `MANIFEST.in`
      include_package_data=True)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
