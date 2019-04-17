from setuptools import setup

setup(
    name='youtube',
    version='0.0.1',
    packages=['youtube'],
    url='',
    license='Private',
    author='Kryštof Tulinger',
    author_email='k.tulinger@seznam.cz',
    description='Youtube test tool',
    keywords="youtube",
    package_data={
        'youtube': [
            'youtube.auth.cfg.sample',
        ]
    },
    install_requires=[
        'click',
        'requests',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'betamax'
    ],
    zip_safe=False
)
