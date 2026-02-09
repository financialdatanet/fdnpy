from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='fdnpy',
    version='0.3.0',
    description='A Python SDK for FinancialData.Net API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/financialdatanet/fdnpy',
    author='FinancialData.Net',
    packages=find_packages(),
    classifiers=[
        'Topic :: Office/Business :: Financial :: Investment',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
    ],
    keywords=[
        'python', 'api', 'finance', 'stock-market', 'algotrading', 'quant', 'quantitative-finance',
        'stock-data', 'stock-prices', 'financial-data', 'algorithmic-trading', 'quantitative-trading',
        'financial-markets', 'stock-trading', 'stock-api', 'financial-modeling', 'investing-api',
        'stock-market-api', 'financial-data-api'
    ],
    project_urls={
        'Homepage': 'https://financialdata.net/',
        'Documentation': 'https://github.com/financialdatanet/fdnpy/blob/main/README.md',
        'Source': 'https://github.com/financialdatanet/fdnpy'
    }
)