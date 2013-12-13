from IsirPythonTools import *

package_name = 'xde_resources'

setup(name='XDE-Resources',
	  version='0.1',
	  description='Urdf & Collada files that are used by XDE-ISIR, but can also be used by other applications',
	  author='Soseph',
	  author_email='hak@isir.upmc.fr',
	  package_dir={package_name:'src'},
	  packages=[package_name],
	  package_data={package_name: ['resources/urdf/*.dae', 'resources/urdf/lwr/*.dae', 'resources/urdf/*.xml']},
	  cmdclass=cmdclass,

	  script_name=script_name,
	  script_args= script_args
	 )
