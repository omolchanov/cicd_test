from setuptools import setup, find_packages

setup(
    name='ci_cd_test_omolchanov',
    version='0.1.7',
    py_modules=['main'],
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='Short description',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my_app_test = ci_cd_test_omolchanov.main:main',
        ]
    }
)
