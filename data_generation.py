import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Constants
builders = [
    ("DLF Ltd.", "BLD001"),
    ("Godrej Properties", "BLD002"),
    ("Sobha Ltd.", "BLD003"),
    ("Prestige Group", "BLD004"),
    ("Tata Housing Development", "BLD005"),
    ("Omaxe Ltd.", "BLD006"),
    ("Lodha Group", "BLD007"),
    ("Brigade Group", "BLD008"),
    ("Raheja Developers", "BLD009"),
]

projects = {
    "DLF Ltd.": [("DLF Cyber City", "PROD001"), ("DLF Capital Greens", "PROD002"), ("DLF One Horizon Center", "PROD003"), ("DLF The Crest", "PROD004")],
    "Godrej Properties": [("Godrej Central", "PROD005"), ("Godrej Platinum", "PROD006"), ("Godrej Nurture", "PROD007"), ("Godrej Woods", "PROD008")],
    "Sobha Ltd.": [("Sobha Dream Acres", "PROD009"), ("Sobha City", "PROD010"), ("Sobha Lifestyle", "PROD011"), ("Sobha International City", "PROD012")],
    "Prestige Group": [("Prestige Lakeside Habitat", "PROD013"), ("Prestige Jindal City", "PROD014"), ("Prestige Jasdan Classic", "PROD015"), ("Prestige Falcon City", "PROD016")],
    "Tata Housing Development": [("Tata Amantra", "PROD017"), ("Tata Avenida", "PROD018"), ("Tata Promont", "PROD019"), ("Tata Primanti", "PROD020")],
    "Omaxe Ltd.": [("Omaxe Connaught Place", "PROD021"), ("Omaxe Royal Residency", "PROD022"), ("Omaxe The Forest Spa", "PROD023"), ("Omaxe World Street", "PROD024")],
    "Lodha Group": [("Lodha The Park", "PROD025"), ("Lodha New Cuffe Parade", "PROD026"), ("Lodha Palava City", "PROD027"), ("Lodha Eternis", "PROD028")],
    "Brigade Group": [("Brigade Orchards", "PROD029"), ("Brigade Panorama", "PROD030"), ("Brigade Exotica", "PROD031"), ("Brigade Meadows", "PROD032")],
    "Raheja Developers": [("Raheja Revanta", "PROD033"), ("Raheja The Leela Sky Villas", "PROD034"), ("Raheja Vanya", "PROD035"), ("Raheja Maheshwara", "PROD036")],
}

# Sample data generation
num_rows = 100000
data = []

for _ in range(num_rows):
    builder_name, builder_code = random.choice(builders)
    project_name, project_code = random.choice(projects[builder_name])
    rate_sq_meter = random.randint(5000, 15000)  # Random rate per square meter
    year = random.randint(2020, 2024)
    location = random.choice(['Delhi', 'Noida', 'Gurgaon', 'Mohali', 'Mumbai', 'Kolkata', 'Bangalore'])
    stage = random.choice(['Completed', 'Under Construction', 'Upcoming'])
    dimension = random.choice(['1 BHK', '2 BHK', '3 BHK', '4 BHK'])
    property_type = random.choice(['Apartment', 'Villa', 'Commercial', 'Plot'])
    flat_available = random.randint(0, 100)
    total_occupied_flat = random.randint(50, 100)
    total_booked = random.randint(0, flat_available)
    on_time = random.choice(['Yes', 'No'])
    expected_delivery_date = datetime.now() + timedelta(days=random.randint(30, 365))
    actual_delivery_date = expected_delivery_date if on_time == 'Yes' else expected_delivery_date + timedelta(days=random.randint(1, 60))
    customer_code = f"CUST{random.randint(10000, 99999)}"
    customer_name = f"Customer {random.randint(1, 1000)}"
    customer_email = f"{customer_name.lower().replace(' ', '_')}@example.com"
    customer_phone = f"+91{random.randint(6000000000, 9999999999)}"
    possession_date = datetime.now() + timedelta(days=random.randint(30, 365))
    interior_quality_rating = random.randint(1, 5)
    exterior_quality_rating = random.randint(1, 5)
    society_rating = random.randint(1, 5)
    security_rating = random.randint(1, 5)
    amenities = random.choice(['Gym', 'Swimming Pool', 'Play Area', 'Parking', 'Garden'])
    builder_rating = random.uniform(1, 5)
    material_code = f"MAT{random.randint(100, 999)}"
    material_name = random.choice(['Cement', 'Bricks', 'Steel', 'Glass'])
    material_description = f"{material_name} for construction"
    material_price = random.uniform(50, 500)
    date = datetime.now().strftime("%Y-%m-%d")
    material_qty = random.randint(1, 100)
    unit = random.choice(['kg', 'm2', 'nos'])
    
    # New fields
    property_code = f"PROP{random.randint(10000, 99999)}"  # Generate property code
    property_address = f"Room {random.randint(1, 100)}, {location}"  # Generate property address
    property_area = random.randint(50, 500)  # Random property area in sq/m
    property_price = rate_sq_meter * property_area  # Calculate property price

    data.append([
        builder_name, builder_code, project_code, project_name, rate_sq_meter, year, location,
        stage, dimension, property_type, flat_available, total_occupied_flat, total_booked,
        on_time, expected_delivery_date.strftime("%Y-%m-%d"), actual_delivery_date.strftime("%Y-%m-%d"),
        customer_code, project_code, property_type, customer_name, customer_email, customer_phone,
        possession_date.strftime("%Y-%m-%d"), interior_quality_rating, exterior_quality_rating,
        society_rating, security_rating, amenities, builder_rating, material_code, material_name,
        material_description, material_price, date, material_qty, unit, property_code, property_address,
        property_area, property_price
    ])

# Create DataFrame
columns = [
    "builder_name", "BuilderCode", "projectCode", "projectName", "rateSqMeter", "year", "location",
    "stage", "dimension", "propertyType", "Flat_available", "totalOccupied_flat", "totalBooked",
    "onTime", "expectedDeliveryDate", "actualDeliveryDate", "customerCode", "projectCode",
    "propertyType", "customerName", "customerEmail", "customerPhone", "possessionDate",
    "interiorQualityRating", "exteriorQualityRating", "societyRating", "securityRating", "amenities",
    "BuilderRating", "materialCode", "materialName", "materialDescription", "materialPrice", "date",
    "materialQty", "unit", "propertyCode", "propertyAddress", "propertyArea", "propertyPrice"
]

df = pd.DataFrame(data, columns=columns)

# Write to CSV
csv_file_path = r'D:\fabricspark_transformation\data_gen\construction_project_data_final.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV files successfully created where applicable!{csv_file_path}")
