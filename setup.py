from setuptools import setup, find_packages

setup(
    name='mirlab',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'librosa',
        'numpy',
        'matplotlib',
        'textual',
    ],
    entry_points={
        'console_scripts': [
            'mirlab = mirlab.launcher:main',
        ],
    },
)
