"""RELEVANT FEATURES.

Each dictionary maps: {original_col_name: (new_name, dtype, fill_value)}
    - new_name:   the desired name for the column.
    - dtype:      the desired datatype for the column.
    - fill_value: how to fill missing values. Options are:
                      - None:      skip missing-value replacement
                      - a literal: e.g. 0
                      - "mean":    mean value (numerical columns)
                      - "median":  median value (numerical columns)
                      - "missing": fills in "missing" (categorical columns)
                      - "dummy": convert Yes/No strings to 0/1 integers and fills missings with 0 
"""

# ============================================================
# HOUSEHOLD-LEVEL FEATURES
# ============================================================

IDENTIFYING_INFO_2023 = {
    "ctry":           ("country",                       "object",   None        ),
    "interview__key": ("interview_key",                 "object",   None        ),
    #"hhid":          ("hhid",                          "object",   "missing"   ),
    "ea":             ("enumeration_area",              "object",   None        ),
    "dist":           ("district",                      "object",   None        ),
    "region":         ("region",                        "object",   None        ),
    # "res_rel":      ("respondant_relation_to_head",   "object",   "missing"   ), #dropped: 50-70% missings
}

LAND_OWNERSHIP_ACCESS_2023 = {
    "interview__key":  ("interview_key",                                    "object",   None        ),
    "lnd_mes":         ("land_measurement",                                 "object",   None        ),
    # "lnd_mes_1":     ("land_measurement_other",                           "object",   "missing"   ),
    "lnd01":           ("land_size_cropland",                               "float32",  0           ),
    "lnd02":           ("land_size_fallow",                                 "float32",  0           ),
    "lnd03":           ("land_size_agroforestry_forestry",                  "float32",  0           ),
    "lnd04":           ("land_size_pasture",                                "float32",  0           ),
    "lnd08":           ("land_size_residential",                            "float32",  0           ),
    "lnd09":           ("land_size_lodge_camp",                             "float32",  0           ),
    # "lnd06":         ("land_size_other",                                  "float32",  0           ),
    "lnd_ten01":       ("land_cropland_ownership_status",                   "object",   "missing"   ),
    # "lnd_ten02":     ("land_fallow_ownership_status",                     "object",   "missing"   ), #dropped: 60-90% missings
    # "lnd_ten03":     ("land_agroforestry_forestry_ownership_status",      "object",   "missing"   ), #dropped: >90% missings
    # "lnd_ten04":     ("land_pasture_ownership_status",                    "object",   "missing"   ), #dropped: >90% missings
    "lnd_ten08":       ("land_residential_ownership_status",                "object",   "missing"   ),
    # "lnd_ten09":     ("land_lodge_camp_ownership_status",                 "object",   "missing"   ), #dropped: 100% missings
    # "lnd_ten06":      ("land_other_ownership_status",                     "object",   "missing"   ),
    "lnd_16":          ("land_used_as_collateral",                          "object",   "missing"   ), #is yes/no, could be 1/0
    "num_plots":       ("land_number_of_plots",                             "float32",  0           ),
}

CROP_PRODUCTION_2023 = {
    "interview__key":     ("interview_key",                    "object",  None        ),
    # "r_crop__id":       ("crop_type",                        "object",  "missing"   ),#not necessary to know the specific crop
    "crop_harvest":       ("crop_harvested",                   "float32", "dummy"     ),
    # "crop_output":      ("crop_harvest_amount",              "float32", 0           ),
    # "crop_unit":        ("crop_harvest_unit",                "object",  "missing"   ),
    # "crop_unit_1":      ("crop_harvest_unit_other",          "object",  None        ),
    "crop_sale":          ("crop_sale",                        "float32", "dummy"     ),
    "crop_saleamt":       ("crop_sale_amount",                 "float32", 0           ),
    # "crop_slunits":     ("crop_sale_unit",                   "object",  "missing"   ),
    # "crop_slunits_1":   ("crop_sale_unit_other",             "object",  None        ),
    "crop_price":         ("crop_sale_price_per_unit",         "float32", 0           ),
    "crop_homecons":      ("crop_home_consumption_amount",     "float32", 0           ),
    # "crop_clunits":     ("crop_home_consumption_unit",       "object",  "missing"   ),
    # "crop_cunits_1":    ("crop_home_consumption_unit_other", "object",  None        ),
    "cp_stor":            ("crop_storage",                     "float32", "dummy"     ),
    # "cpamt":            ("crop_storage_amount",              "float32", 0           ),
    # "cpunits2":         ("crop_storage_unit",                "object",  "missing"   ),
    # "cpunits2_other":   ("crop_storage_unit_other",          "object",  None        ),
    "crop_buyer__1":      ("crop_buyer_market",                "float32", "dummy"     ),
    "crop_buyer__2":      ("crop_buyer_trader",                "float32", "dummy"     ),
    "crop_buyer__3":      ("crop_buyer_cooperative",           "float32", "dummy"     ),
    "crop_buyer__4":      ("crop_buyer_commercial_farm",       "float32", "dummy"     ),
    "crop_buyer__5":      ("crop_buyer_hospitality",           "float32", "dummy"     ),
    "crop_buyer__6":      ("crop_buyer_government",            "float32", "dummy"     ),
    # "crop_buyer_other": ("crop_buyer_other",                 "object",  None        ),
    "cp07":               ("crop_organic_fertilizer",          "float32", "dummy"     ),
    "cp08":               ("crop_inorganic_fertilizer",        "float32", "dummy"     ),
    "cp09":               ("crop_pesticides",                  "float32", "dummy"     ),
    "cp11":               ("crop_tractor",                     "float32", "dummy"     ),
}

CROP_EXPENDITURE_2023 = {
    "interview__key":   ("interview_key",                       "object",   None),
    "crp_ip1_exp":      ("crop_exp_seeds_last_12_months",       "float32",  0),
    "crp_ip3_exp":      ("crop_exp_fertilizer_last_12_months",  "float32",  0),
    "crp_ip5_exp":      ("crop_exp_pesticide_last_12_months",   "float32",  0),
    "crp_ip6_exp":      ("crop_exp_machinery_last_12_months",   "float32",  0),
    "crp_ip7_exp":      ("crop_exp_hired_labor_last_12_months", "float32",  0),
    "crp_ip8_exp":      ("crop_exp_land_rental_last_12_months", "float32",  0),
    "crp_ip9_exp":      ("crop_exp_transport_last_12_months",   "float32",  0),
    "crp_ip10_exp":     ("crop_exp_other_last_12_months",       "float32",  0),
}

MARKET_ACCESS_2023 = {
    "interview__key":        ("interview_key",                    "object",     None),
    "markt_output_dist":     ("market_output_distance_in_km",     "float32",    99999), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_input_dist":      ("market_input_distance_in_km",      "float32",    99999), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_buyer":           ("market_type",                      "object",     "missing"),
    # "markt_buyer_oth":     ("market_type_other",                "object",     None),
    "crop_contract":         ("crop_contract",                    "float32",    "dummy"),
    "contract_crop":         ("crop_contract_crop_type",          "object",     "missing"),
    "input_access_subsidy":  ("subsidy",                          "float32",    "dummy"),
    "subsidy_type__1":       ("subsidy_type_seeds",               "float32",    "dummy"),
    "subsidy_type__2":       ("subsidy_type_fertilizer",          "float32",    "dummy"),
    "subsidy_type__3":       ("subsidy_type_agro_chemicals",      "float32",    "dummy"),
    "subsidy_type__4":       ("subsidy_type_interest_free_loan",  "float32",    "dummy"),
    "subsidy_supplier__1":   ("subsidy_supplier_government",      "float32",    "dummy"),
    "subsidy_supplier__2":   ("subsidy_supplier_ngos",            "float32",    "dummy"),
    "subsidy_supplier__3":   ("subsidy_supplier_company",         "float32",    "dummy"),
    # "subsidy_supplier_oth": ("subsidy_supplier_other",          "object",     None),
}

LIVESTOCK_OWNERSHIP_2023 = {
    "interview__key":        ("interview_key",                              "object",  None),
    "r_livestock__id":       ("livestock_type",                             "object",  "missing"),
    "lv02":                  ("livestock_number_owned",                     "float32", 0),
    "lv03":                  ("livestock_number_sold",                      "float32", 0),
    "lv06":                  ("livestock_number_lost_disease_theft",        "float32", 0),
    "lv07":                  ("livestock_number_lost_wildlife_attack",      "float32", 0),
    "lv08":                  ("livestock_price_head_sold",                  "float32", 0),
}

LIFESTOCK_GRAZING_2023 = {
    "interview__key":            ("interview_key",                                    "object",     None),
    "grazing_dist":              ("grazing_distance_in_min",                          "float32",    0),
    "grazing_days":              ("grazing_time_in_min",                              "float32",    0),
    "grazing_hour":              ("grazing_time_hours_per_day",                       "float32",    0),
    "grazing_ownership":         ("grazing_land_ownership_status",                    "object",     "missing"),
    "grazing_sharing":           ("grazing_land_number_hh_sharing",                   "float32",    0),
    "grazing_permit":            ("grazing_land_permit",                              "float32",    "dummy"), 
    "grazing_permit_price":      ("grazing_land_permit_price",                        "float32",    0),
    "grazing_years":             ("grazing_land_use_duration_in_years",               "float32",    0),
    "grazing_challenges__1":     ("grazing_land_challenges_little_gras",              "float32",    "dummy"),
    "grazing_challenges__2":     ("grazing_land_challenges_prosopis_parthenium",      "float32",    "dummy"), 
    "grazing_challenges__3":     ("grazing_land_challenges_other_pastoralists",       "float32",    "dummy"), 
    "grazing_challenges__4":     ("grazing_land_challenges_ethnic_conflict",          "float32",    "dummy"), 
    "grazing_challenges__5":     ("grazing_land_challenges_tension_conflict",         "float32",    "dummy"), 
    "grazing_challenges__6":     ("grazing_land_challenges_theft",                    "float32",    "dummy"), 
    "grazing_challenges__7":     ("grazing_land_challenges_raiding",                  "float32",    "dummy"), 
    "grazing_challenges__8":     ("grazing_land_challenges_no_water",                 "float32",    "dummy"), 
    "grazing_challenges__9":     ("grazing_land_challenges_too_far",                  "float32",    "dummy"), 
    "grazing_challenges__10":    ("grazing_land_challenges_expensive",                "float32",    "dummy"), 
    "grazing_challenges__11":    ("grazing_land_challenges_None",                     "float32",    "dummy"), 
    # "grazing_challenge_other": ("grazing_land_challenges_other",                    "object",  None),
}

LIFESTOCK_INCOME_2023 = {
    "interview__key":       ("interview_key",                                "object",      None),
    "liv_pdtsal":           ("livestock_products_sold_last_12_months",       "float32",     "dummy"),
    "which_liv_pdts__1":    ("livestock_products_sold_meat",                 "float32",     "dummy"),
    "which_liv_pdts__2":    ("livestock_products_sold_milk",                 "float32",     "dummy"),
    "which_liv_pdts__3":    ("livestock_products_sold_cheese",               "float32",     "dummy"),
    "which_liv_pdts__4":    ("livestock_products_sold_yogurt",               "float32",     "dummy"),
    "which_liv_pdts__5":    ("livestock_products_sold_wool",                 "float32",     "dummy"),
    "which_liv_pdts__6":    ("livestock_products_sold_honey_wax",            "float32",     "dummy"),
    "which_liv_pdts__7":    ("livestock_products_sold_eggs",                 "float32",     "dummy"),
    # "which_liv_pdts_oth": ("livestock_products_sold_other",                "object",      None),
    "liv_buyer":            ("livestock_products_buyer",                     "object",      "missing"),
    # "liv_buyer_oth":       ("livestock_products_buyer_other",              "object",      None),
    "liv_buyer_where":      ("livestock_products_market_type",               "object",      "missing"),
    "livmkt_dist":          ("livestock_market_distance_in_km",              "float32",     0),
    "liv_pdt_inc":          ("livestock_income_last_12_months",              "float32",     0),
    "liv_contract":         ("livestock_contract",                           "float32",     "dummy"),
}

LIFESTOCK_EXPENDITURE_2023 = {
    "interview__key":     ("interview_key",                     "object",   None),
    "lvexp01_11":         ("livestock_exp_feed_fodder",         "float32",  0),
    "lvexp02_12":         ("livestock_exp_rent_gazing_land",    "float32",  0),
    "lvexp03_13":         ("livestock_exp_veterinary_services", "float32",  0),
    "lvexp04_14":         ("livestock_exp_shelter",             "float32",  0),
    "lvexp05_15":         ("livestock_exp_hired_labor",         "float32",  0),
    # "lvexp06_16":       ("livestock_exp_other",               "float32",  0),
}

HOUSING_CONDITIONS_2023 = {
    "interview__key":    ("interview_key",                  "object",  None),
    "h02":               ("house_room_number",              "float32", 0),
    "h03":               ("house_roof_material",            "object",  "missing"),
    # "h03_oth":         ("house_roof_material_other",      "object",  None),
    "h04":               ("house_wall_material",            "object",  "missing"),
    # "h04_oth":         ("house_wall_material_other",      "object",  None),
    "h05":               ("house_floor_material",           "object",  "missing"),
    # "h05_oth":         ("house_floor_material_other",     "object",  None),
    "h06":               ("house_water_source",             "object",  "missing"),
    # "h06_oth":         ("house_water_source_other",       "object",  None),
    "h07":               ("house_toilet_type",              "object",  "missing"),
    # "h07_oth":         ("house_toilet_type_other",        "object",  None),
}

ENERGY_ACCESS_2023 = {
    "interview__key":    ("interview_key",                              "object", None),
    "h09":               ("house_energy_source",                        "object", "missing"),
    # "h09_oth":         ("house_energy_source_other",                  "object", None),
    "h10":               ("house_energy_source_for_cooking",            "object", "missing"),
    # "h10_1":           ("house_energy_source_for_cooking_other",      "object", None),
    "h11":               ("house_energy_source_for_lighting",           "object", "missing"),
    # "h11_1":           ("house_energy_source_for_lighting_other",     "object", None),
}

ASSETS_OWNED_2023 = {
    "interview__key":    ("interview_key",          "object",  None),
    "r_asset_own__id":   ("asset_type",             "object",  "missing"),
    "ha0_1":             ("asset_number_owned",     "float32", 0),
    "ha0_4":             ("asset_price_per_unit",   "float32", 0), #TODO: using mean per asset_type would be better!
}

INTERNET_ACCESS_2023 = {
    "interview__key":    ("interview_key",                          "object",   None),
    "access_internet":   ("internet_access",                        "float32",  "dummy"),
    "internet_home":     ("internet_access_at_home",                "float32",  "dummy"),
    # "distance_internet": ("internet_access_distance_in_meters",     "float32", None), #dropped: 100% missings
    #TODO: What Types of Online Activities Do you Engage in when using the Internet? Available
}

SHOCKS_AND_COPING_2023 = {
    "interview__key":   ("interview_key",                                       "object",  None),
    # "r_shocks__id":   ("shock_id",                                            "object",  None),
    "r_shocks":         ("shock_type_affected_last_12_months",                  "object",  None),
    "sh_1":             ("shock_frequency_last_12_months",                      "float32", None),
    "sh_2":             ("shock_severity_last_12_months",                       "object",  None),

    #COPING
    "sh_3__1":           ("shock_coping_strategy_relatives_friends",            "object",  None),
    "sh_3__2":           ("shock_coping_strategy_government",                   "object",  None),
    "sh_3__3":           ("shock_coping_strategy_food_reduction",               "object",  None),
    "sh_3__4":           ("shock_coping_strategy_changed_cropping_practices",   "object",  None),
    "sh_3__5":           ("shock_coping_strategy_more_employment",              "object",  None),
    "sh_3__6":           ("shock_coping_strategy_hh_member_migration",          "object",  None),
    "sh_3__7":           ("shock_coping_strategy_savings",                      "object",  None),
    "sh_3__8":           ("shock_coping_strategy_insurance",                    "object",  None),
    "sh_3__9":           ("shock_coping_strategy_credit",                       "object",  None),
    "sh_3__10":          ("shock_coping_strategy_sold_hh_assets",               "object",  None),
    "sh_3__11":          ("shock_coping_strategy_sold_livestock",               "object",  None),
    "sh_3__12":          ("shock_coping_strategy_migration",                    "object",  None),
    "sh_3__13":          ("shock_coping_strategy_police_report",                "object",  None),
    "sh_3__14":          ("shock_coping_strategy_nothing",                      "object",  None),
    # "sh_3_oth":        ("shock_coping_strategy_other",                        "object",  None),

    "sh_4":              ("shock_future_likelihood_well_prepared",              "object",  None),
    "sh_5":              ("shock_future_likelihood_recover_fully",              "object",  None),
    "sh_6":              ("shock_future_likelihood_change_income_source",       "object",  None),
}

SOCIAL_NETWORK_2023 = {
    "interview__key":   ("interview_key",                           "object",   None),
    "as19":             ("mobile_money_access",                     "float32",  "dummy"),
    "as18__1":          ("membership_farmers_group",                "float32",  "dummy"),
    "as18__2":          ("membership_agricultural_cooperative",     "float32",  "dummy"),
}

SOCIAL_EMBEDDEDNESS_2023 = {
    # ONLY RESPONDAND ASEKD:CAN BE USED AS A PROXY FOR THE OPTIMISM OF THE HH
    "interview__key":   ("interview_key",                                "object",  None),
    "as_loc01_in":      ("my_life_course_depends_on_me",                 "object",  "missing"),
    "as_loc02_in":      ("success_is_hard_work",                         "object",  "missing"),
    "as_loc03_in":      ("ability_is_more_important_than_effort",        "object",  "missing"),
    "as_loc04_in":      ("my_plans_will_work",                           "object",  "missing"),
    "as_loc06_in":      ("I_can_shape_my_future_positively",             "object",  "missing"),
    "as_loc12_in":      ("I_am_optimistic_about_my_future",              "object",  "missing"),
    "as_loc13_in":      ("I_am_optimistic_about_my_familys_future",      "object",  "missing"),
    "exp_ev1_01":       ("worry_about_job_loss_or_economic_livelihood",  "object",  "missing"),
}

FOOD_INSECURITY_2023 = {
    "interview__key":       ("interview_key",                    "object",      None),
    "food_sufficent":       ("sufficent_food_number_of_month",   "float32",     0),
    #TODO: During the Last 12 Months, Was There a Time When, Because of Lack of Money or Ot... available!
}

OTHER_INCOME_SOURCES_2023 = {
    "interview__key":       ("interview_key",           "object",  None),
    "r_otherincome__id":    ("other_income_source",     "object",  "missing"),
    "inc_oth_amt":          ("other_income_amount",     "float32", "mean"), #TODO: using mean per income source would be better!
    "int_oth_income":       ("other_income_frequency",  "object",  "missing"),
}

ROAD_CONNECTIVITY_2023 = {
    "interview__key":       ("interview_key",               "object",  None),
    "road_1":               ("road_type",                   "object",  "missing"),
    "road_2":               ("road_condition",              "object",  "missing"),
    "road_6":               ("road_distance_in_minutes",    "float32", "mean"), #very little missings, so mean is a save option!
}

# ============================================================
# INDIVIDUAL-LEVEL FEATURES
# ============================================================

HH_MEMBERS_2023 = {
    "interview__key":   ("interview_key",        "object",  None),
    "r_members__id":    ("members_id",           "object",  None),
    "ha03":             ("gender",               "object",  "missing"),
    "ha_rel":           ("relation_to_head",     "object",  "missing"),
    "age":              ("age",                  "float32", "mean"),
    "ha07":             ("ethnic_group",         "object",  "missing"),
    # "ha07_other":     ("ethnic_group_new",     "object",  "missing"),
    "religio":          ("religion",             "object",  "missing"),
    # "religio_1":      ("religion_other",       "object",  "missing"),
    "educ1":            ("education_level",      "object",  "missing"),
}

OFF_FARM_EMPLOYMENT_2023 = {
    "interview__key":       "interview_key",
    "r_members__id":        "members_id", 
    "lbr3_1":               "sector_off_farm_empl_last_12_months",
    # "lbr3_1_oth":           "sector_off_farm_empl_last_12_months_other",
    "emp_form":             "empl_type",

    #SELF-EMPLOYMENT / OWN BUSINESS
    "bus_yr":                   "self_empl_duration_in_months",
    # "bus_dry":                  "self_empl_duration_dry_season_in_months",
    # "bus_rain":                 "self_empl_duration_rainy_season_in_months",
    "bus_days_wk":              "self_empl_days_per_week",
    "bus_hrs":                  "self_empl_hours_per_day",
    # "bus_sales":                "self_empl_sales", #per week? per months?
    # "bus_main_use__1":          "self_empl_main_use_invest_in_own_business",
    # "bus_input":                "self_empl_input_costs", #per week? per months?
    # "bus_labor":                "self_empl_labor_costs", #per week? per months?
    # "bus_capital":              "self_empl_capital_costs", #Machinery Maintenance, Rent #per week? per months? 
    # "bus_reg":                  "self_empl_registered",
    # "bus_loc":                  "self_empl_location",
    # "bus_employees":            "self_empl_number_of_employees",
    # "tourism_motivate__1":      "self_empl_motivation_previous_experience", 
    "tourism_motivate__2":      "self_empl_motivation_others_success",  
    # "tourism_motivate__3":      "self_empl_motivation_unclear",  #what dis this "Figure that this Kind.."?
    "tourism_motivate__4":      "self_empl_motivation_unemployment",
    "tourism_motivate__5":      "self_empl_motivation_insufficient_income_1", # from what? agriculture?
    "tourism_motivate__6":      "self_empl_motivation_insufficient_income_2", # from what? agriculture?
    "tourism_motivate__7":      "self_empl_motivation_insufficient_income_3", # from what? agriculture?
    "tourism_motivate__8":      "self_empl_motivation_inherited_business", 
    # "tourism_motivate_oth":     "self_empl_motivation_other",
    "years_exp_agri":           "self_empl_years_experience_in_years",
    # "business_obstacle__1":     "self_empl_obstacle_1", # what is it?
    # "business_obstacle__2":     "self_empl_obstacle_2", # what is it?
    # "business_obstacle__3":     "self_empl_obstacle_3", # what is it?
    # "business_obstacle__4":     "self_empl_obstacle_4", # what is it?
    # "business_obstacle__5":     "self_empl_obstacle_5", # what is it?
    # "business_obstacle__6":     "self_empl_obstacle_6", # what is it?
    # "business_obstacle__7":     "self_empl_obstacle_7", # what is it?
    # "business_obstacle__8":     "self_empl_obstacle_8", # what is it?
    # "business_obstacle__9":     "self_empl_obstacle_9", # what is it?
    # "business_obstacle__10":    "self_empl_obstacle_10", # what is it?
    # "business_obstacle__11":    "self_empl_obstacle_11", # what is it?
    # "business_obs_other":       "self_empl_obstacle_other",
    # "business_financing__1":    "self_empl_three_main_financing_contraints_1", # what is it?
    # "business_financing__2":    "self_empl_three_main_financing_contraints_2", # what is it?
    # "business_financing__3":    "self_empl_three_main_financing_contraints_3", # what is it?
    # "business_financing__4":    "self_empl_three_main_financing_contraints_4", # what is it?
    # "business_financing__5":    "self_empl_three_main_financing_contraints_5", # what is it?
    # "business_financing__6":    "self_empl_three_main_financing_contraints_6", # what is it?
    # "business_financing__7":    "self_empl_three_main_financing_contraints_7", # what is it?
    # "business_financing__8":    "self_empl_three_main_financing_contraints_8", # what is it?
    # "business_financing__9":    "self_empl_three_main_financing_contraints_9", # what is it?
    # "business_financing__10":   "self_empl_three_main_financing_contraints_10", # what is it?
    # "business_financing__11":   "self_empl_three_main_financing_contraints_11", # what is it?
    # "business_financing__12":   "self_empl_three_main_financing_contraints_12", # what is it?
    # "business_financing_oth":   "self_empl_three_main_financing_contraints_other", 
    # "business_finance__1":      "self_empl_loan_source_1", # what is it?
    # "business_finance__2":      "self_empl_loan_source_2", # what is it?
    # "business_finance__3":      "self_empl_loan_source_3", # what is it?
    # "business_finance__4":      "self_empl_loan_source_4", # what is it?
    # "business_finance__5":      "self_empl_loan_source_5", # what is it?
    # "business_finance__6":      "self_empl_loan_source_6", # what is it?
    # "business_finance__7":      "self_empl_loan_source_7", # what is it?
    # "business_finance__8":      "self_empl_loan_source_8", # what is it?
    # "business_finance_oth":     "self_empl_loan_source_other", 
    
    #WAGE EMPLOYMENT
    # "lbr3_2":           "wage_empl_company_name",
    "lbr3_3":           "wage_empl_location",
    "lbr3_4":           "wage_empl_type",
    "lbr3_5":           "wage_empl_permament_wage_per_month",
    "lbr3_6":           "wage_empl_permament_days_per_week",
    "lbr3_7":           "wage_empl_permament_hours_per_day",
    # "lbr3_8":           "wage_empl_seasonal_payment_frequency",
    "lbr3_9":           "wage_empl_seasonal_wage",
    # "lbr3_10":          "wage_empl_seasonal_duration_in_months_1", # what is this?
    # "lbr3_11":          "wage_empl_seasonal_duration_in_months_2", # what is this?
    "lbr3_12":          "wage_empl_seasonal_duration_days_per_week", 
    "lbr3_13":          "wage_empl_seasonal_duration_hours_per_day",
    
    "lbr10":            "wage_empl_contract_status", 
    # "lbr10_1":          "wage_empl_contract_status_other",
    # "job_search":       "wage_empl_job_search",
    # "job_search_oth":   "wage_empl_job_search_other",
    # "lbr09":            "wage_empl_training_received",
    # "emp_years":        "wage_empl_duration_in_years",
}

ON_FARM_EMPLOYMENT_2023 = {
    "interview__key":       "interview_key",
    "r_members__id":        "members_id", 
    "lbr13":                "farm_empl_last_12_months",

    #CROPS
    # "Ibr13_1":              "farm_empl_cash_crops_duration_rainy_season_in_months",
    # "Ibr13_2":              "farm_empl_cash_crops_duration_dry_season_in_months",
    "Ibr13_3":              "farm_empl_cash_crops_days_per_week",
    "Ibr13_4":              "farm_empl_cash_crops_hours_per_day",
    # "Ibr13_5":              "farm_empl_food_crops_duration_rainy_season_in_months",
    # "Ibr13_6":              "farm_empl_food_crops_duration_dry_season_in_months",
    "Ibr13_8":              "farm_empl_food_crops_days_per_week",
    "Ibr13_9":              "farm_empl_food_crops_hours_per_day",
    "years_exp_crp":        "farm_empl_crops_years_experience_in_years",

    #LIVESTOCK
    # "Ibr13_10":             "farm_empl_livestock_duration_in_months_1", # what time horizon?
    # "Ibr13_11":             "farm_empl_livestock_duration_in_months_2", # what time horizon?
    # "Ibr13_12":             "farm_empl_livestock_duration_in_months_3", # what time horizon?
    # "Ibr13_13":             "farm_empl_livestock_duration_in_months_4", # what time horizon?
    "years_exp_liv":        "farm_empl_livestock_years_experience_in_years",
}

MIGRATION_2023 = {
    "interview__key":  "interview_key",
    "r_members__id":   "members_id",
    # "remit_amt":       "remittance_amount",
}

ASPIRATIONS_2023 = {
    "interview__key":    "interview_key",
    "r_members__id":     "members_id",
    "as01":              "beans_allocated_to_empl_occupation",
    "asp_occup":         "aspired_occupation_5_years_ahead",
    # "life_satisfaction": "life_satisfaction",
    "aspire_cont_farm":  "aspiration_continue_farming", #includes partly and full exit ## is it also 5 years?!
    
    #AGRICULTURAL LOAN
    "agri_loan":          "agriculture_loan_last_5_years",
    "agri_loan_amt":      "agriculture_loan_amount",
    # "agri_loan_lndr__1":  "agriculture_loan_lender_bank",
    # "agri_loan_lndr__2":  "agriculture_loan_lender_credit_union",
    # "agri_loan_lndr__3":  "agriculture_loan_lender_private_lender",
    # "agri_loan_lndr__4":  "agriculture_loan_lender_government",
    # "agri_loan_lndr__5":  "agriculture_loan_lender_ngos",
    # "agri_loan_lndr_oth": "agriculture_loan_lender_other",
}

CHILD_ASPIRATIONS_2023 = {
    "interview__key":       "interview_key",
    "r_members__id":        "members_id",
    "r_child__id":          "child_id",
    # "asocp01":              "child_aspiration_occupation", #open ended!
    "youth_child_tofarm":   "child_aspiration_continue_farming", 
}