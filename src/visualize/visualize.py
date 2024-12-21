import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(fields, filename, chart_type='bar'):
    try:
        data = pd.read_csv(filename) if filename.endswith('.csv') else pd.read_json(filename)
        
        # Here we're focusing on Matplotlib for simplicity. Plotly.js and D3.js would be for web interfaces.
        if chart_type == 'bar':
            for field in fields:
                data[field].value_counts().sort_index().plot(kind='bar')
                plt.title(f'Bar Chart for {field}')
                plt.show()
        # Add more chart types here as needed
        
    except Exception as e:
        print(f"Error visualizing data: {str(e)}")