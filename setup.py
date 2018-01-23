from setuptools import setup

setup(
    name='pytest-gc',
    description='The garbage collector plugin for py.test',
    license='MIT license',
    version='0.0.1',
    author='Victor Titor',
    url='https://github.com/vtitor/pytest-gc',
    py_modules=['pytest_gc'],
    entry_points={'pytest11': ['gc = pytest_gc']},
    install_requires=['pytest'],
    tests_require=['pytest'],
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
)
