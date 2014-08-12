from setuptools import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='weather',
    version='0.1',
    packages=['weather'],
    author='',
    author_email='',
    url='https://github.com/hamperbot/weather',
    install_requires=requirements,
    package_data={'weather': ['requirements.txt', 'README.md', 'LICENSE']}
)
