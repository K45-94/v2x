import pandas as pd

def query_data(filename, condition):
    try:
        # Load the data
        if filename.endswith('.csv'):
            data = pd.read_csv(filename)
        elif filename.endswith('.json'):
            data = pd.read_json(filename)
        else:
            raise ValueError(f"Unsupported file type for {filename}")
        
        # Simple query syntax parsing (this is very basic and needs expansion for real use)
        column, op, value = condition.replace('>', ' > ').replace('<', ' < ').split()
        value = float(value) if '.' in value else int(value)
        
        # Apply the query
        if op == '>':
            result = data[data[column] > value]
        elif op == '<':
            result = data[data[column] < value]
        else:
            result = data[data[column] == value]
        
        print(result.head())  # Display a portion of the results
        return result
    except Exception as e:
        print(f"Error querying data: {str(e)}")