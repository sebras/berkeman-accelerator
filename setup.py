from distutils.core import setup, Extension

gzlinesmodule = Extension("gzlines", sources = ["gzlinesmodule.c"], libraries=["z"])

setup(name="gzlines", version="1.8.0", description="Read/write values from/to gz files", ext_modules=[gzlinesmodule])
