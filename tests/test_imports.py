import importlib

# List of core dependencies to test for successful import
DEPENDENCIES = [
    'transformers',
    'langchain',
    'bs4',
    'scrapy',
    'mlflow',
    'docker',
    'streamlit',
    'pandas',
    'numpy',
    'sklearn',
    'requests'
]


def test_imports():
    """Ensure core dependencies can be imported."""
    for package in DEPENDENCIES:
        assert importlib.import_module(package) is not None
