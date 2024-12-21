# src/query.py

import pandas as pd
from chardet import detect

def detect_encoding_and_query(filename, condition):
    # Encoding detection logic (as per our previous setup)
    try:
        with open(filename, 'rb') as file:
            raw_data = file.read()
            result = detect(raw_data)
            detected_encoding = result['encoding']
            confidence = result['confidence']
            print(f"Detected encoding: {detected_encoding} with confidence {confidence}")

        if confidence > 0.7:
            data = load_data(filename, detected_encoding)
        else:
            data = attempt_common_encodings(filename)
        
        return apply_query(data, condition)
    except Exception as e:
        print(f"Error querying data: {str(e)}")
        return None

def load_data(filename, encoding):
    if filename.endswith('.csv'):
        return pd.read_csv(filename, encoding=encoding)
    elif filename.endswith('.json'):
        return pd.read_json(filename)
    else:
        raise ValueError(f"Unsupported file type for {filename}")

def attempt_common_encodings(filename):
    common_encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'windows-1252', 'iso-8859-1']
    for encoding in common_encodings:
        try:
            return load_data(filename, encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError("Could not determine the correct encoding for the file.")

def apply_query(data, condition):
    # Simple query parsing for now, expand to handle complex conditions
    conditions = condition.split(' AND ')
    result = data
    
    for cond in conditions:
        column, op, value = cond.replace('>', ' > ').replace('<', ' < ').replace('>=', ' >= ').replace('<=', ' <= ').split()
        value = float(value) if '.' in value else int(value)
        
        if op == '>':
            result = result[result[column] > value]
        elif op == '<':
            result = result[result[column] < value]
        elif op == '>=':
            result = result[result[column] >= value]
        elif op == '<=':
            result = result[result[column] <= value]
        else:
            result = result[result[column] == value]
    
    print(result.head())  # Display a portion of the results
    return result