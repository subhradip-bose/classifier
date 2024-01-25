from setuptools import setup, find_packages

setup(
    name='ablv_classifier',
    include_package_data=True,
    version='1.0.0',
    packages=find_packages(include=['ablv_classifier', 'ablv_classifier.*']),
    install_requires=[
        'presidio_analyzer',
        'presidio_anonymizer',
        'pandas',
        "scikit-learn",
        "sentence_transformers",
        "numpy",

    ]
)