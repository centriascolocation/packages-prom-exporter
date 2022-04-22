import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='packages-prom-exporter'',
    version='0.0.1',
    packages=[''],
    url='https://github.com/centriascolocation/packages-prom-exporter.git',
    license='Apache License 2.0',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Dirk Piethan',
    author_email='dirk@centrias.de',
    description='Prometheus exporter for available linux package updates',
    install_requires=[
        'prometheus_client',
        'apscheduler',
    ],
    scripts=[
        'packages-prom-exporter'
    ]
)