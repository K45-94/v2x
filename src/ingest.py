import pandas as pd

def ingest_data(filename):
    try:
        if filename.endswith('.csv'):
            data = pd.read_csv(filename)
        elif filename.endswith('.json'):
            data = pd.read_json(filename)
        else:
            raise ValueError(f"Unsupported file type for {filename}")
        
        # You might want to save this data or process it further here
        print(f"Data from {filename} ingested successfully.")
        return data
    except Exception as e:
        print(f"Error ingesting data: {str(e)}")