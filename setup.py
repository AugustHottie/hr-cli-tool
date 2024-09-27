from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
  readme = f.read()

setup(
    name='hr-cli-tool',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='augusthottie',
    author_email='myaugusthottie@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)