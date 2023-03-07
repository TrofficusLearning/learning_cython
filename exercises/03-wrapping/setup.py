from distutils.core import setup, Extension
from Cython.Build import cythonize

ld = Extension(name="levenshtein_cython",
               sources=["levenshtein_cython.pyx", "levenshtein.c"]
               )

setup(ext_modules=cythonize(ld))
