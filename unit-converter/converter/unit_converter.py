import streamlit as ui

def convert_unit(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,            # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,         # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,             # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000           # 1 kilogram = 1000 gram
    }
    
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not supported"
    

ui.title("Unit Converter")

value = ui.number_input("Enter the value:", min_value=1.0, step=1.0)

unit_from = ui.selectbox("convert from:", ["meters", "kilometers", "grams", "kilograms"])

unit_to = ui.selectbox("convert to:", ["meters", "kilometers", "grams", "kilograms"])

if ui.button("convert"):
    result = convert_unit(value, unit_from, unit_to)
    ui.write(f"Converted value: {result}")



# import streamlit as ui

# def convert_unit(value, unit_from, unit_to):
#     conversions = {
#         ("meter", "kilometer"): 0.001,  
#         ("kilometer", "meter"): 1000,   
#         ("gram", "kilogram"): 0.001,    
#         ("kilogram", "gram"): 1000     
#     }
    
#     if (unit_from, unit_to) in conversions:
#         conversion = conversions[(unit_from, unit_to)]
#         return value * conversion
#     elif unit_from == unit_to:  
#         return value  
#     else:
#         return "Conversion not supported"
    

# ui.title("Unit Converter by Alishba Meraj")

# value = ui.number_input("Enter the value:")

# unit_from = ui.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])

# unit_to = ui.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# if ui.button("Convert"):
#     result = convert_unit(value, unit_from, unit_to)
#     ui.write(f"Converted value: {result}")
