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

package_dir = ph.path(package_name)

properties_path = package_dir.joinpath('properties.yml')
with properties_path.open('w') as f:
    f.write(yaml.dump(properties))
    print 'Wrote: {}'.format(properties_path)

# Create the tar.gz plugin archive
tar_path = "%s-%s.tar.gz" % (package_name, version)
with tarfile.open(tar_path, "w:gz") as tar:
    current_dir = os.getcwd()
    try:
        os.chdir(package_name)

        here = ph.path('.')
        for path_i in itertools.chain(here.files('*.py'),
                                      map(ph.path, ['properties.yml', 'hooks',
                                                    'requirements.txt'])):
            if path_i.exists():
                tar.add(str(here.relpathto(path_i)))
        print 'Wrote: {}'.format(tar_path)
    finally:
        os.chdir(current_dir)
