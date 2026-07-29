"""Mappings."""

# ============================================================
# DATA CLEANING MAPPINGS
# ============================================================

years_of_schooling = {
    # No education 
    "No formal education":          0,
    "Nursey/ Kindergarten/ECD":     0,
    "Pre-Primary":                  0,
    "Adult Literacy":               0,
    "Religious education":          0,
    "Other educational training":   0,
    "I dont know":                  0,

    # BOTSWANA + TANZANIA: Standard 1-7/8 (=Primary School) & Form 1-5/6 (=Secondary School)
    "Standard 1":               1,
    "Standard 2":               2,
    "Standard 3":               3,
    "Standard 4":               4,
    "Standard 5":               5,
    "Standard 6":               6,
    "Standard 7":               7,
    "Standard 8":               8,
    "Form 1":                   8,
    "Form 2":                   9,
    "Form 3":                   10,
    "Form 4":                   11,
    "Form 5":                   12,
    "Form 6":                   13,

    # KENYA + NAMIBIA: Primary 1-8 & Secondary 1-4
    "Primary 1":                1,
    "Primary 2":                2,
    "Primary 3":                3,
    "Primary 4":                4,
    "Primary 5":                5,
    "Primary 6":                6,
    "Primary 7":                7,
    "Primary 8":                8,
    "Secondary school Year 1":  9,
    "Secondary school Year 2":  10,
    "Secondary school Year 3":  11,
    "Secondary school Year 4":  12,

    # ZAMBIA: Grade 1-12 (=Primary & Secondary School)
    "Grade 1":                  1,
    "Grade 2":                  2,
    "Grade 3":                  3,
    "Grade 4":                  4,
    "Grade 5":                  5,
    "Grade 6":                  6,
    "Grade 7":                  7,
    "Grade 8":                  8,
    "Grade 9":                  9,
    "Grade 10":                 10,
    "Grade 11":                 11,
    "Grade 12":                 12,

    #Higher Education
    "Post secondary tertiary college":  14,
    "College":                          14,
    "University level":                 15,
    "Post graduate university level":   16,
}

#WHERE TO USE: LIVESTOCK + CROPS SOLD + ASSET VALUE + OTHER INCOME + WAGES + YIELDS
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
    'Other': 0.6175, # we are assuming any 'Other' to be 'Lima' as they mainly exist in Zambia
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
    "Other➡️specify":                 0.00,  # unknown animal, can't assign a factor
}

other_income_frequency = {
    "Monthly": 1.0,
    "Every three months": 1/3,
    "Every 6 months": 1/6,
    "Every year": 1/12,
    "Lump sum (single payment)": 1/12,   
}

shock_categories = {
    "Large Rise in Prices of Food":                                                                       "price_shock",
    "Drought or Extended Period of No Rain":                                                              "drought",
    "Crop Failure":                                                                                       "crop_failure",
    "Chronicor Severe Illnessor Accident of a Household Member":                                          "illness_death",
    "Livestock Disease/Death":                                                                            "livestock_loss",
    "Large Rise in Prices of Agricultural Inputs(E.g.Agrochemicals,Machinery,HiredLabour)":               "price_shock",
    "Death of a Household Member":                                                                        "illness_death",
    "Large Fall in Sale Prices for Cropsand or Livestock":                                                "price_shock",
    "Floods":                                                                                             "floods",
    "Robbery/Burglary":                                                                                   "other",
    "Livestock Theft(IncludingRaids)":                                                                    "livestock_loss",
    "Loss of Employment":                                                                                 "other",
    "Dwelling Damaged":                                                                                   "other",
    "Household Business Failure(Non-Agricultural)":                                                       "other",
    "Fire on Property":                                                                                   "other",
    "Ethnic or Clan Clashes":                                                                             "other",
    "Household Member Jailed":                                                                            "other",
    "Fallen Sick of COVID-19":                                                                            "illness_death",
    "End of Regular Assistance(E.g.Pension,CashTransfer,Remittances)from Outside the Household":          "other",
    "Other":                                                                                              "other",
    "Loss of Land":                                                                                       "other",
    "Household Memeber Died of COVID-19":                                                                 "illness_death",
}

likelihood = {
    "Extremely likely": 1, 
    "Very  likely": 1,
    "Not very likely": 0, 
    "Not at all likely": 0,     
}

employment_sector = {
    #Primary Sector: creating raw materials
    "Small-scale farm":                                 "agriculture",
    "Large-scale farm":                                 "agriculture",

    #Secondary Sector: turning raw materials into goods -- NONE

    #Tertiary Sector: Services (no production)
    "Retail trade":                                     "private_service",
    "Beauty industry (hair, skin etc)":                 "private_service",
    "Food industry":                                    "private_service",
    "Security services":                                "private_service",
    "Transport":                                        "private_service",
    "Hospitality (e.g., Accommodation & Lodging )":     "private_service",
    "Domestic/household helper":                        "private_service",
    "Travel and Tourism":                               "private_service",
    "Recreation & Events":                              "private_service",
    "Education (teacher etc)":                          "public_service",
    "Health (nurse, doctor etc)":                       "public_service",
    "Other public sector":                              "public_service",

    #Other/Unclear
    "Others, specify":                                  "other_unclear",
    "I don't know":                                     "other_unclear",
}

aspired_occupation = {
    #Primary Sector: creating raw materials
    "Crop farming/cultivation":                                                                 "agriculture",
    "Both crop and livestock/fish farming":                                                     "agriculture",
    "Livestock keeping/raising":                                                                "agriculture",
    "Fishing":                                                                                  "agriculture",
    "Agricultural wage labour (hired agricultural labour)":                                     "agriculture",
    "Self-employed agribusiness/agrienterprise":                                                "agriculture",

    #Secondary Sector: turning raw materials into goods
    "Factory worker/manufacturing jobs":                                                        "manufacturing",
    "Construction labour":                                                                      "manufacturing",
    
    #Tertiary Sector: Services (no production)
    "Self-employed non-agribusiness (wholesale/retail trade, etc.)":                            "private_service",
    "Other service sector jobs (worker in hotels, restaurants, shops, security guards, etc.)":  "private_service",
    "Domestic/household helper":                                                                "private_service",
    "Driver/transport":                                                                         "private_service",
    "Government officers/employees/ civil servant":                                             "public_service",
    "Teacher/education":                                                                        "public_service",

    #Other/Unclear
    "Charcoal burning, production, and selling":                                                "charcoal",
    "None/No employment":                                                                       "other_unclear",
    "Retired/Pensioner":                                                                        "other_unclear",
}

self_employment_location = {
    "Village in region":        "in_region",
    "Town in region":           "in_region",
    "village outside region":   "outside_region",
    "Other, Specify":           None,
    "Town outside region":      "outside_region",
    "Outside the country":      "outside_region",   
}

wage_employment_location = {
    "In this village":                                      "in_region",
    "Town or city within this district/region":             "in_region",
    "In other rural area within or outside this district":  "outside_region",
    "Town or city in another district/region":              "outside_region",
    "Outside the country":                                  "outside_region",
}

contract_status = {
    "Long term permanent contract":     "long_term",
    "Daily wage labourer":              "daily",
    "Fixed term permanent contract":    "fixed_term",
    "Part-time contract":               "part_time",
    "No contract (informal)":           None,   
    "Volunteering":                     None, 
    "Other (specify)":                  None, 
    "Self-employed/ own firm":          None, 
    "Refuse to answer":                 None,
}

job_search = { #how did you find the job? The answers donnot make sense!
    "Public employment/recruitment agency":             "public_employment",
    "From neighbors or friends":                        "family_friends",
    "From family and relatives":                        "family_friends",
    "Private employment/recruitment agency":            "private_employment",
    "Online postings":                                  "online",   
    "Farmer or producer organizations or cooperatives": "organizations_cooperatives", 
    "Others, specify":                                  None, 
    "Vocational training centres":                      "training_center",
}

job_satisfaction = { #ordinal encoding
    "Very dissatisfied":  0,
    "Dissatisfied":       1,
    "Neither":            2,
    "Satisfied":          3,
    "Very satisfied":     4,
}

# ============================================================
# FEATURE ENGINEERING MAPPINGS
# ============================================================