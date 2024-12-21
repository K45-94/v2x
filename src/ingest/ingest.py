import pandas as pd

def ingest_data(filename):
    try:
        data = pd.read_csv(filename, encoding='utf-8-sig')  # Try 'utf-8-sig' for BOM issues
        print(data.head())
        print(f"Data from {filename} ingested successfully.")
        return data
    except UnicodeDecodeError as e:
        print(f"Error ingesting data: {e}")
    except Exception as e:
        print(f"Error ingesting data: {str(e)}")