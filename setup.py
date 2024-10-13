from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cadnano2',
    version='2.3',
    description='Cadnano2 for PyQt5',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mtaku3/cadnano2',
    author='mtaku3',
    license='MIT',
    packages=['cadnano2'],
    package_data={'cadnano': ['ui/mainwindow/images/*.svg', 'ui/mainwindow/images/*.png']},
    install_requires=['PyQt5'],
    entry_points = {'console_scripts': ['cadnano2 = cadnano2.main:main']},
)

