"""Mappings used for data cleaning."""

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

#WHERE TO USE: LIVESTOCK + CROPS SOLD + ASSET VALUE + OTHER INCOME
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

income_frequency = {
    "Monthly": 12.0,
    "Every three months": 4.0,
    "Every 6 months": 2.0,
    "Every year": 1.0,
    "Lump sum (single payment)": 1.0,   
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
    "Small-scale farm":                                 "Agriculture",
    "Large-scale farm":                                 "Agriculture",

    #Secondary Sector: turning raw materials into goods -- NONE

    #Tertiary Sector: Services (no production)
    "Retail trade":                                     "Private Service",
    "Beauty industry (hair, skin etc)":                 "Private Service",
    "Food industry":                                    "Private Service",
    "Security services":                                "Private Service",
    "Transport":                                        "Private Service",
    "Hospitality (e.g., Accommodation & Lodging )":     "Private Service",
    "Domestic/household helper":                        "Private Service",
    "Travel and Tourism":                               "Private Service",
    "Recreation & Events":                              "Private Service",
    "Education (teacher etc)":                          "Public Service",
    "Health (nurse, doctor etc)":                       "Public Service",
    "Other public sector":                              "Public Service",

    #Other/Unclear
    "Others, specify":                                  "Other/Unclear",
    "I don't know":                                     "Other/Unclear",
}

aspired_occupation = {
    #Primary Sector: creating raw materials
    "Crop farming/cultivation":                                                                 "Agriculture",
    "Both crop and livestock/fish farming":                                                     "Agriculture",
    "Livestock keeping/raising":                                                                "Agriculture",
    "Fishing":                                                                                  "Agriculture",
    "Agricultural wage labour (hired agricultural labour)":                                     "Agriculture",
    "Self-employed agribusiness/agrienterprise":                                                "Agriculture",

    #Secondary Sector: turning raw materials into goods
    "Factory worker/manufacturing jobs":                                                        "Manufacturing",
    "Construction labour":                                                                      "Manufacturing",
    
    #Tertiary Sector: Services (no production)
    "Self-employed non-agribusiness (wholesale/retail trade, etc.)":                            "Private Service",
    "Other service sector jobs (worker in hotels, restaurants, shops, security guards, etc.)":  "Private Service",
    "Domestic/household helper":                                                                "Private Service",
    "Driver/transport":                                                                         "Private Service",
    "Government officers/employees/ civil servant":                                             "Public Service",
    "Teacher/education":                                                                        "Public Service",

    #Other/Unclear
    "Charcoal burning, production, and selling":                                                "Charcoal",
    "None/No employment":                                                                       "Other/Unclear",
    "Retired/Pensioner":                                                                        "Other/Unclear",
}

