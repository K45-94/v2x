import pandas as pd

def query_data(filename, condition):
    try:
        # Load the data
        if filename.endswith('.csv'):
            data = pd.read_csv(filename, encoding='utf-8-sig')  # Try 'utf-8-sig' for BOM issues
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
    except UnicodeDecodeError as e:
        print(f"Error querying data: {e}")
    except Exception as e:
        print(f"Error querying data: {str(e)}")