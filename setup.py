from setuptools import setup, find_packages

setup(
    name="bible-summary",
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'bible_summary': ['data/*.json'],
    },
    description="A package for summarizing Bible books",
    author="Riki Morohashi",
    author_email="rikimorohashi@gmail.com",
    url="https://rikim.me/docs/bible-summary/",
    long_description=open('README.md', 'r').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bible-summary=bible_summary.summary:main',
        ],
    },
)
