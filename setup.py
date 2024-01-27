from setuptools import setup, Extension
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('cython')
install('numpy')

from Cython.Build import cythonize
import numpy


package = Extension('widerface_eval.bbox', ['box_overlaps.pyx'], include_dirs=[numpy.get_include()])
setup(
    name='widerface-eval',
    version='1.0',
    description='Evaluation code for WIDER FACE',
    ext_modules=cythonize(package),
    package_dir={'widerface_eval': ''},
    py_modules=['widerface_eval.evaluation'],
    install_requires=[
        'Cython',
        'numpy',
        'scipy',
        'argparse',
        'tqdm',
    ],
)
