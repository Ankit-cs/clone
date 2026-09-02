# Hotel Booking Analytics and Cancellation Prediction

## Machine Learning Practical Assignment

**Student Information:**
- **Name:** Anurag
- **Roll No:** CSJMA23001390009
- **Contribution:** Full implementation of data preprocessing, from-scratch feature selection, and EDA.

---

##  Project Overview

This ML project develops a data-driven decision-support system for hotel booking analytics.

The project combines:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Business Insights and Recommendations

The objective is to analyze historical hotel booking data, identify important cancellation patterns, and produce a final ML-ready dataset.

---

##  Project Objectives

The main objectives of the project are:

1. Clean and prepare the hotel booking dataset.
2. Explore booking and cancellation patterns.
3. Engineer meaningful analytical features.
4. Identify important factors associated with cancellation prediction.
5. Translate analytical findings into actionable business recommendations.

---

##  Dataset

The project uses the **Hotel Booking Demand** dataset.

The dataset contains booking information from two hotels:

- City Hotel
- Resort Hotel

The target variable is:

`is_canceled`

where:

- `0` = Booking was not cancelled
- `1` = Booking was cancelled

The cleaned dataset contains:

- 87,377 booking records
- 24,024 cancelled bookings
- 63,353 completed bookings
- 27.49% overall cancellation rate

The original dataset is available from Kaggle:

https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

---

## Data Preparation

The data preparation process included:

- Duplicate detection and removal
- Missing-value treatment
- Data type validation
- Feature selection
- Data consistency checks

A total of 32,013 duplicate records were removed from the original dataset.

The dataset was reduced from:

`119,390 records`

to:

`87,377 records`

after duplicate removal.

---

## Feature Engineering

Additional analytical features were created to improve business analysis and machine learning.

Examples include:

- `total_nights`
- `total_guests`
- `estimated_revenue`
- `arrival_month_num`
- `season`
- `booking_size`
- `stay_category`
- `lead_time_category`

These features support the overall analytical workflow and feature selection steps.

---

##  Key Business Insights

The analysis identified several important patterns.

### Lead Time

Bookings made further in advance show higher cancellation rates.

Bookings with a lead time of 91+ days had approximately a 36.8% cancellation rate.

### Hotel Type

City Hotel showed a higher cancellation rate than Resort Hotel.

- City Hotel: approximately 30.04%
- Resort Hotel: approximately 23.49%

### Market Segment

Online Travel Agency bookings represented a major portion of the dataset and showed a relatively high cancellation rate.

### Repeat Guests

Repeat guests showed a substantially lower cancellation rate compared with new guests.

### ADR

Cancelled bookings had a higher average ADR than completed bookings in the analyzed dataset.

### Deposit Type

The Non Refund category showed an unusually high cancellation rate and should be investigated carefully because this may reflect a particular recording or business-policy convention.

---

##  Business Recommendations

Based on the EDA and feature analysis, hotels can consider:

1. Prioritizing monitoring of long-lead bookings.
2. Reviewing cancellation behavior within Online Travel Agency channels.
3. Investigating the business rules behind Non Refund bookings.
4. Encouraging repeat-customer relationships.
5. Monitoring financial impact in addition to cancellation counts.
6. Using arrival-date-level analysis to support inventory and overbooking decisions.