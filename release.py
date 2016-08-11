import itertools
import os
import tarfile
import yaml

from microdrop_utility import Version
import path_helpers as ph

package_name = 'microdrop_plugin_template'
plugin_name = 'wheelerlab.microdrop_plugin_template'

# create a version sting based on the git revision/branch
version = str(Version.from_git_repository())

# write the 'properties.yml' file
properties = {'plugin_name': plugin_name, 'package_name': package_name,
              'version': version}
with open('properties.yml', 'w') as f:
    f.write(yaml.dump(properties))

# create the tar.gz plugin archive
with tarfile.open("%s-%s.tar.gz" % (package_name, version), "w:gz") as tar:
    current_dir = os.getcwd()
    try:
        os.chdir(package_name)

        here = ph.path('.')
        for path_i in itertools.chain(here.files('*.py'),
                                      map(ph.path, ['properties.yml', 'hooks',
                                                    'requirements.txt'])):
            if path_i.exists():
                tar.add(str(here.relpathto(path_i)))
    finally:
        os.chdir(current_dir)
