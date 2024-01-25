from setuptools import setup, find_packages

setup(
    name='ablv_classifier',
    version='1.0.0',
    packages=find_packages(),
    package_data={'ablv_classifier': ['*','data/v1/entity_list.csv', 'data/v1/type_mapping.csv']},
    include_package_data=True,
    install_requires=[
        'presidio_analyzer',
        'presidio_anonymizer',
        'pandas',
        "scikit-learn",
        "sentence_transformers",
        "numpy",
    ]
)