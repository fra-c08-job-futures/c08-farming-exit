"""Mappings used for data cleaning."""

education_mapping = {
    # No education 
    "No formal education":          {"years_of_schooling": 0,   "education_level": "No formal education"},
    "Nursey/ Kindergarten/ECD":     {"years_of_schooling": 0,   "education_level": "No formal education"},
    "Pre-Primary":                  {"years_of_schooling": 0,   "education_level": "No formal education"},
    "Adult Literacy":               {"years_of_schooling": 0,   "education_level": "No formal education"},
    "Religious education":          {"years_of_schooling": 0,   "education_level": "No formal education"},
    "Other educational training":   {"years_of_schooling": 0,   "education_level": "No formal education"},
    "I dont know":                  {"years_of_schooling": 0,   "education_level": "No formal education"},

    # BOTSWANA + TANZANIA: Standard 1-7/8 (=Primary School) & Form 1-5/6 (=Secondary School)
    "Standard 1":               {"years_of_schooling": 1,   "education_level": "Some primary"},
    "Standard 2":               {"years_of_schooling": 2,   "education_level": "Some primary"},
    "Standard 3":               {"years_of_schooling": 3,   "education_level": "Some primary"},
    "Standard 4":               {"years_of_schooling": 4,   "education_level": "Some primary"},
    "Standard 5":               {"years_of_schooling": 5,   "education_level": "Some primary"},
    "Standard 6":               {"years_of_schooling": 6,   "education_level": "Some primary"},
    "Standard 7":               {"years_of_schooling": 7,   "education_level": "Some primary"},
    "Standard 8":               {"years_of_schooling": 8,   "education_level": "Some primary"},
    "Form 1":                   {"years_of_schooling": 8,   "education_level": "Some secondary"},
    "Form 2":                   {"years_of_schooling": 9,   "education_level": "Some secondary"},
    "Form 3":                   {"years_of_schooling": 10,  "education_level": "Some secondary"},
    "Form 4":                   {"years_of_schooling": 11,  "education_level": "Some secondary"},
    "Form 5":                   {"years_of_schooling": 12,  "education_level": "Some secondary"},
    "Form 6":                   {"years_of_schooling": 13,  "education_level": "Some secondary"},
 
    # KENYA + NAMIBIA: Primary 1-8 & Secondary 1-4
    "Primary 1":                {"years_of_schooling": 1,   "education_level": "Some primary"},
    "Primary 2":                {"years_of_schooling": 2,   "education_level": "Some primary"},
    "Primary 3":                {"years_of_schooling": 3,   "education_level": "Some primary"},
    "Primary 4":                {"years_of_schooling": 4,   "education_level": "Some primary"},
    "Primary 5":                {"years_of_schooling": 5,   "education_level": "Some primary"},
    "Primary 6":                {"years_of_schooling": 6,   "education_level": "Some primary"},
    "Primary 7":                {"years_of_schooling": 7,   "education_level": "Some primary"},
    "Primary 8":                {"years_of_schooling": 8,   "education_level": "Some primary"},
    "Secondary school Year 1":  {"years_of_schooling": 9,   "education_level": "Some secondary"},
    "Secondary school Year 2":  {"years_of_schooling": 10,  "education_level": "Some secondary"},
    "Secondary school Year 3":  {"years_of_schooling": 11,  "education_level": "Some secondary"},
    "Secondary school Year 4":  {"years_of_schooling": 12,  "education_level": "Some secondary"},
 
    # ZAMBIA: Grade 1-12 (=Primary & Secondary School)
    "Grade 1":                  {"years_of_schooling": 1,   "education_level": "Some primary"},
    "Grade 2":                  {"years_of_schooling": 2,   "education_level": "Some primary"},
    "Grade 3":                  {"years_of_schooling": 3,   "education_level": "Some primary"},
    "Grade 4":                  {"years_of_schooling": 4,   "education_level": "Some primary"},
    "Grade 5":                  {"years_of_schooling": 5,   "education_level": "Some primary"},
    "Grade 6":                  {"years_of_schooling": 6,   "education_level": "Some primary"},
    "Grade 7":                  {"years_of_schooling": 7,   "education_level": "Some primary"},
    "Grade 8":                  {"years_of_schooling": 8,   "education_level": "Some secondary"},
    "Grade 9":                  {"years_of_schooling": 9,   "education_level": "Some secondary"},
    "Grade 10":                 {"years_of_schooling": 10,  "education_level": "Some secondary"},
    "Grade 11":                 {"years_of_schooling": 11,  "education_level": "Some secondary"},
    "Grade 12":                 {"years_of_schooling": 12,  "education_level": "Some secondary"},
 
    #Higher Education
    "Post secondary tertiary college":  {"years_of_schooling": 14, "education_level": "Post-secondary (non-university)"},
    "College":                          {"years_of_schooling": 14, "education_level": "Post-secondary (non-university)"},
    "University level":                 {"years_of_schooling": 15, "education_level": "University"},
    "Post graduate university level":   {"years_of_schooling": 16, "education_level": "Postgraduate (university)"},
}

#WHERE TO USE: LIVESTOCK + CROPS SOLD + ASSET VALUE
eur_exchange_rates = {
    "Botswana": 0.069,   # BWP -> EUR
    "Kenya": 0.0071,     # KES -> EUR
    "Namibia": 0.049,    # NAD -> EUR
    "Tanzania": 0.00034, # TZS -> EUR
    "Zambia": 0.033,     # ZMW -> EUR
}
    
acres_conversion_factors = {
    'Acres': 1.0,
    'Hectares': 2.471,
    'Lima': 0.6175, #Zambia measurements
}

livestock_conversion_factors = {
    "Cows/Heifers":                   0.70,
    "Bulls/Oxen/Steers":              0.70,
    "Calves - Males/Females":         0.20,
    "Goats - He/She/Kids":            0.10,
    "Sheep - Rams/Ewes/Lambs":        0.10,
    "Pigs - Boar/Sows/Piglets":       0.20,
    "Chicken - Cocks/Broilers":       0.01,
    "Chicken - Hens/Layers":          0.01,
    "Ducks":                          0.01,
    "Dove /Pigeon":                   0.01,
    "Guinea Fowls":                   0.01,
    "Horses":                         0.80,
    "Mules/Donkey":                   0.50,
    "Camel":                          1.00,
    "Beehive":                        0.00,  # not a standard TLU category
    "Insects (Bees/Crickets/Etc.)":   0.00,  # not a standard TLU category
    "Other➡️specify":                0.00,  # unknown animal, can't assign a factor
}

income_frequency = {
    "Monthly": 12.0,
    "Every three months": 4.0,
    "Every 6 months": 2.0,
    "Every year": 1.0,
    "Lump sum (single payment)": 1.0,   
}