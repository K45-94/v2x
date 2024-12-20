import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result

file_path = 'data/sample.csv'
encoding_info = detect_encoding(file_path)
print(f"Detected encoding: {encoding_info['encoding']}")