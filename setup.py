from setuptools import setup, find_packages

setup(
    name='CICDTest_omolchanov',
    version='0.1.1',
    license='MIT',
    packages=find_packages(),  # No 'where' needed
    description='Short description',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cli=cicdtest_omolchanov.main:main',
        ]
    },
)
