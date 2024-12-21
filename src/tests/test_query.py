import pytest
from src.query.query import query_data
import pandas as pd
import os

@pytest.fixture
def sample_csv():
    sample_data = {'Age': [25, 30, 45, 60], 'Salary': [50000, 60000, 70000, 80000]}
    df = pd.DataFrame(sample_data)
    df.to_csv('sample.csv', index=False)
    yield 'sample.csv'
    os.remove('sample.csv')

def test_query_age_greater_than(sample_csv):
    result = query_data(sample_csv, 'Age > 45')
    assert len(result) == 1
    assert result['Age'].iloc[0] == 60

def test_query_age_less_than(sample_csv):
    result = query_data(sample_csv, 'Age < 30')
    assert len(result) == 1
    assert result['Age'].iloc[0] == 25