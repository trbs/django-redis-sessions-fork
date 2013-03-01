from setuptools import setup
from redis_sessions import __version__


# no with statement for python 2.5
def long_description():
    f = open('README.rst')
    rst = f.read()
    f.close()
    return rst


packages = ['redis_sessions']


setup(
    name='django-redis-sessions-fork',
    version=__version__,
    description="Redis Session Backend For Django",
    long_description=long_description(),
    keywords='django, sessions,',
    author='Martin Rusev',
    author_email='hellysmile@gmail.com',
    url='http://pypi.python.org/pypi/django-redis-sessions-fork',
    license='BSD',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=2.4.10'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
