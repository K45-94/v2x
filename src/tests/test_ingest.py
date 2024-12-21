import pytest
from src.ingest.ingest import ingest_data
import pandas as pd
import os

@pytest.fixture
def sample_csv():
    sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(sample_data)
    df.to_csv('sample.csv', index=False)
    yield 'sample.csv'
    os.remove('sample.csv')  # Clean up after test

@pytest.fixture
def sample_json():
    sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(sample_data)
    df.to_json('sample.json', orient='records')
    yield 'sample.json'
    os.remove('sample.json')  # Clean up after test

def test_ingest_csv(sample_csv):
    result = ingest_data(sample_csv)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3

def test_ingest_json(sample_json):
    result = ingest_data(sample_json)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3

def test_ingest_unsupported():
    with pytest.raises(ValueError):
        ingest_data('unsupported_file.xyz')