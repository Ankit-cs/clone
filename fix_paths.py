import json
import glob

replacements = {
    "'/content/hotel_bookings.csv'": "'../data/raw/hotel_bookings.csv'",
    "\"hotel_bookings_clean.csv\"": "'../data/processed/hotel_bookings_clean.csv'",
    "'../data/hotel_bookings.csv'": "'../data/raw/hotel_bookings.csv'",
    "\"hotel_bookings.csv\"": "'../data/raw/hotel_bookings.csv'"
}

for nb_path in glob.glob("notebooks/*.ipynb"):
    with open(nb_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(nb_path, "w", encoding="utf-8") as f:
        f.write(content)
print("Paths fixed!")
