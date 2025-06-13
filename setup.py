from setuptools import setup, find_packages

setup(
    name='CICDTest',
    version='0.1.0',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='Short description',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        # List dependencies here, e.g., "numpy", "requests"
    ],

    entry_points={
        'console_scripts': [
            'cli=main:main',  # Optional command-line entry point
        ]
    },
)