from setuptools import setup, find_packages

setup(
    name='fdnpy',
    version='0.2.0',
    description='A Python SDK for FinancialData.Net API',
    url='https://github.com/financialdatanet/fdnpy',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
    ],
)