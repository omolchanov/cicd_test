from setuptools import setup, find_packages

setup(
    name='CICDTest',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List dependencies here, e.g., "numpy", "requests"
    ],
    entry_points={
        'console_scripts': [
            'cli=main:main',  # Optional command-line entry point
        ]
    },
)