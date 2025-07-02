from setuptools import setup, find_packages

setup(
    name='mirlab',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,  # Important to include non-py files
    package_data={
        'mirlab': ['menu.tcss'],
    },
    install_requires=[
        'librosa',
        'matplotlib',
        'numpy',
        'scipy',
        'textual',
    ],
    entry_points={
        'console_scripts': [
            'mirlab = mirlab.launcher:main',
        ],
    },
    author='Luca Spanedda',
    description='Audio analysis TUI tool',
    url='https://github.com/LucaSpanedda/mirlab',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
