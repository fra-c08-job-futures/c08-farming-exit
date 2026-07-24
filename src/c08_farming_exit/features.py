"""FEATURE DICTIONARIES.

Each dictionary maps: {original_col_name: (new_name, dtype, fill_value, mapping)}
    - new_name:   the desired name for the column.
    - dtype:      the desired datatype for the column.
    - fill_value: how to fill missing values. Options are:
                      - None:      skip missing-value replacement
                      - a literal: e.g. 0 (numerical columns)
                      - "mean":    mean value (numerical columns)
                      - "median":  median value (numerical columns)
                      - "missing": fills in "missing" (categorical columns)
                      - "dummy": convert Yes/No strings to 0/1 integers and fills missings with 0 
    - mapping:    how to convert the values based on a pre-defined mapping (None for no mapping)
"""
from c08_farming_exit import mappings

# ============================================================
# HOUSEHOLD-LEVEL FEATURES
# ============================================================

IDENTIFYING_INFO_2023 = {
    "ctry":           ("country",                       "object",   None,        None),
    "interview__key": ("interview_key",                 "object",   None,        None),
    #"hhid":          ("hhid",                          "object",   "missing",   None),
    "ea":             ("enumeration_area",              "object",   None,        None),
    "dist":           ("district",                      "object",   None,        None),
    "region":         ("region",                        "object",   None,        None),
    # "res_rel":      ("respondant_relation_to_head",   "object",   "missing",   None), #dropped: 50-70% missings
}

LAND_OWNERSHIP_ACCESS_2023 = {
    "interview__key":  ("interview_key",                                    "object",   None,        None                               ),
    "lnd_mes":         ("land_measurement",                                 "object",   None,        mappings.acres_conversion_factors  ),
    # "lnd_mes_1":     ("land_measurement_other",                           "object",   "missing"n   None                               ),
    "lnd01":           ("land_size_cropland",                               "float32",  0,           None                               ),
    "lnd02":           ("land_size_fallow",                                 "float32",  0,           None                               ),
    "lnd03":           ("land_size_agroforestry_forestry",                  "float32",  0,           None                               ),
    "lnd04":           ("land_size_pasture",                                "float32",  0,           None                               ),
    "lnd08":           ("land_size_residential",                            "float32",  0,           None                               ),
    "lnd09":           ("land_size_lodge_camp",                             "float32",  0,           None                               ),
    # "lnd06":         ("land_size_other",                                  "float32",  0,           None                               ),
    "lnd_ten01":       ("land_cropland_ownership_status",                   "object",   "missing",   None                               ),
    # "lnd_ten02":     ("land_fallow_ownership_status",                     "object",   "missing",   None                               ), #dropped: 60-90% missings
    # "lnd_ten03":     ("land_agroforestry_forestry_ownership_status",      "object",   "missing",   None                               ), #dropped: >90% missings
    # "lnd_ten04":     ("land_pasture_ownership_status",                    "object",   "missing",   None                               ), #dropped: >90% missings
    "lnd_ten08":       ("land_residential_ownership_status",                "object",   "missing",   None                               ),
    # "lnd_ten09":     ("land_lodge_camp_ownership_status",                 "object",   "missing",   None                               ), #dropped: 100% missings
    # "lnd_ten06":      ("land_other_ownership_status",                     "object",   "missing",   None                               ),
    "lnd_16":          ("land_used_as_collateral",                          "float32",  "dummy",     None                               ),
    "num_plots":       ("land_number_of_plots",                             "float32",  0,           None                               ),
}

CROP_PRODUCTION_2023 = {
    "interview__key":     ("interview_key",                    "object",  None,        None),
    # "r_crop__id":       ("crop_type",                        "object",  "missing",   None),#not necessary to know the specific crop
    "crop_harvest":       ("crop_harvested",                   "float32", "dummy",     None),
    # "crop_output":      ("crop_harvest_amount",              "float32", 0,           None),
    # "crop_unit":        ("crop_harvest_unit",                "object",  "missing",   None),
    # "crop_unit_1":      ("crop_harvest_unit_other",          "object",  None,        None),
    "crop_sale":          ("crop_sale",                        "float32", "dummy",     None),
    "crop_saleamt":       ("crop_sale_amount",                 "float32", 0,           None),
    # "crop_slunits":     ("crop_sale_unit",                   "object",  "missing",   None),
    # "crop_slunits_1":   ("crop_sale_unit_other",             "object",  None,        None),
    "crop_price":         ("crop_sale_price_per_unit",         "float32", 0,           None),
    "crop_homecons":      ("crop_home_consumption_amount",     "float32", 0,           None),
    # "crop_clunits":     ("crop_home_consumption_unit",       "object",  "missing",   None),
    # "crop_cunits_1":    ("crop_home_consumption_unit_other", "object",  None,        None),
    "cp_stor":            ("crop_storage",                     "float32", "dummy",     None),
    # "cpamt":            ("crop_storage_amount",              "float32", 0,           None),
    # "cpunits2":         ("crop_storage_unit",                "object",  "missing",   None),
    # "cpunits2_other":   ("crop_storage_unit_other",          "object",  None,        None),
    "crop_buyer__1":      ("crop_buyer_market",                "float32", "dummy",     None),
    "crop_buyer__2":      ("crop_buyer_trader",                "float32", "dummy",     None),
    "crop_buyer__3":      ("crop_buyer_cooperative",           "float32", "dummy",     None),
    "crop_buyer__4":      ("crop_buyer_commercial_farm",       "float32", "dummy",     None),
    "crop_buyer__5":      ("crop_buyer_hospitality",           "float32", "dummy",     None),
    "crop_buyer__6":      ("crop_buyer_government",            "float32", "dummy",     None),
    # "crop_buyer_other": ("crop_buyer_other",                 "object",  None,        None),
    "cp07":               ("crop_organic_fertilizer",          "float32", "dummy",     None),
    "cp08":               ("crop_inorganic_fertilizer",        "float32", "dummy",     None),
    "cp09":               ("crop_pesticides",                  "float32", "dummy",     None),
    "cp11":               ("crop_tractor",                     "float32", "dummy",     None),
}

CROP_EXPENDITURE_2023 = {
    "interview__key":   ("interview_key",                       "object",   None,   None),
    "crp_ip1_exp":      ("crop_exp_seeds_last_12_months",       "float32",  0,      None),
    "crp_ip3_exp":      ("crop_exp_fertilizer_last_12_months",  "float32",  0,      None),
    "crp_ip5_exp":      ("crop_exp_pesticide_last_12_months",   "float32",  0,      None),
    "crp_ip6_exp":      ("crop_exp_machinery_last_12_months",   "float32",  0,      None),
    "crp_ip7_exp":      ("crop_exp_hired_labor_last_12_months", "float32",  0,      None),
    "crp_ip8_exp":      ("crop_exp_land_rental_last_12_months", "float32",  0,      None),
    "crp_ip9_exp":      ("crop_exp_transport_last_12_months",   "float32",  0,      None),
    "crp_ip10_exp":     ("crop_exp_other_last_12_months",       "float32",  0,      None),
}

MARKET_ACCESS_2023 = {
    "interview__key":        ("interview_key",                    "object",     None,       None),
    "markt_output_dist":     ("market_output_distance_in_km",     "float32",    99999,      None), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_input_dist":      ("market_input_distance_in_km",      "float32",    99999,      None), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_buyer":           ("market_type",                      "object",     "missing",  None),
    # "markt_buyer_oth":     ("market_type_other",                "object",     None,       None),
    "crop_contract":         ("crop_contract",                    "float32",    "dummy",    None),
    "contract_crop":         ("crop_contract_crop_type",          "object",     "missing",  None),
    "input_access_subsidy":  ("subsidy",                          "float32",    "dummy",    None),
    "subsidy_type__1":       ("subsidy_type_seeds",               "float32",    "dummy",    None),
    "subsidy_type__2":       ("subsidy_type_fertilizer",          "float32",    "dummy",    None),
    "subsidy_type__3":       ("subsidy_type_agro_chemicals",      "float32",    "dummy",    None),
    "subsidy_type__4":       ("subsidy_type_interest_free_loan",  "float32",    "dummy",    None),
    "subsidy_supplier__1":   ("subsidy_supplier_government",      "float32",    "dummy",    None),
    "subsidy_supplier__2":   ("subsidy_supplier_ngos",            "float32",    "dummy",    None),
    "subsidy_supplier__3":   ("subsidy_supplier_company",         "float32",    "dummy",    None),
    # "subsidy_supplier_oth": ("subsidy_supplier_other",          "object",     None,       None),
}

LIVESTOCK_OWNERSHIP_2023 = {
    "interview__key":        ("interview_key",                              "object",  None,        None                                    ),
    "r_livestock__id":       ("livestock_type",                             "object",  "missing",   mappings.livestock_conversion_factors   ),
    "lv02":                  ("livestock_number_owned",                     "float32", 0,           None                                    ),
    "lv03":                  ("livestock_number_sold",                      "float32", 0,           None                                    ),
    "lv06":                  ("livestock_number_lost_disease_theft",        "float32", 0,           None                                    ),
    "lv07":                  ("livestock_number_lost_wildlife_attack",      "float32", 0,           None                                    ), 
    "lv08":                  ("livestock_price_head_sold",                  "float32", 0,           None                                    ),
}

LIFESTOCK_GRAZING_2023 = {
    "interview__key":            ("interview_key",                                    "object",     None,       None),
    "grazing_dist":              ("grazing_distance_in_min",                          "float32",    0,          None),
    "grazing_days":              ("grazing_time_in_min",                              "float32",    0,          None),
    "grazing_hour":              ("grazing_time_hours_per_day",                       "float32",    0,          None),
    "grazing_ownership":         ("grazing_land_ownership_status",                    "object",     "missing",  None),
    "grazing_sharing":           ("grazing_land_number_hh_sharing",                   "float32",    0,          None),
    "grazing_permit":            ("grazing_land_permit",                              "float32",    "dummy",    None), 
    "grazing_permit_price":      ("grazing_land_permit_price",                        "float32",    0,          None),
    "grazing_years":             ("grazing_land_use_duration_in_years",               "float32",    0,          None),
    "grazing_challenges__1":     ("grazing_land_challenges_little_gras",              "float32",    "dummy",    None),
    "grazing_challenges__2":     ("grazing_land_challenges_prosopis_parthenium",      "float32",    "dummy",    None), 
    "grazing_challenges__3":     ("grazing_land_challenges_other_pastoralists",       "float32",    "dummy",    None), 
    "grazing_challenges__4":     ("grazing_land_challenges_ethnic_conflict",          "float32",    "dummy",    None), 
    "grazing_challenges__5":     ("grazing_land_challenges_tension_conflict",         "float32",    "dummy",    None), 
    "grazing_challenges__6":     ("grazing_land_challenges_theft",                    "float32",    "dummy",    None), 
    "grazing_challenges__7":     ("grazing_land_challenges_raiding",                  "float32",    "dummy",    None), 
    "grazing_challenges__8":     ("grazing_land_challenges_no_water",                 "float32",    "dummy",    None), 
    "grazing_challenges__9":     ("grazing_land_challenges_too_far",                  "float32",    "dummy",    None), 
    "grazing_challenges__10":    ("grazing_land_challenges_expensive",                "float32",    "dummy",    None), 
    "grazing_challenges__11":    ("grazing_land_challenges_None",                     "float32",    "dummy",    None), 
    # "grazing_challenge_other": ("grazing_land_challenges_other",                    "object",     None,       None),
}

LIFESTOCK_INCOME_2023 = {
    "interview__key":       ("interview_key",                                "object",      None,      None),
    "liv_pdtsal":           ("livestock_products_sold_last_12_months",       "float32",     "dummy",   None),
    "which_liv_pdts__1":    ("livestock_products_sold_meat",                 "float32",     "dummy",   None),
    "which_liv_pdts__2":    ("livestock_products_sold_milk",                 "float32",     "dummy",   None),
    "which_liv_pdts__3":    ("livestock_products_sold_cheese",               "float32",     "dummy",   None),
    "which_liv_pdts__4":    ("livestock_products_sold_yogurt",               "float32",     "dummy",   None),
    "which_liv_pdts__5":    ("livestock_products_sold_wool",                 "float32",     "dummy",   None),
    "which_liv_pdts__6":    ("livestock_products_sold_honey_wax",            "float32",     "dummy",   None),
    "which_liv_pdts__7":    ("livestock_products_sold_eggs",                 "float32",     "dummy",   None),
    # "which_liv_pdts_oth": ("livestock_products_sold_other",                "object",      None,      None),
    "liv_buyer":            ("livestock_products_buyer",                     "object",      "missing", None),
    # "liv_buyer_oth":       ("livestock_products_buyer_other",              "object",      None,      None),
    "liv_buyer_where":      ("livestock_products_market_type",               "object",      "missing", None),
    "livmkt_dist":          ("livestock_market_distance_in_km",              "float32",     0,         None),
    "liv_pdt_inc":          ("livestock_income_last_12_months",              "float32",     0,         None),
    "liv_contract":         ("livestock_contract",                           "float32",     "dummy",   None),
}

LIFESTOCK_EXPENDITURE_2023 = {
    "interview__key":     ("interview_key",                     "object",   None, None),
    "lvexp01_11":         ("livestock_exp_feed_fodder",         "float32",  0,    None),
    "lvexp02_12":         ("livestock_exp_rent_gazing_land",    "float32",  0,    None),
    "lvexp03_13":         ("livestock_exp_veterinary_services", "float32",  0,    None),
    "lvexp04_14":         ("livestock_exp_shelter",             "float32",  0,    None),
    "lvexp05_15":         ("livestock_exp_hired_labor",         "float32",  0,    None),
    # "lvexp06_16":       ("livestock_exp_other",               "float32",  0,    None),
}

HOUSING_CONDITIONS_2023 = {
    "interview__key":    ("interview_key",                  "object",  None,      None),
    "h02":               ("house_room_number",              "float32", 0,         None),
    "h03":               ("house_roof_material",            "object",  "missing", None),
    # "h03_oth":         ("house_roof_material_other",      "object",  None,      None),
    "h04":               ("house_wall_material",            "object",  "missing", None),
    # "h04_oth":         ("house_wall_material_other",      "object",  None,      None),
    "h05":               ("house_floor_material",           "object",  "missing", None),
    # "h05_oth":         ("house_floor_material_other",     "object",  None,      None),
    "h06":               ("house_water_source",             "object",  "missing", None),
    # "h06_oth":         ("house_water_source_other",       "object",  None,      None),
    "h07":               ("house_toilet_type",              "object",  "missing", None),
    # "h07_oth":         ("house_toilet_type_other",        "object",  None,      None),
}

ENERGY_ACCESS_2023 = {
    "interview__key":    ("interview_key",                              "object", None,      None),
    "h09":               ("house_energy_source",                        "object", "missing", None),
    # "h09_oth":         ("house_energy_source_other",                  "object", None,      None),
    "h10":               ("house_energy_source_for_cooking",            "object", "missing", None),
    # "h10_1":           ("house_energy_source_for_cooking_other",      "object", None,      None),
    "h11":               ("house_energy_source_for_lighting",           "object", "missing", None),
    # "h11_1":           ("house_energy_source_for_lighting_other",     "object", None,      None),
}

ASSETS_OWNED_2023 = {
    "interview__key":    ("interview_key",          "object",  None,      None),
    "r_asset_own__id":   ("asset_type",             "object",  "missing", None),
    "ha0_1":             ("asset_number_owned",     "float32", 0,         None),
    "ha0_4":             ("asset_price_per_unit",   "float32", 0,         None), #TODO: using mean per asset_type would be better!
}

INTERNET_ACCESS_2023 = {
    "interview__key":    ("interview_key",                          "object",   None,   None),
    "access_internet":   ("internet_access",                        "float32",  "dummy", None),
    "internet_home":     ("internet_access_at_home",                "float32",  "dummy", None),
    # "distance_internet": ("internet_access_distance_in_meters",     "float32", None,    None), #dropped: 100% missings
    #TODO: What Types of Online Activities Do you Engage in when using the Internet? Available
}

SHOCKS_AND_COPING_2023 = {
    "interview__key":   ("interview_key",                                       "object",  None, None),
    # "r_shocks__id":   ("shock_id",                                            "object",  None, None),
    "r_shocks":         ("shock_type_affected_last_12_months",                  "object",  None, None),
    "sh_1":             ("shock_frequency_last_12_months",                      "float32", None, None),
    "sh_2":             ("shock_severity_last_12_months",                       "object",  None, None),

    #COPING
    "sh_3__1":           ("shock_coping_strategy_relatives_friends",            "object",  None, None),
    "sh_3__2":           ("shock_coping_strategy_government",                   "object",  None, None),
    "sh_3__3":           ("shock_coping_strategy_food_reduction",               "object",  None, None),
    "sh_3__4":           ("shock_coping_strategy_changed_cropping_practices",   "object",  None, None),
    "sh_3__5":           ("shock_coping_strategy_more_employment",              "object",  None, None),
    "sh_3__6":           ("shock_coping_strategy_hh_member_migration",          "object",  None, None),
    "sh_3__7":           ("shock_coping_strategy_savings",                      "object",  None, None),
    "sh_3__8":           ("shock_coping_strategy_insurance",                    "object",  None, None),
    "sh_3__9":           ("shock_coping_strategy_credit",                       "object",  None, None),
    "sh_3__10":          ("shock_coping_strategy_sold_hh_assets",               "object",  None, None),
    "sh_3__11":          ("shock_coping_strategy_sold_livestock",               "object",  None, None),
    "sh_3__12":          ("shock_coping_strategy_migration",                    "object",  None, None),
    "sh_3__13":          ("shock_coping_strategy_police_report",                "object",  None, None),
    "sh_3__14":          ("shock_coping_strategy_nothing",                      "object",  None, None),
    # "sh_3_oth":        ("shock_coping_strategy_other",                        "object",  None, None),

    "sh_4":              ("shock_future_likelihood_well_prepared",              "object",  None, None),
    "sh_5":              ("shock_future_likelihood_recover_fully",              "object",  None, None),
    "sh_6":              ("shock_future_likelihood_change_income_source",       "object",  None, None),
}

SOCIAL_NETWORK_2023 = {
    "interview__key":   ("interview_key",                           "object",   None,    None),
    "as19":             ("mobile_money_access",                     "float32",  "dummy", None),
    "as18__1":          ("membership_farmers_group",                "float32",  "dummy", None),
    "as18__2":          ("membership_agricultural_cooperative",     "float32",  "dummy", None),
}

SOCIAL_EMBEDDEDNESS_2023 = {
    # ONLY RESPONDAND ASEKD:CAN BE USED AS A PROXY FOR THE OPTIMISM OF THE HH
    "interview__key":   ("interview_key",                                "object",  None,      None),
    "as_loc01_in":      ("my_life_course_depends_on_me",                 "object",  "missing", None),
    "as_loc02_in":      ("success_is_hard_work",                         "object",  "missing", None),
    "as_loc03_in":      ("ability_is_more_important_than_effort",        "object",  "missing", None),
    "as_loc04_in":      ("my_plans_will_work",                           "object",  "missing", None),
    "as_loc06_in":      ("I_can_shape_my_future_positively",             "object",  "missing", None),
    "as_loc12_in":      ("I_am_optimistic_about_my_future",              "object",  "missing", None),
    "as_loc13_in":      ("I_am_optimistic_about_my_familys_future",      "object",  "missing", None),
    "exp_ev1_01":       ("worry_about_job_loss_or_economic_livelihood",  "object",  "missing", None),
}

FOOD_INSECURITY_2023 = {
    "interview__key":       ("interview_key",                    "object",      None, None),
    "food_sufficent":       ("sufficent_food_number_of_month",   "float32",     0,    None),
    #TODO: During the Last 12 Months, Was There a Time When, Because of Lack of Money or Ot... available!
}

OTHER_INCOME_SOURCES_2023 = {
    "interview__key":       ("interview_key",           "object",  None,      None                      ),
    "r_otherincome__id":    ("other_income_source",     "object",  "missing", None                      ),
    "inc_oth_amt":          ("other_income_amount",     "float32", "mean",    None                      ), #TODO: using mean per income source would be better!
    "int_oth_income":       ("other_income_frequency",  "object",  "missing", mappings.income_frequency ),
}

ROAD_CONNECTIVITY_2023 = {
    "interview__key":       ("interview_key",               "object",  None,   None),
    "road_1":               ("road_type",                   "object",  "missing", None),
    "road_2":               ("road_condition",              "object",  "missing", None),
    "road_6":               ("road_distance_in_minutes",    "float32", "mean",    None), #very little missings, so mean is a save option!
}

# ============================================================
# INDIVIDUAL-LEVEL FEATURES
# ============================================================

HH_MEMBERS_2023 = {
    "interview__key":   ("interview_key",        "object",  None,       None                        ),
    "r_members__id":    ("members_id",           "object",  None,       None                        ),
    "ha03":             ("gender",               "object",  "missing",  None                        ),
    "ha_rel":           ("relation_to_head",     "object",  "missing",  None                        ),
    "age":              ("age",                  "float32", "mean",     None                        ),
    "ha07":             ("ethnic_group",         "object",  "missing",  None                        ),
    # "ha07_other":     ("ethnic_group_new",     "object",  "missing",  None                        ),
    "religio":          ("religion",             "object",  "missing",  None                        ),
    # "religio_1":      ("religion_other",       "object",  "missing",  None                        ),
    "educ1":            ("education_level",      "object",  "missing",  mappings.education_mapping  ),
}

OFF_FARM_EMPLOYMENT_2023 = {
    "interview__key":           ("interview_key",                                   None, None, None),
    "r_members__id":            ("members_id",                                      None, None, None),
    "lbr3_1":                   ("sector_off_farm_empl_last_12_months",             None, None, None),
    # "lbr3_1_oth":             ("sector_off_farm_empl_last_12_months_other",       None, None, None),
    "emp_form":                 ("empl_type",                                       None, None, None),

    #SELF-EMPLOYMENT / OWN BUSINESS
    "bus_yr":                   ("self_empl_duration_in_months",                    None, None, None),
    # "bus_dry":                ("self_empl_duration_dry_season_in_months",         None, None, None),
    # "bus_rain":               ("self_empl_duration_rainy_season_in_months",       None, None, None),
    "bus_days_wk":              ("self_empl_days_per_week",                         None, None, None),
    "bus_hrs":                  ("self_empl_hours_per_day",                         None, None, None),
    # "bus_sales":              ("self_empl_sales",                                 None, None, None), #per week? per months?
    # "bus_main_use__1":        ("self_empl_main_use_invest_in_own_business",       None, None, None),
    # "bus_input":              ("self_empl_input_costs",                           None, None, None), #per week? per months?
    # "bus_labor":              ("self_empl_labor_costs",                           None, None, None), #per week? per months?
    # "bus_capital":            ("self_empl_capital_costs",                         None, None, None), #Machinery Maintenance, Rent #per week? per months?
    # "bus_reg":                ("self_empl_registered",                            None, None, None),
    # "bus_loc":                ("self_empl_location",                              None, None, None),
    # "bus_employees":          ("self_empl_number_of_employees",                   None, None, None),
    # "tourism_motivate__1":    ("self_empl_motivation_previous_experience",        None, None, None),
    "tourism_motivate__2":      ("self_empl_motivation_others_success",             None, None, None),
    # "tourism_motivate__3":    ("self_empl_motivation_unclear",                    None, None, None),  #what dis this "Figure that this Kind.."?
    "tourism_motivate__4":      ("self_empl_motivation_unemployment",               None, None, None),
    "tourism_motivate__5":      ("self_empl_motivation_insufficient_income_1",      None, None, None), # from what? agriculture?
    "tourism_motivate__6":      ("self_empl_motivation_insufficient_income_2",      None, None, None), # from what? agriculture?
    "tourism_motivate__7":      ("self_empl_motivation_insufficient_income_3",      None, None, None), # from what? agriculture?
    "tourism_motivate__8":      ("self_empl_motivation_inherited_business",         None, None, None),
    # "tourism_motivate_oth":   ("self_empl_motivation_other",                      None, None, None),
    "years_exp_agri":           ("self_empl_years_experience_in_years",             None, None, None),
    # "business_obstacle__1":   ("self_empl_obstacle_1",                            None, None, None), # what is it?
    # "business_obstacle__2":   ("self_empl_obstacle_2",                            None, None, None), # what is it?
    # "business_obstacle__3":   ("self_empl_obstacle_3",                            None, None, None), # what is it?
    # "business_obstacle__4":   ("self_empl_obstacle_4",                            None, None, None), # what is it?
    # "business_obstacle__5":   ("self_empl_obstacle_5",                            None, None, None), # what is it?
    # "business_obstacle__6":   ("self_empl_obstacle_6",                            None, None, None), # what is it?
    # "business_obstacle__7":   ("self_empl_obstacle_7",                            None, None, None), # what is it?
    # "business_obstacle__8":   ("self_empl_obstacle_8",                            None, None, None), # what is it?
    # "business_obstacle__9":   ("self_empl_obstacle_9",                            None, None, None), # what is it?
    # "business_obstacle__10":  ("self_empl_obstacle_10",                           None, None, None), # what is it?
    # "business_obstacle__11":  ("self_empl_obstacle_11",                           None, None, None), # what is it?
    # "business_obs_other":     ("self_empl_obstacle_other",                        None, None, None),
    # "business_financing__1":  ("self_empl_three_main_financing_contraints_1",     None, None, None), # what is it?
    # "business_financing__2":  ("self_empl_three_main_financing_contraints_2",     None, None, None), # what is it?
    # "business_financing__3":  ("self_empl_three_main_financing_contraints_3",     None, None, None), # what is it?
    # "business_financing__4":  ("self_empl_three_main_financing_contraints_4",     None, None, None), # what is it?
    # "business_financing__5":  ("self_empl_three_main_financing_contraints_5",     None, None, None), # what is it?
    # "business_financing__6":  ("self_empl_three_main_financing_contraints_6",     None, None, None), # what is it?
    # "business_financing__7":  ("self_empl_three_main_financing_contraints_7",     None, None, None), # what is it?
    # "business_financing__8":  ("self_empl_three_main_financing_contraints_8",     None, None, None), # what is it?
    # "business_financing__9":  ("self_empl_three_main_financing_contraints_9",     None, None, None), # what is it?
    # "business_financing__10": ("self_empl_three_main_financing_contraints_10",    None, None, None), # what is it?
    # "business_financing__11": ("self_empl_three_main_financing_contraints_11",    None, None, None), # what is it?
    # "business_financing__12": ("self_empl_three_main_financing_contraints_12",    None, None, None), # what is it?
    # "business_financing_oth": ("self_empl_three_main_financing_contraints_other", None, None, None),
    # "business_finance__1":    ("self_empl_loan_source_1",                         None, None, None), # what is it?
    # "business_finance__2":    ("self_empl_loan_source_2",                         None, None, None), # what is it?
    # "business_finance__3":    ("self_empl_loan_source_3",                         None, None, None), # what is it?
    # "business_finance__4":    ("self_empl_loan_source_4",                         None, None, None), # what is it?
    # "business_finance__5":    ("self_empl_loan_source_5",                         None, None, None), # what is it?
    # "business_finance__6":    ("self_empl_loan_source_6",                         None, None, None), # what is it?
    # "business_finance__7":    ("self_empl_loan_source_7",                         None, None, None), # what is it?
    # "business_finance__8":    ("self_empl_loan_source_8",                         None, None, None), # what is it?
    # "business_finance_oth":   ("self_empl_loan_source_other",                     None, None, None),
    
    #WAGE EMPLOYMENT
    # "lbr3_2":                 ("wage_empl_company_name",                          None, None, None),
    "lbr3_3":                   ("wage_empl_location",                              None, None, None),
    "lbr3_4":                   ("wage_empl_type",                                  None, None, None),
    "lbr3_5":                   ("wage_empl_permament_wage_per_month",              None, None, None),
    "lbr3_6":                   ("wage_empl_permament_days_per_week",               None, None, None),
    "lbr3_7":                   ("wage_empl_permament_hours_per_day",               None, None, None),
    # "lbr3_8":                 ("wage_empl_seasonal_payment_frequency",            None, None, None),
    "lbr3_9":                   ("wage_empl_seasonal_wage",                         None, None, None),
    # "lbr3_10":                ("wage_empl_seasonal_duration_in_months_1",         None, None, None), # what is this?
    # "lbr3_11":                ("wage_empl_seasonal_duration_in_months_2",         None, None, None), # what is this?
    "lbr3_12":                  ("wage_empl_seasonal_duration_days_per_week",       None, None, None),
    "lbr3_13":                  ("wage_empl_seasonal_duration_hours_per_day",       None, None, None),
    
    "lbr10":                    ("wage_empl_contract_status",                       None, None, None),
    # "lbr10_1":                ("wage_empl_contract_status_other",                 None, None, None),
    # "job_search":             ("wage_empl_job_search",                            None, None, None),
    # "job_search_oth":         ("wage_empl_job_search_other",                      None, None, None),
    # "lbr09":                  ("wage_empl_training_received",                     None, None, None),
    # "emp_years":              ("wage_empl_duration_in_years",                     None, None, None),
}

ON_FARM_EMPLOYMENT_2023 = {
    "interview__key": ("interview_key",                                        None, None, None),
    "r_members__id":  ("members_id",                                           None, None, None),
    "lbr13":          ("farm_empl_last_12_months",                             None, None, None),

    #CROPS
    # "Ibr13_1":      ("farm_empl_cash_crops_duration_rainy_season_in_months", None, None, None),
    # "Ibr13_2":      ("farm_empl_cash_crops_duration_dry_season_in_months",   None, None, None),
    "Ibr13_3":        ("farm_empl_cash_crops_days_per_week",                   None, None, None),
    "Ibr13_4":        ("farm_empl_cash_crops_hours_per_day",                   None, None, None),
    # "Ibr13_5":      ("farm_empl_food_crops_duration_rainy_season_in_months", None, None, None),
    # "Ibr13_6":      ("farm_empl_food_crops_duration_dry_season_in_months",   None, None, None),
    "Ibr13_8":        ("farm_empl_food_crops_days_per_week",                   None, None, None),
    "Ibr13_9":        ("farm_empl_food_crops_hours_per_day",                   None, None, None),
    "years_exp_crp":  ("farm_empl_crops_years_experience_in_years",            None, None, None),

    #LIVESTOCK
    # "Ibr13_10":     ("farm_empl_livestock_duration_in_months_1",             None, None, None), # what time horizon?
    # "Ibr13_11":     ("farm_empl_livestock_duration_in_months_2",             None, None, None), # what time horizon?
    # "Ibr13_12":     ("farm_empl_livestock_duration_in_months_3",             None, None, None), # what time horizon?
    # "Ibr13_13":     ("farm_empl_livestock_duration_in_months_4",             None, None, None), # what time horizon?
    "years_exp_liv":  ("farm_empl_livestock_years_experience_in_years",        None, None, None),
}

MIGRATION_2023 = {
    "interview__key": ("interview_key",     None, None, None),
    "r_members__id":  ("members_id",        None, None, None),
    # "remit_amt":    ("remittance_amount", None, None, None),
}

ASPIRATIONS_2023 = {
    "interview__key":       ("interview_key",                          None, None, None),
    "r_members__id":        ("members_id",                             None, None, None),
    "as01":                 ("beans_allocated_to_empl_occupation",     None, None, None),
    "asp_occup":            ("aspired_occupation_5_years_ahead",       None, None, None),
    # "life_satisfaction":  ("life_satisfaction",                      None, None, None),
    "aspire_cont_farm":     ("aspiration_continue_farming",            None, None, None), #includes partly and full exit ## is it also 5 years?!
    
    #AGRICULTURAL LOAN
    "agri_loan":            ("agriculture_loan_last_5_years",          None, None, None),
    "agri_loan_amt":        ("agriculture_loan_amount",                None, None, None),
    # "agri_loan_lndr__1":  ("agriculture_loan_lender_bank",           None, None, None),
    # "agri_loan_lndr__2":  ("agriculture_loan_lender_credit_union",   None, None, None),
    # "agri_loan_lndr__3":  ("agriculture_loan_lender_private_lender", None, None, None),
    # "agri_loan_lndr__4":  ("agriculture_loan_lender_government",     None, None, None),
    # "agri_loan_lndr__5":  ("agriculture_loan_lender_ngos",           None, None, None),
    # "agri_loan_lndr_oth": ("agriculture_loan_lender_other",          None, None, None),
}

CHILD_ASPIRATIONS_2023 = {
    "interview__key":     ("interview_key",                     None, None, None),
    "r_members__id":      ("members_id",                        None, None, None),
    "r_child__id":        ("child_id",                          None, None, None),
    # "asocp01":          ("child_aspiration_occupation",       None, None, None), #open ended!
    "youth_child_tofarm": ("child_aspiration_continue_farming", None, None, None),
}
