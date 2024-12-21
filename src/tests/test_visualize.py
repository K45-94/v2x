import pytest
from src.visualize.visualize import visualize_data
import pandas as pd
import os

@pytest.fixture
def sample_csv():
    sample_data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
    df = pd.DataFrame(sample_data)
    df.to_csv('sample.csv', index=False)
    yield 'sample.csv'
    os.remove('sample.csv')

def test_visualize_bar_chart(sample_csv, monkeypatch):
    # Mocking plt.show since it's not testable in an automated environment
    def mock_show(*args, **kwargs):
        pass
    monkeypatch.setattr('matplotlib.pyplot.show', mock_show)
    
    visualize_data(['Category'], sample_csv, chart_type='bar')
    # Here we're just checking if the function runs without error. 
    # Real visualization would need manual inspection or screenshot comparison.