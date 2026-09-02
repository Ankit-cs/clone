import json
import os
import base64

notebook_path = r"c:\mlProject\anurag\Hotel-Booking-Analytics-and-Cancellation-Prediction-\notebooks\EDA.ipynb"
images_dir = r"c:\mlProject\anurag\Hotel-Booking-Analytics-and-Cancellation-Prediction-\images"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

img_count = 0
for cell in nb.get('cells', []):
    if cell['cell_type'] == 'code':
        for output in cell.get('outputs', []):
            if 'data' in output and 'image/png' in output['data']:
                img_count += 1

print(f"Found {img_count} images in EDA.ipynb")
