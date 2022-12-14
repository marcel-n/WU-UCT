from setuptools import find_packages, setup

VERSION = '0.0.0.dev'


info = dict(
    name='wu-uct',
    version=VERSION,

    packages=find_packages('.', exclude=('Results', 'OutLogs', 'Logs', 'Figures')),
    # package_dir={'': 'src'},

    # install_requires=(
    #     'gym',
    #     'numpy',
    #     'torch', 
    #     'torchvision', 
    #     'torchaudio',
    # ),

    python_requires='>= 3.9'
)

setup(**info)