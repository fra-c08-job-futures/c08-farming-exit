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
    "Other➡️specify":                0.00,  # unknown animal, can't assign a factor
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

migration_intention = { 
    "No intention to migrate":              0,
    "Yes temporarily migrate":              1,
    "Don’t know":                           0,
    "Yes permanently migrate":              1,
    "Refuse to answer":                     0,
}

life_satisfaction = { #ordinal encoding
    "Very dissatisfied": 0,
    "dissatisfied":      1,
    "Neither":           2,
    "Satisfied":         3,
    "Very satisfied":    4,
}

aspiration_continue_farming = { 
    "Continue to farming":                  "continue",
    "Both":                                 "hybrid",
    "Other non-agricultural business":      "exit",
    "Not engaged in farming":               "exit",
}

child_aspiration_continue_farming = { #ordinal encoding
    "Very unlikely":        0,
    "Unlikely":             1,
    "Maybe, maybe not":     2,
    "Likely":               3,
    "Very likely":          4,
}

primary_activity = {
    # Farm work
    "Small livestock raising (e.g. sheep, goats, pigs)":    "farm_work",
    "Large livestock raising (e.g. cattle, camel)":         "farm_work",
    "Food crop farming":                                    "farm_work",
    "Cash crop farming":                                    "farm_work",
    "Poultry raising (e.g. chickens, ducks, turkeys)":      "farm_work",
    "Fishpond culture":                                     "farm_work",
    "Pasture farming":                                      "farm_work",
    "Selling crops and crop products":                      "farm_work",
    "Selling milk and other livestock produce":             "farm_work",

    # Non-farm work
    "Work as employed":                                     "wage_employed_work",
    "Own business work":                                    "self_employed_work",
    "Weaving, sewing, textile care":                        "self_employed_work",

    # Domestic and care work
    "Cooking":                                              "domestic_and_care_work",
    "Domestic work (incl fetching wood and water)":         "domestic_and_care_work",
    "Care for children":                                    "domestic_and_care_work",
    "Shopping/getting service (incl health services)":      "domestic_and_care_work",
    "Caring for adults (sick, elderly)":                    "domestic_and_care_work",

    # Personal time and leisure
    "Sleeping and resting":                                 "personal_time_leisure",
    "Social activities and hobbies":                        "personal_time_leisure",
    "Personal care":                                        "personal_time_leisure",
    "Eating and drinking":                                  "personal_time_leisure",
    "Watching TV/listening to radio/reading":               "personal_time_leisure",
    "Religious activities":                                 "personal_time_leisure",
    "Exercising":                                           "personal_time_leisure",

    # Mobility & education
    "Commuting (to/from work or school)":                   "mobility_education",
    "Travelling (not for work or school)":                  "mobility_education",
    "School (also homework)":                               "mobility_education",
    "Other→specify...":                                     "other",
}

agreement = { #ordinal encoding
    "Strongly disagree":            0,
    "Disagree":                     1,
    "Indifferent (neither nor)":    2,
    "Agree":                        3,
    "Strongly agree":               4,
}

worries = { #ordinal encoding
    "Not at all worried":   0,
    "Slightly worried":     1,
    "Worried":              2,
    "Very worried":         3,
    "Extremely worried":    4,
}

lighting_source = { #ordinal encoding
    "Firewood":                        0,
    "Torch":                           1,
    "Candle":                          2,
    "Lamp oil":                        3,
    "Any other energy for lighting":   4,
    "Solar":                           5,
    "Gas (biogas)":                    6,
    "Electricity":                     7,
    "Private generator":               8,
}

toilet_type = { #ordinal encoding
    "No facility/Bush/polythene":            0,
    "Uncovered pit latrine":                 1,
    "Covered pit latrine without a slab":    2,
    "Covered pit patrine with slab":         3,
    "VIP latrine":                           4,
    "Ecosan toilet":                         5,
    "Flush toilet":                          6,
    "Other➡️ Please specify":                float("nan"),
}

wall_material = { #ordinal encoding
    "Grass":                        0,
    "Mud with poles":               1,
    "Unburnt bricks with mud":      2,
    "Wood":                         3,
    "Tin/iron sheets/mabaati":      4,
    "Bricks with cement":           5,
    "Concrete":                     6,
    "Other➡️ Please specify":       float("nan"),
}

energy_source = { #ordinal encoding
    "NONE":                                                  float("nan"),
    "own electricity generation: electric generator":        0,
    "own electricity generation: solar panel":               1,
    "household is connected to an off-grid solar system":    2,
    "household is connected to the electrical grid":         3,
    "Others ➡️ Specify":                                    float("nan"),
    "I don't know":                                          float("nan"),
    "Refused to answer":                                     float("nan"),
}

ownership = { #ordinal encoding
    "State owned":                        0,
    "Leased/rented":                      1,
    "Co-share/ co-farming":               2,
    "Communally owned":                   3,
    "Private owned with no land title":   4,
    "Private owned with land title":      5,
    "Don’t know":                         float("nan"),
}

floor_material = { #ordinal encoding
    "Sand":                        0,
    "Smooth earth (soil)":         1,
    "Wood":                        2,
    "Cement screed":               3,
    "Ceramic or other tiles":      4,
    "Other➡️ Please specify":     float("nan"),
}

roof_material = { #ordinal encoding
    "Thatched grass":              0,
    "Tin":                         1,
    "Iron sheets":                 2,
    "Tiles":                       3,
    "Concrete":                    4,
    "Other➡️ Please specify":     float("nan"),
}

market_type = { #ordinal encoding
    "Directly at the homestead":                      0,
    "Directly at the farm":                           1,
    "Market in this village":                         2,
    "Rural market in neighbouring other village":     3,
    "Urban market (town) in this region":             4,
    "Large city market in this or other region":      5,
}

buyer_type = { #ordinal encoding
    "Direct buyers, open-air market":                 0,
    "Brokers, middlemen, traders":                    1,
    "Cooperatives, farmers associations, groups":     2,
    "Government":                                     3,
    "Other➡️ Please specify":                         float("nan"),
}

road_condition = { #ordinal encoding
    "Almost not passable":                                         0,
    "Only passable with certain vehicles/ at certain times":       1,
    "Well passable":                                               2,
    "Very well passable, in both rainy and dry season":            3,
}

road_type = { #ordinal encoding
    "Dirt road/ bush road":     0,
    "Murram/ gravel road":      1,
    "Tarmac road":              2,
    "None of these":            float("nan"),
}

water_source = { #ordinal encoding
    "Unprotected source (well spring river lake tank truck)":       0,
    "Protected (borehole protected well public taps rain water)":   1,
    "Piped water (house or public)":                                2,
    "Other, Specify":                                               float("nan"),
}

cooking_energy_source = { #ordinal encoding
    "Firewood":              0,
    "Charcoal":              1,
    "Gas (incl. biogas)":    2,
    "Electric cookers":      3,
}


# ============================================================
# FEATURE ENGINEERING MAPPINGS
# ============================================================

#WHERE TO USE: LIVESTOCK + CROPS SOLD + ASSET VALUE + OTHER INCOME + WAGES + YIELDS
eur_exchange_rates = {
    "Botswana": 0.069,   # BWP -> EUR
    "Kenya": 0.0071,     # KES -> EUR
    "Namibia": 0.049,    # NAD -> EUR
    "Tanzania": 0.00034, # TZS -> EUR
    "Zambia": 0.033,     # ZMW -> EUR
}