from setuptools import setup, find_packages

setup(
    name='CICDTest_omolchanov',
    version='0.1.3',
    py_modules=['main'],
    license='MIT',
    package_dir={'': 'src'},
    description='Short description',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cicd = main:main',
        ]
    }
)
