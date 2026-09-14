"""FEATURE DICTIONARIES.

Each dictionary maps: {original_col_name: (new_name, dtype, dummy, mapping)}
    - new_name:   the desired name for the column.
    - dtype:      the desired datatype for the column.
    - dummy:      set to "dummy" if a Yes/No answer should be converted into a dummy of 1/0, otherwise None; ONLY COMBINE IT WITH dtype = "float64"!
    - mapping:    how to convert the values based on a pre-defined mapping (None for no mapping)
"""
from c08_farming_exit import mappings

# ============================================================
# HOUSEHOLD-LEVEL FEATURES
# ============================================================

IDENTIFYING_INFO_2023 = {
    "ctry":           ("country",                                      "object",   None,        None),
    "interview__key": ("interview_key",                                "object",   None,        None),
    #"hhid":          ("hhid",                                         "object",   None,        None),
    "ea":             ("enumeration_area",                             "object",   None,        None),
    "dist":           ("district",                                     "object",   None,        None),
    "region":         ("region",                                       "object",   None,        None),
    "res_head":       ("respondant_head_or_representative",            "object",   None,        None), 
    "res_rel":        ("respondant_representative_relation_to_head",   "object",   None,        None), 
}

LAND_OWNERSHIP_ACCESS_2023 = {
    "interview__key":  ("interview_key",                                    "object",   None,           None                               ),
    "lnd_mes":         ("land_measurement",                                 "object",   None,           mappings.acres_conversion_factors  ),
    # "lnd_mes_1":     ("land_measurement_other",                           "object",   None,           None                               ),
    "lnd01":           ("land_size_cropland",                               "float64",  None,           None                               ),
    "lnd02":           ("land_size_fallow",                                 "float64",  None,           None                               ),
    "lnd03":           ("land_size_agroforestry_forestry",                  "float64",  None,           None                               ),
    "lnd04":           ("land_size_pasture",                                "float64",  None,           None                               ),
    "lnd08":           ("land_size_residential",                            "float64",  None,           None                               ),
    "lnd09":           ("land_size_lodge_camp",                             "float64",  None,           None                               ),
    # "lnd06":         ("land_size_other",                                  "float64",  None,           None                               ),
    "lnd_ten01":       ("land_cropland_ownership_status",                   "object",   None,           mappings.ownership                 ),
    # "lnd_ten02":     ("land_fallow_ownership_status",                     "object",   None,           None                               ), #dropped: 60-90% missings
    # "lnd_ten03":     ("land_agroforestry_forestry_ownership_status",      "object",   None,           None                               ), #dropped: >90% missings
    # "lnd_ten04":     ("land_pasture_ownership_status",                    "object",   None,           None                               ), #dropped: >90% missings
    "lnd_ten08":       ("land_residential_ownership_status",                "object",   None,           mappings.ownership                 ),
    # "lnd_ten09":     ("land_lodge_camp_ownership_status",                 "object",   None,           None                               ), #dropped: 100% missings
    # "lnd_ten06":      ("land_other_ownership_status",                     "object",   None,           None                               ),
    "lnd_16":          ("land_used_as_collateral",                          "float64",  "dummy",        None                               ),
    "num_plots":       ("land_number_of_plots",                             "float64",  None,           None                               ),
}

CROP_PRODUCTION_2023 = {
    "interview__key":     ("interview_key",                    "object",  None,         None),
    "r_crop__id":         ("crop_type",                        "object",  None,         None),
    "crop_harvest":       ("crop_harvested",                   "float64", "dummy",      None),
    # "crop_output":      ("crop_harvest_amount",              "float64", None,         None),
    # "crop_unit":        ("crop_harvest_unit",                "object",  None,         None),
    # "crop_unit_1":      ("crop_harvest_unit_other",          "object",  None,         None),
    "crop_sale":          ("crop_sale",                        "float64", "dummy",      None),
    "crop_saleamt":       ("crop_sale_amount",                 "float64", None,         None),
    # "crop_slunits":     ("crop_sale_unit",                   "object",  None,         None),
    # "crop_slunits_1":   ("crop_sale_unit_other",             "object",  None,         None),
    "crop_price":         ("crop_sale_price_per_unit",         "float64", None,         None),
    "crop_homecons":      ("crop_home_consumption_amount",     "float64", None,         None),
    # "crop_clunits":     ("crop_home_consumption_unit",       "object",  None,         None),
    # "crop_cunits_1":    ("crop_home_consumption_unit_other", "object",  None,         None),
    "cp_stor":            ("crop_storage",                     "float64", None,         None),
    # "cpamt":            ("crop_storage_amount",              "float64", None,         None),
    # "cpunits2":         ("crop_storage_unit",                "object",  None,         None),
    # "cpunits2_other":   ("crop_storage_unit_other",          "object",  None,         None),
    "crop_buyer__1":      ("crop_buyer_market",                "float64", "dummy",      None),
    "crop_buyer__2":      ("crop_buyer_trader",                "float64", "dummy",      None),
    "crop_buyer__3":      ("crop_buyer_cooperative",           "float64", "dummy",      None),
    "crop_buyer__4":      ("crop_buyer_commercial_farm",       "float64", "dummy",      None),
    "crop_buyer__5":      ("crop_buyer_hospitality",           "float64", "dummy",      None),
    "crop_buyer__6":      ("crop_buyer_government",            "float64", "dummy",      None),
    # "crop_buyer_other": ("crop_buyer_other",                 "object",  None,         None),
    "cp07":               ("crop_organic_fertilizer",          "float64", "dummy",      None),
    "cp08":               ("crop_inorganic_fertilizer",        "float64", "dummy",      None),
    "cp09":               ("crop_pesticides",                  "float64", "dummy",      None),
    "cp11":               ("crop_tractor",                     "float64", "dummy",      None),
}

CROP_EXPENDITURE_2023 = {
    "interview__key":   ("interview_key",                       "object",   None,      None),
    "crp_ip1_exp":      ("crop_exp_seeds_last_12_months",       "float64",  None,      None),
    "crp_ip3_exp":      ("crop_exp_fertilizer_last_12_months",  "float64",  None,      None),
    "crp_ip5_exp":      ("crop_exp_pesticide_last_12_months",   "float64",  None,      None),
    "crp_ip6_exp":      ("crop_exp_machinery_last_12_months",   "float64",  None,      None),
    "crp_ip7_exp":      ("crop_exp_hired_labor_last_12_months", "float64",  None,      None),
    "crp_ip8_exp":      ("crop_exp_land_rental_last_12_months", "float64",  None,      None),
    "crp_ip9_exp":      ("crop_exp_transport_last_12_months",   "float64",  None,      None),
    "crp_ip10_exp":     ("crop_exp_other_last_12_months",       "float64",  None,      None),
}

MARKET_ACCESS_2023 = {
    "interview__key":        ("interview_key",                    "object",     None,       None),
    "markt_output_dist":     ("market_output_distance_in_km",     "float64",    None,       None), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_input_dist":      ("market_input_distance_in_km",      "float64",    None,       None), #0-70% missings, too valueable to dismiss -> special treatment
    "markt_buyer":           ("market_type",                      "object",     None,       mappings.market_type),
    # "markt_buyer_oth":     ("market_type_other",                "object",     None,       None),
    "crop_contract":         ("crop_contract",                    "float64",    "dummy",    None),
    "contract_crop":         ("crop_contract_crop_type",          "object",     None,       None), #almost all MAIZE!
    "input_access_subsidy":  ("subsidy",                          "float64",    "dummy",    None),
    "subsidy_type__1":       ("subsidy_type_seeds",               "float64",    "dummy",    None),
    "subsidy_type__2":       ("subsidy_type_fertilizer",          "float64",    "dummy",    None),
    "subsidy_type__3":       ("subsidy_type_agro_chemicals",      "float64",    "dummy",    None),
    "subsidy_type__4":       ("subsidy_type_interest_free_loan",  "float64",    "dummy",    None),
    "subsidy_supplier__1":   ("subsidy_supplier_government",      "float64",    "dummy",    None),
    "subsidy_supplier__2":   ("subsidy_supplier_ngos",            "float64",    "dummy",    None),
    "subsidy_supplier__3":   ("subsidy_supplier_company",         "float64",    "dummy",    None),
    # "subsidy_supplier_oth": ("subsidy_supplier_other",          "object",     None,       None),
}

LIVESTOCK_OWNERSHIP_2023 = {
    "interview__key":        ("interview_key",                              "object",  None,        None                                    ),
    "r_livestock__id":       ("livestock_type",                             "object",  None,        mappings.livestock_conversion_factors   ),
    "lv02":                  ("livestock_number_owned",                     "float64", None,        None                                    ),
    "lv03":                  ("livestock_number_sold",                      "float64", None,        None                                    ),
    "lv06":                  ("livestock_number_lost_disease_theft",        "float64", None,        None                                    ),
    "lv07":                  ("livestock_number_lost_wildlife_attack",      "float64", None,        None                                    ), 
    "lv08":                  ("livestock_price_head_sold",                  "float64", None,        None                                    ),
}

LIFESTOCK_GRAZING_2023 = {
    "interview__key":            ("interview_key",                                    "object",     None,       None),
    "grazing_dist":              ("grazing_distance_in_min",                          "float64",    None,       None),
    "grazing_days":              ("grazing_time_in_min",                              "float64",    None,       None),
    "grazing_hour":              ("grazing_time_hours_per_day",                       "float64",    None,       None),
    "grazing_ownership":         ("grazing_land_ownership_status",                    "object",     None,       mappings.ownership),
    "grazing_sharing":           ("grazing_land_number_hh_sharing",                   "float64",    None,       None),
    "grazing_permit":            ("grazing_land_permit",                              "float64",    "dummy",    None), 
    "grazing_permit_price":      ("grazing_land_permit_price",                        "float64",    None,       None),
    "grazing_years":             ("grazing_land_use_duration_in_years",               "float64",    None,       None),
    "grazing_challenges__1":     ("grazing_land_challenges_little_gras",              "float64",    "dummy",    None),
    "grazing_challenges__2":     ("grazing_land_challenges_prosopis_parthenium",      "float64",    "dummy",    None), 
    "grazing_challenges__3":     ("grazing_land_challenges_other_pastoralists",       "float64",    "dummy",    None), 
    "grazing_challenges__4":     ("grazing_land_challenges_ethnic_conflict",          "float64",    "dummy",    None), 
    "grazing_challenges__5":     ("grazing_land_challenges_tension_conflict",         "float64",    "dummy",    None), 
    "grazing_challenges__6":     ("grazing_land_challenges_theft",                    "float64",    "dummy",    None), 
    "grazing_challenges__7":     ("grazing_land_challenges_raiding",                  "float64",    "dummy",    None), 
    "grazing_challenges__8":     ("grazing_land_challenges_no_water",                 "float64",    "dummy",    None), 
    "grazing_challenges__9":     ("grazing_land_challenges_too_far",                  "float64",    "dummy",    None), 
    "grazing_challenges__10":    ("grazing_land_challenges_expensive",                "float64",    "dummy",    None), 
    # "grazing_challenges__11":  ("grazing_land_challenges_None",                     "float64",    "dummy",    None), 
    # "grazing_challenge_other": ("grazing_land_challenges_other",                    "object",     None,       None),
}

LIFESTOCK_INCOME_2023 = {
    "interview__key":       ("interview_key",                                "object",      None,      None),
    "liv_pdtsal":           ("livestock_products_sold_last_12_months",       "float64",     "dummy",   None),
    "which_liv_pdts__1":    ("livestock_products_sold_meat",                 "float64",     "dummy",   None),
    "which_liv_pdts__2":    ("livestock_products_sold_milk",                 "float64",     "dummy",   None),
    "which_liv_pdts__3":    ("livestock_products_sold_cheese",               "float64",     "dummy",   None),
    "which_liv_pdts__4":    ("livestock_products_sold_yogurt",               "float64",     "dummy",   None),
    "which_liv_pdts__5":    ("livestock_products_sold_wool",                 "float64",     "dummy",   None),
    "which_liv_pdts__6":    ("livestock_products_sold_honey_wax",            "float64",     "dummy",   None),
    "which_liv_pdts__7":    ("livestock_products_sold_eggs",                 "float64",     "dummy",   None),
    # "which_liv_pdts_oth": ("livestock_products_sold_other",                "object",      None,      None),
    "liv_buyer":            ("livestock_products_buyer",                     "object",      None,      mappings.buyer_type),
    # "liv_buyer_oth":       ("livestock_products_buyer_other",              "object",      None,      None),
    "liv_buyer_where":      ("livestock_products_market_type",               "object",      None,      mappings.livestock_market_type),
    "livmkt_dist":          ("livestock_market_distance_in_km",              "float64",     None,      None),
    "liv_pdt_inc":          ("livestock_income_last_12_months",              "float64",     None,      None),
    "liv_contract":         ("livestock_contract",                           "float64",     "dummy",   None),
}

LIFESTOCK_EXPENDITURE_2023 = {
    "interview__key":     ("interview_key",                     "object",   None,    None),
    "lvexp01_11":         ("livestock_exp_feed_fodder",         "float64",  None,    None),
    "lvexp02_12":         ("livestock_exp_rent_gazing_land",    "float64",  None,    None),
    "lvexp03_13":         ("livestock_exp_veterinary_services", "float64",  None,    None),
    "lvexp04_14":         ("livestock_exp_shelter",             "float64",  None,    None),
    "lvexp05_15":         ("livestock_exp_hired_labor",         "float64",  None,    None),
    # "lvexp06_16":       ("livestock_exp_other",               "float64",  None,    None),
}

HOUSING_CONDITIONS_2023 = {
    "interview__key":    ("interview_key",                  "object",  None,      None),
    "h02":               ("house_room_number",              "float64", None,      None),
    "h03":               ("house_roof_material",            "object",  None,      mappings.roof_material),
    # "h03_oth":         ("house_roof_material_other",      "object",  None,      None),
    "h04":               ("house_wall_material",            "object",  None,      mappings.wall_material),
    # "h04_oth":         ("house_wall_material_other",      "object",  None,      None),
    "h05":               ("house_floor_material",           "object",  None,      mappings.floor_material),
    # "h05_oth":         ("house_floor_material_other",     "object",  None,      None),
    "h06":               ("house_water_source",             "object",  None,      mappings.water_source),
    # "h06_oth":         ("house_water_source_other",       "object",  None,      None),
    "h07":               ("house_toilet_type",              "object",  None,      mappings.toilet_type),
    # "h07_oth":         ("house_toilet_type_other",        "object",  None,      None),
}

ENERGY_ACCESS_2023 = {
    "interview__key":    ("interview_key",                              "object", None,      None),
    "h09":               ("house_energy_source",                        "object", None,      mappings.energy_source),
    # "h09_oth":         ("house_energy_source_other",                  "object", None,      None),
    "h10":               ("house_energy_source_for_cooking",            "object", None,      mappings.cooking_energy_source),
    # "h10_1":           ("house_energy_source_for_cooking_other",      "object", None,      None),
    "h11":               ("house_energy_source_for_lighting",           "object", None,      mappings.lighting_source),
    # "h11_1":           ("house_energy_source_for_lighting_other",     "object", None,      None),
}

ASSETS_OWNED_2023 = {
    "interview__key":    ("interview_key",          "object",  None,        None),
    "r_asset_own__id":   ("asset_type",             "object",  None,        None),
    "ha0_1":             ("asset_number_owned",     "float64", None,        None),
    "ha0_4":             ("asset_price_per_unit",   "float64", None,        None), #TODO: using mean per asset_type would be good!
}

INTERNET_ACCESS_2023 = {
    "interview__key":       ("interview_key",                          "object",   None,    None),
    "access_internet":      ("internet_access",                        "float64",  "dummy", None),
    "internet_home":        ("internet_access_at_home",                "float64",  "dummy", None),
    # "distance_internet":  ("internet_access_distance_in_meters",     "float64",  None,    None), #dropped: 100% missings
    "inter_activity__9":    ("internet_activity_pay_bills",            "float64",  "dummy", None),
    "inter_activity__10":   ("internet_activity_operate_business",     "float64",  "dummy", None),
    "cost_internet":        ("internet_monthly_cost",                  "float64",  None, None),
    #TODO: What Types of Online Activities Do you Engage in when using the Internet? Available
}

SHOCKS_AND_COPING_2023 = {
    "interview__key":   ("interview_key",                                       "object",  None,     None),
    # "r_shocks__id":   ("shock_id",                                            "object",  None,     None),
    "r_shocks":         ("shock_type_affected_last_12_months",                  "object",  None,     mappings.shock_categories),
    # "sh_1":           ("shock_frequency_last_12_months",                      "float64", None,     None), #kicked out for now to keep it simple
    # "sh_2":           ("shock_severity_last_12_months",                       "object",  None,     None), #kicked out for now to keep it simple

    #COPING
    "sh_3__1":          ("shock_coping_strategy_relatives_friends",             "float64", None,     None),
    "sh_3__2":          ("shock_coping_strategy_government",                    "float64", None,     None),
    "sh_3__3":          ("shock_coping_strategy_food_reduction",                "float64", None,     None),
    "sh_3__4":          ("shock_coping_strategy_changed_cropping_practices",    "float64", None,     None),
    "sh_3__5":          ("shock_coping_strategy_more_employment",               "float64", None,     None),
    "sh_3__6":          ("shock_coping_strategy_hh_member_migration",           "float64", None,     None),
    "sh_3__7":          ("shock_coping_strategy_savings",                       "float64", None,     None),
    "sh_3__8":          ("shock_coping_strategy_insurance",                     "float64", None,     None),
    "sh_3__9":          ("shock_coping_strategy_credit",                        "float64", None,     None),
    "sh_3__10":         ("shock_coping_strategy_sold_hh_assets",                "float64", None,     None),
    "sh_3__11":         ("shock_coping_strategy_sold_livestock",                "float64", None,     None),
    "sh_3__12":         ("shock_coping_strategy_migration",                     "float64", None,     None),
    # "sh_3__13":       ("shock_coping_strategy_police_report",                 "float64", None,     None), #kicked out for now to keep it simple
    # "sh_3__14":       ("shock_coping_strategy_nothing",                       "float64", None,     None), #kicked out for now to keep it simple
    # "sh_3_oth":       ("shock_coping_strategy_other",                         "float64", None,     None),

    # "sh_4":           ("shock_future_likelihood_well_prepared",               "object",  None,     None), #kicked out for now to keep it simple
    # "sh_5":           ("shock_future_likelihood_recover_fully",               "object",  None,     None), #kicked out for now to keep it simple
    "sh_6":             ("shock_future_likelihood_change_income_source",        "object",  None,     mappings.likelihood),
}

SOCIAL_NETWORK_2023 = {
    "interview__key":   ("interview_key",                           "object",   None,    None),
    "as19":             ("mobile_money_access",                     "float64",  "dummy", None),
    "as18__1":          ("membership_farmers_group",                "float64",  "dummy", None),
    "as18__2":          ("membership_agricultural_cooperative",     "float64",  "dummy", None),
}

SOCIAL_EMBEDDEDNESS_2023 = {
    # ONLY RESPONDAND ASKED:CAN BE USED AS A PROXY FOR THE OPTIMISM OF THE HH
    "interview__key":   ("interview_key",                                "object",  None, None),
    "as_loc01_in":      ("my_life_course_depends_on_me",                 "object",  None, mappings.agreement),  #positive 
    #"as_loc02_in":      ("success_is_hard_work",                         "object",  None, mappings.agreement), #difficult to interpret
    #"as_loc03_in":      ("ability_is_more_important_than_effort",        "object",  None, mappings.agreement), #difficult to interpret
    "as_loc04_in":      ("my_plans_will_work",                           "object",  None, mappings.agreement),  #positive 
    "as_loc06_in":      ("I_can_shape_my_future_positively",             "object",  None, mappings.agreement),  #positive 
    "as_loc12_in":      ("I_am_optimistic_about_my_future",              "object",  None, mappings.agreement),  #positive 
    "as_loc13_in":      ("I_am_optimistic_about_my_familys_future",      "object",  None, mappings.agreement),  #positive 
    "exp_ev1_01":       ("worry_about_job_loss_or_economic_livelihood",  "object",  None, mappings.worries),    #negative 
}

FOOD_INSECURITY_2023 = {
    "interview__key":       ("interview_key",                    "object",      None, None),
    "food_sufficent":       ("sufficent_food_number_of_month",   "float64",     None, None),
    #TODO: During the Last 12 Months, Was There a Time When, Because of Lack of Money or Ot... available!
}

OTHER_INCOME_SOURCES_2023 = {
    "interview__key":       ("interview_key",           "object",  None,        None                            ),
    "r_otherincome__id":    ("other_income_source",     "object",  None,        None                            ),
    "inc_oth_amt":          ("other_income_amount",     "float64", None,        None                            ), #TODO: using mean per income source would be good!
    "int_oth_income":       ("other_income_frequency",  "object",  None,        mappings.other_income_frequency ),
}

ROAD_CONNECTIVITY_2023 = {
    "interview__key":       ("interview_key",               "object",  None,    None),
    "road_1":               ("road_type",                   "object",  None,    mappings.road_type),
    "road_2":               ("road_condition",              "object",  None,    mappings.road_condition),
    "road_6":               ("road_distance_in_minutes",    "float64", None,    None), #very little missings, so mean is a save option!
}



# ============================================================
# INDIVIDUAL-LEVEL FEATURES
# ============================================================

HH_MEMBERS_2023 = {
    "interview__key":   ("interview_key",        "object",  None,       None                        ),
    "r_members__id":    ("members_id",           "object",  None,       None                        ),
    "ha03":             ("female",               "object",  None,       mappings.gender             ),
    "ha_rel":           ("relation_to_head",     "object",  None,       None                        ),
    "age":              ("age",                  "float64", None,       None                        ),
    "ha07":             ("ethnic_group",         "object",  None,       None                        ), #there are 129 different ethnic groups in the 5 countries, sure you want to keep this?
    # "ha07_other":     ("ethnic_group_new",     "object",  None,       None                        ),
    "religio":          ("religion",             "object",  None,       None                        ),
    # "religio_1":      ("religion_other",       "object",  None,       None                        ),
    "educ1":            ("years_of_schooling",   "object",  None,       mappings.years_of_schooling ),
}

OFF_FARM_EMPLOYMENT_2023 = {
    "interview__key":           ("interview_key",                                               "object",   None,   None),
    "r_members__id":            ("members_id",                                                  "object",   None,   None),
    "lbr3_1":                   ("sector_off_farm_empl_last_12_months",                         "object",   None,   mappings.employment_sector),
    # "lbr3_1_oth":             ("sector_off_farm_empl_last_12_months_other",                   "object",   None,   None),
    "emp_form":                 ("empl_type",                                                   "object",   None,   None), #Self-employed or employee

    #SELF-EMPLOYMENT / OWN BUSINESS
    # "bus_yr":                 ("self_empl_duration_in_months_last_12_months",                 "float64",  None,   None),
    "bus_dry":                  ("self_empl_duration_dry_season_in_months_last_12_months",      "float64",  None,   None),
    "bus_rain":                 ("self_empl_duration_rainy_season_in_months_last_12_months",    "float64",  None,   None), 
    "bus_days_wk":              ("self_empl_days_per_week",                                     "float64",  None,   None),
    "bus_hrs":                  ("self_empl_hours_per_day",                                     "float64",  None,   None),
    "bus_sales":                ("self_empl_sales_last_30_days",                                "float64",  None,   None),
    "bus_main_use__1":          ("self_empl_main_use_invest_in_own_business",                   "float64",  None,   None),
    "bus_main_use__2":          ("self_empl_main_use_food",                                     "float64",  None,   None),
    "bus_main_use__3":          ("self_empl_main_use_education",                                "float64",  None,   None),
    "bus_main_use__4":          ("self_empl_main_use_health",                                   "float64",  None,   None),
    "bus_main_use__5":          ("self_empl_main_use_housing_furniture",                        "float64",  None,   None),
    "bus_main_use__6":          ("self_empl_main_use_transportation",                           "float64",  None,   None),
    "bus_main_use__7":          ("self_empl_main_use_entertainment",                            "float64",  None,   None),
    # "bus_main_use_others":    ("self_empl_main_use_other",                                    "object",   None,   None),
    "bus_input":                ("self_empl_input_costs_last_30_days",                          "float64",  None,   None),
    "bus_labor":                ("self_empl_labor_costs_last_30_days",                          "float64",  None,   None), 
    "bus_capital":              ("self_empl_capital_costs_last_30_days",                        "float64",  None,   None), #Machinery Maintenance, Rent 
    "bus_reg":                  ("self_empl_registered",                                        "float64", "dummy", None),
    "bus_loc":                  ("self_empl_location",                                          "object",   None,   mappings.self_employment_location),
    "bus_employe":              ("self_empl_number_of_employees",                               "float64",  None,   None),
    "years_exp_agri":           ("self_empl_years_experience_in_years",                         "float64",  None,   None),
    "tourism_motivate__1":      ("self_empl_motiv_previous_experience",                         "float64", "dummy", None),
    "tourism_motivate__2":      ("self_empl_motiv_others_are_successful",                       "float64", "dummy", None),
    "tourism_motivate__3":      ("self_empl_motiv_believe_in_success",                          "float64", "dummy", None),
    "tourism_motivate__4":      ("self_empl_motiv_unemployment",                                "float64", "dummy", None),
    "tourism_motivate__5":      ("self_empl_motiv_insuff_income_from_farming",                  "float64", "dummy", None),
    "tourism_motivate__6":      ("self_empl_motiv_insuff_income_from_agr_job",                  "float64", "dummy", None),
    "tourism_motivate__7":      ("self_empl_motiv_insuff_income_from_non_agr_job",              "float64", "dummy", None),
    "tourism_motivate__8":      ("self_empl_motiv_inherited_business",                          "float64", "dummy", None),
    # "tourism_motivate_oth":   ("self_empl_motivation_other",                                  "object",   None,   None),
    "business_obstacle__1":     ("self_empl_obstacle_taxes_regulation",                         "float64", "dummy", None), 
    "business_obstacle__2":     ("self_empl_obstacle_financing",                                "float64", "dummy", None), 
    "business_obstacle__3":     ("self_empl_obstacle_political_instability",                    "float64", "dummy", None), 
    "business_obstacle__4":     ("self_empl_obstacle_inflation",                                "float64", "dummy", None), 
    "business_obstacle__5":     ("self_empl_obstacle_infrastructure",                           "float64", "dummy", None), 
    "business_obstacle__6":     ("self_empl_obstacle_organised_crime",                          "float64", "dummy", None), 
    "business_obstacle__7":     ("self_empl_obstacle_street_crime",                             "float64", "dummy", None), 
    "business_obstacle__8":     ("self_empl_obstacle_corruption",                               "float64", "dummy", None), 
    "business_obstacle__9":     ("self_empl_obstacle_no_purchasing_power",                      "float64", "dummy", None), 
    "business_obstacle__10":    ("self_empl_obstacle_racial_discrimination",                    "float64", "dummy", None), 
    "business_obstacle__11":    ("self_empl_obstacle_no_land_access",                           "float64", "dummy", None), 
    # "business_obs_other":     ("self_empl_obstacle_other",                                    "object",   None,   None),
    "business_financing__1":    ("self_empl_three_main_finance_constr_high_int_rate",           "float64", "dummy", None), 
    "business_financing__2":    ("self_empl_three_main_finance_constr_no_long_term_loan",       "float64", "dummy", None), 
    "business_financing__3":    ("self_empl_three_main_finance_constr_no_collateral",           "float64", "dummy", None),
    "business_financing__4":    ("self_empl_three_main_finance_constr_paperwork",               "float64", "dummy", None),
    "business_financing__5":    ("self_empl_three_main_finance_constr_credit_info",             "float64", "dummy", None),
    "business_financing__6":    ("self_empl_three_main_finance_constr_connections",             "float64", "dummy", None),
    "business_financing__7":    ("self_empl_three_main_finance_constr_bank_lacks_money",        "float64", "dummy", None),
    "business_financing__8":    ("self_empl_three_main_finance_constr_no_export_finance",       "float64", "dummy", None),
    "business_financing__9":    ("self_empl_three_main_finance_constr_no_equity",               "float64", "dummy", None),
    "business_financing__10":   ("self_empl_three_main_finance_constr_no_leasing",              "float64", "dummy", None),
    "business_financing__11":   ("self_empl_three_main_finance_constr_no_foreign_banks",        "float64", "dummy", None),
    "business_financing__12":   ("self_empl_three_main_finance_constr_corruption",              "float64", "dummy", None),
    # "business_financing_oth": ("self_empl_three_main_finance_constr_other",                   "object",   None,   None),
    "business_finance__1":     ("self_empl_loan_source_retained_earnings",                      "float64", "dummy", None),
    "business_finance__2":     ("self_empl_loan_source_local_banks",                            "float64", "dummy", None),
    "business_finance__3":     ("self_empl_loan_source_family_friends",                         "float64", "dummy", None),
    "business_finance__4":     ("self_empl_loan_source_supplier_credit",                        "float64", "dummy", None),
    "business_finance__5":     ("self_empl_loan_source_sale_of_stock",                          "float64", "dummy", None),
    "business_finance__6":     ("self_empl_loan_source_foreign_banks",                          "float64", "dummy", None),
    "business_finance__7":     ("self_empl_loan_source_develop_finance",                        "float64", "dummy", None),
    "business_finance__8":     ("self_empl_loan_source_moneylenders",                           "float64", "dummy", None),
    # "business_finance_oth":  ("self_empl_loan_source_other",                                  "object",   None,   None),
    "support_local_gov":       ("self_empl_supported_by_governance",                            "float64", "dummy", None), #there is more info on what kind of support!
    
    #WAGE EMPLOYMENT
    # "lbr3_2":                 ("wage_empl_company_name",                                                      "object",  None,   None),
    "lbr3_3":                   ("wage_empl_location",                                                          "object",  None,   mappings.wage_employment_location),
    "lbr3_4":                   ("wage_empl_type",                                                              "object",  None,   None), #permanent or seasonal?

    #permanent
    "lbr3_5":                   ("wage_empl_permanent_wage_per_month",                                          "float64", None,   None),
    "lbr3_5_1__1":              ("wage_empl_permanent_main_use_invest_in_own_business",                         "float64", None,   None),
    "lbr3_5_1__2":              ("wage_empl_permanent_main_use_food",                                           "float64", None,   None),
    "lbr3_5_1__3":              ("wage_empl_permanent_main_use_education",                                      "float64", None,   None),
    "lbr3_5_1__4":              ("wage_empl_permanent_main_use_health",                                         "float64", None,   None),
    "lbr3_5_1__5":              ("wage_empl_permanent_main_use_housing_furniture",                              "float64", None,   None),
    "lbr3_5_1__6":              ("wage_empl_permanent_main_use_transportation",                                 "float64", None,   None),
    "lbr3_5_1__7":              ("wage_empl_permanent_main_use_entertainment",                                  "float64", None,   None),
    # "lbr3_5_1_oth":           ("wage_empl_permanent_main_use_other",                                          "object",  None,   None),
    "lbr3_6":                   ("wage_empl_permanent_days_per_week",                                           "float64", None,   None),
    "lbr3_7":                   ("wage_empl_permanent_hours_per_day",                                           "float64", None,   None),

    #seasonal/casual
    "lbr3_8":                   ("wage_empl_seasonal_casual_payment_frequency",                                 "object",  None,   None),
    "lbr3_9":                   ("wage_empl_seasonal_casual_wage_per_interval",                                 "float64", None,   None),
    "lbr3_9_1__1":              ("wage_empl_seasonal_casual_main_use_invest_in_own_business",                   "float64", None,   None),
    "lbr3_9_1__2":              ("wage_empl_seasonal_casual_main_use_food",                                     "float64", None,   None),
    "lbr3_9_1__3":              ("wage_empl_seasonal_casual_main_use_education",                                "float64", None,   None),
    "lbr3_9_1__4":              ("wage_empl_seasonal_casual_main_use_health",                                   "float64", None,   None),
    "lbr3_9_1__5":              ("wage_empl_seasonal_casual_main_use_housing_furniture",                        "float64", None,   None),
    "lbr3_9_1__6":              ("wage_empl_seasonal_casual_main_use_transportation",                           "float64", None,   None),
    "lbr3_9_1__7":              ("wage_empl_seasonal_casual_main_use_entertainment",                            "float64", None,   None),
    # "lbr3_9_1_oth":           ("wage_empl_seasonal_casual_main_use_other",                                    "object",  None,   None),
    "lbr3_10":                  ("wage_empl_seasonal_casual_rainy_season_duration_in_months_last_12_months",    "float64", None,   None), 
    "lbr3_11":                  ("wage_empl_seasonal_casual_dry_season_duration_in_months_last_12_months",      "float64", None,   None), 
    "lbr3_12":                  ("wage_empl_seasonal_casual_duration_days_per_week",                            "float64", None,   None),
    "lbr3_13":                  ("wage_empl_seasonal_casual_duration_hours_per_day",                            "float64", None,   None),

    #GENERAL
    "Ibr3_14__1":               ("benefits_housing",                                                            "float64", "dummy", None),
    "Ibr3_14__2":               ("benefits_meals",                                                              "float64", "dummy", None),
    "Ibr3_14__3":               ("benefits_transportation",                                                     "float64", "dummy", None),
    "Ibr3_15":                  ("uncompensated_work",                                                          "float64", "dummy", None),
    "Ibr3_16":                  ("work_accident",                                                               "float64", "dummy", None),
    "Ibr3_17":                  ("paternity_maternity_leave",                                                   "float64", "dummy", None),
    "Ibr3_18":                  ("health_insurance",                                                            "float64", "dummy", None),
    "Ibr3_19":                  ("unprotected_dangerous_products",                                              "float64", "dummy", None),
    "leave":                    ("paid_annual_leave",                                                           "float64", "dummy", None),
    "sick_leave":               ("paid_sick_leave",                                                             "float64", "dummy", None),
    "lbr10":                    ("contract_status",                                                             "object",   None,   mappings.contract_status),
    # "lbr10_1":                ("contract_status_other",                                                       "object",   None,   None),
    "job_search":               ("job_search",                                                                  "object",   None,   mappings.job_search),
    # "job_search_oth":         ("job_search_other",                                                            "object",   None,   None),
    "lbr09":                    ("training_received",                                                           "float64", "dummy", None),
    "emp_years":                ("duration_in_years",                                                           "float64",  None,   None),
    "lbr11":                    ("job_satisfaction",                                                            "object",   None,   mappings.job_satisfaction), 
}

ON_FARM_EMPLOYMENT_2023 = {
    "interview__key":       ("interview_key",                                                         "object",   None,   None),
    "r_members__id":        ("members_id",                                                            "object",   None,   None),
    "lbr13":                ("farm_empl_last_12_months",                                              "float64",  "dummy", None),

    #CROPS
    "Ibr13_1":              ("farm_empl_cash_crops_duration_rainy_season_in_months_last_12_months",   "float64",  None,   None),
    "Ibr13_2":              ("farm_empl_cash_crops_duration_dry_season_in_months_last_12_months",     "float64",  None,   None),
    "Ibr13_3":              ("farm_empl_cash_crops_days_per_week",                                    "float64",  None,   None),
    "Ibr13_4":              ("farm_empl_cash_crops_hours_per_day",                                    "float64",  None,   None),
    "Ibr13_5":              ("farm_empl_food_crops_duration_rainy_season_in_months_last_12_months",   "float64",  None,   None),
    "Ibr13_6":              ("farm_empl_food_crops_duration_dry_season_in_months_last_12_months",     "float64",  None,   None),
    "Ibr13_8":              ("farm_empl_food_crops_days_per_week",                                    "float64",  None,   None),
    "Ibr13_9":              ("farm_empl_food_crops_hours_per_day",                                    "float64",  None,   None),
    "years_exp_crp":        ("farm_empl_crops_years_experience_in_years",                             "float64",  None,   None),

    #LIVESTOCK
    "Ibr13_10":             ("farm_empl_livestock_duration_rainy_season_in_months_last_12_months",    "float64",  None,   None), 
    "Ibr13_11":             ("farm_empl_livestock_duration_dry_season_in_months_last_12_months",      "float64",  None,   None), 
    "Ibr13_12":             ("farm_empl_livestock_days_per_week",                                     "float64",  None,   None), 
    "Ibr13_13":             ("farm_empl_livestock_hours_per_day",                                     "float64",  None,   None), 
    "years_exp_liv":        ("farm_empl_livestock_years_experience_in_years",                         "float64",  None,   None),

    "onfarm_main_use__1":   ("farm_empl_main_use_invest_in_own_business",                             "float64",  None,   None),
    "onfarm_main_use__2":   ("farm_empl_main_use_food",                                               "float64",  None,   None),
    "onfarm_main_use__3":   ("farm_empl_main_use_education",                                          "float64",  None,   None),
    "onfarm_main_use__4":   ("farm_empl_main_use_health",                                             "float64",  None,   None),
    "onfarm_main_use__5":   ("farm_empl_main_use_housing_furniture",                                  "float64",  None,   None),
    "onfarm_main_use__6":   ("farm_empl_main_use_transportation",                                     "float64",  None,   None),
    "onfarm_main_use__7":   ("farm_empl_main_use_entertainment",                                      "float64",  None,   None),
}

MIGRATION_2023 = {
    "interview__key": ("interview_key",                         "object",   None,       None),
    "r_members__id":  ("members_id",                            "object",   None,       None),
    "migrant_ind":    ("migrant_last_12_months",                "float64",  "dummy",    None),
    "migrant_current":("current_migrant",                       "float64",  "dummy",    None),
    "migr_itt":       ("migration_intention_next_12_months",    "object",   None,       mappings.migration_intention),
    "remit_amt":      ("remittance_amount_sent_last_12_months", "float64",  None,       None),
}

ASPIRATIONS_2023 = {
    "interview__key":       ("interview_key",                          "object",    None,   None),
    "r_members__id":        ("members_id",                             "object",    None,   None),
    "as01":                 ("beans_allocated_to_empl_occupation",     "float64",   None,   None),
    "asp_occup":            ("aspired_occupation_5_years_ahead",       "object",    None,   mappings.aspired_occupation),
    "life_satisfaction":    ("life_satisfaction",                      "object",    None,   mappings.life_satisfaction),
    "aspire_cont_farm":     ("aspiration_continue_farming",            "object",    None,   mappings.aspiration_continue_farming), #No time horizon: Do you aspire to continue to farm or venture into other businesses or combine both?
    
    #AGRICULTURAL LOAN
    "agri_loan":            ("agriculture_loan_last_5_years",          "float64",  "dummy", None),
    "agri_loan_amt":        ("agriculture_loan_amount",                "float64",   None,   None),
    "agri_loan_lndr__1":    ("agriculture_loan_lender_bank",           "float64",  "dummy", None),
    "agri_loan_lndr__2":    ("agriculture_loan_lender_credit_union",   "float64",  "dummy", None),
    "agri_loan_lndr__3":    ("agriculture_loan_lender_private_lender", "float64",  "dummy", None),
    "agri_loan_lndr__4":    ("agriculture_loan_lender_government",     "float64",  "dummy", None),
    "agri_loan_lndr__5":    ("agriculture_loan_lender_ngos",           "float64",  "dummy", None),
    # "agri_loan_lndr_oth": ("agriculture_loan_lender_other",          "object",    None,   None),
}

CHILD_ASPIRATIONS_2023 = {
    "interview__key":     ("interview_key",                     "object",   None, None),
    "r_members__id":      ("members_id",                        "object",   None, None),
    "r_child__id":        ("child_id",                          "object",   None, None),
    # "asocp01":          ("child_aspiration_occupation",       None,       None, None), #open ended! What profession or occupation do you aspire for %rostertitle%?
    "youth_child_tofarm": ("child_aspiration_continue_farming", "object",   None, mappings.child_aspiration_continue_farming), #How likely would you encourage %rostertitle% engage in agriculture--farm or venture into farming (agribusiness or agri enterprise)?
}

TIME_ALLOCATION_2023 = { #In the last complete 24 hours, starting yesterday morning at 3 am, finishing 2:59 am of the current day, which activities did you carry out? 
    "interview__key":     ("interview_key",                         "object",   None, None),
    "r_members__id":      ("members_id",                            "object",   None, None),
    "f_time__id":         ("time_slot",                             "object",   None, None),
    "f_prim":             ("primary_activity",                      "object",   None, mappings.primary_activity),
}

DECISION_MAKING_2023 = {
    "interview__key":       ("interview_key",               "object",  None,    None),
    "r_members__id":        ("members_id",                  "object",  None,    None),
    "decision_code":        ("decision_type",               "object",  None,    mappings.decision_code),
    "decision_maker_1":     ("decision_maker_1",            "object",  None,    None), 
    "decision_maker_2":     ("decision_maker_2",            "object",  None,    None),
}

