import os

main_readme = r"c:\mlProject\anurag\Hotel-Booking-Analytics-and-Cancellation-Prediction-\README.md"
pp_readme = r"c:\mlProject\anurag\pp\Hotel-Booking-Analytics-and-Cancellation-Prediction-\README.md"

with open(main_readme, "r", encoding="utf-8") as f:
    main_lines = f.readlines()

with open(pp_readme, "r", encoding="utf-8") as f:
    pp_lines = f.readlines()

# Keep lines 0 to 15 (up to "The project combines:") from main README
new_readme = main_lines[:15] + pp_lines[14:]

with open(main_readme, "w", encoding="utf-8") as f:
    f.writelines(new_readme)

print("README.md updated successfully.")
