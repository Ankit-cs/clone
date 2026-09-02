import json
import os
import base64

notebook_path = r"c:\mlProject\anurag\Hotel-Booking-Analytics-and-Cancellation-Prediction-\notebooks\EDA.ipynb"
images_dir = r"c:\mlProject\anurag\Hotel-Booking-Analytics-and-Cancellation-Prediction-\images"

os.makedirs(images_dir, exist_ok=True)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

img_count = 0
for cell in nb.get('cells', []):
    if cell['cell_type'] == 'code':
        for output in cell.get('outputs', []):
            if 'data' in output and 'image/png' in output['data']:
                img_data = output['data']['image/png']
                
                # Write base64 to png file
                img_path = os.path.join(images_dir, f"eda_graph_{img_count}.png")
                with open(img_path, "wb") as img_file:
                    img_file.write(base64.b64decode(img_data))
                    
                img_count += 1

print(f"Extracted {img_count} images to {images_dir}")
