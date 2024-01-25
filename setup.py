from setuptools import setup, find_packages

setup(
    name='ablv_classifier',
    
    version='1.0.0',
    packages=find_packages(where="ablv_classifier"),
    package_dir={"": "ablv_classifier"},
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