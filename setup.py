from setuptools import setup, find_packages

setup(
    name='mirak_doc_processing',
    version='0.1.0',
    packages=find_packages(where='app'),
    install_requires=[
        'transformers',
        'psycopg2-binary',
        'python-dotenv',
        'pillow',
        'pytesseract',
    ],
) 