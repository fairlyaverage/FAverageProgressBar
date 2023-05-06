from setuptools import find_packages, setup

setup(
    name='FAverageProgressBar',
    packages=find_packages(include=['FAverageProgressBar']),
    version='0.1.0',
    description='Librarification of a fairly average progress bar used to track and predict runtimes for Python loops, and displaying that information on a single line(s) in console accompanying a unicode-stylized progress indicator',
    author='fairlyaverage',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
