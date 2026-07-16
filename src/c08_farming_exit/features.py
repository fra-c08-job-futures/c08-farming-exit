"""Relevant features."""

#HOUSEHOLD-LEVEL FEATURES
IDENTIFYING_INFO_2023 = {
    "ctry":           "country",
    "interview__key": "interview_key",
    #"hhid":           "hhid",
    "ea":             "enumeration_area",
    "dist":           "district",
    "region":         "region",
    "res_rel":        "respondant_relation_to_head",
}

LAND_OWNERSHIP_ACCESS_2023 = {
    "interview__key":  "interview_key",
    # "lnd_mes":         "land_measurement",
    # "lnd_mes_1":       "land_measurement_other",
    # "lnd01":           "land_size_cropland",
    # "lnd02":           "land_size_fallow",
    # "lnd03":           "land_size_agroforestry_forestry",
    # "lnd04":           "land_size_pasture",
    # "lnd08":           "land_size_residential",
    # "lnd09":           "land_size_lodge_camp",
    # "lnd06":           "land_size_other",
    "lnd_ten01":       "land_cropland_ownership_status",
    # "lnd_ten02":       "land_fallow_ownership_status",
    # "lnd_ten03":       "land_agroforestry_forestry_ownership_status",
    # "lnd_ten04":       "land_pasture_ownership_status",
    # "lnd_ten08":       "land_residential_ownership_status",
    # "lnd_ten09":       "land_lodge_camp_ownership_status",
    # "lnd_ten06":       "land_other_ownership_status",
    # "lnd_16":          "land_used_as_collateral",
    # "num_plots":       "land_number_of_plots",
}

PARCEL_INFORMATION_2023 = {
    "interview__key":    "interview_key",
    "num_plots":         "parcel_number_owned", # is it the same as in LAND_OWNERSHIP_ACCESS_2023?
}

CROP_PRODUCTION_2023 = {
    "interview__key":     "interview_key",
    "r_crop__id":         "crop_type",
    "crop_harvest":       "crop_harvested",
    # "crop_output":        "crop_output",
    # "crop_unit":          "crop_unit",
    # "crop_unit_1":        "crop_unit_other",
    # "crop_sales":         "crop_sale",
    # "crop_saleamt":       "crop_sale_amount",
    # "crop_slunits":       "crop_sale_unit",
    # "crop_slunits_1":     "crop_sale_unit_other",
    # "crop_price":         "crop_sale_price_per_unit",
    # "crop_buyer__1":      "crop_buyer_market",
    # "crop_buyer__2":      "crop_buyer_trader",
    # "crop_buyer__3":      "crop_buyer_cooperative",
    # "crop_buyer__4":      "crop_buyer_commercial_farm", 
    # "crop_buyer__5":      "crop_buyer_hospitality",
    # "crop_buyer__6":      "crop_buyer_government",
    # "crop_buyer_other":   "crop_buyer_other",
    # "crop_homecons":      "crop_home_consumption",
    # "crop_clunits":       "crop_home_consumption_unit",
    # "crop_cunits_1":      "crop_home_consumption_unit_other",
    "cp_stor":            "crop_storage",
    # "cpamt":              "crop_storage_amount",
    # "cpunits2":           "crop_storage_unit",
    # "cpunits2_other":     "crop_storage_unit_other",
    "cp07":               "crop_organic_fertilizer",
    "cp08":               "crop_inorganic_fertilizer",
    "cp09":               "crop_pesticides",
    "cp11":               "crop_tractor",
}

CROP_EXPENDITURE_2023 = {
    "interview__key":      "interview_key",
    "crp_ip1_exp":         "crop_exp_seeds_last_12_months",
    "crp_ip3_exp":         "crop_exp_fertilizer_last_12_months",
    "crp_ip5_exp":         "crop_exp_pesticide_last_12_months",
    "crp_ip6_exp":         "crop_exp_machinery_last_12_months",
    "crp_ip7_exp":         "crop_exp_hired_labor_last_12_months",
    "crp_ip8_exp":         "crop_exp_land_rental_last_12_months",
    "crp_ip9_exp":         "crop_exp_transport_last_12_months",
    "crp_ip10_exp":        "crop_exp_other_last_12_months",
}

MARKET_ACCESS_2023 = {
    "interview__key":        "interview_key",
    "markt_output_dist":     "market_output_distance_in_km",
    # "markt_input_dist":      "market_input_distance_in_km",
    # "markt_buyer":           "market_type",
    # "markt_buyer_oth":       "market_type_other",
    "crop_contract":         "crop_contract",
    # "contract_crop":         "crop_contract_crop_type",
    "input_access_subsidy":  "subsidy",
    # "subsidy_type__1":       "subsidy_type_seeds",
    # "subsidy_type__2":       "subsidy_type_fertilizer",
    # "subsidy_type__3":       "subsidy_type_agro_chemicals",
    # "subsidy_type__4":       "subsidy_type_interest_free_loan",
    # "subsidy_supplier__1":   "subsidy_supplier_government",
    # "subsidy_supplier__2":   "subsidy_supplier_ngos",
    # "subsidy_supplier__3":   "subsidy_supplier_company",
    # "subsidy_supplier_oth":  "subsidy_supplier_other",
}

LIVESTOCK_OWNERSHIP_2023 = {
    "interview__key":        "interview_key",
    # "r_livestock__id":       "livestock_type",
    "lv02":                  "livestock_owned",
    # "lv07":                  "livestock_number_sold",
    # "lv06":                  "livestock_number_lost_disease_theft",
    # "lv07":                  "livestock_number_lost_wildlife_attack",
    # "lv08":                  "livestock_price_head_sold",
}

LIFESTOCK_GRAZING_2023 = {
    "interview__key":           "interview_key",
    "grazing_dist":             "grazing_distance_in_min",
    # "grazing_days":             "grazing_time_in_min",
    "grazing_hour":             "grazing_time_hours_per_day",
    "grazing_ownership":        "grazing_land_ownership_status",
    # "grazing_sharing":          "grazing_land_number_hh_sharing",
    # "grazing_permit":           "grazing_land_permit",
    # "grazing_permit_price":     "grazing_land_permit_price",
    "grazing_years":            "grazing_land_use_duration_in_years",
    "grazing_challenges__1":    "grazing_land_challenges_1", # what is it?
    "grazing_challenges__2":    "grazing_land_challenges_2", # what is it?
    "grazing_challenges__3":    "grazing_land_challenges_3", # what is it?
    "grazing_challenges__4":    "grazing_land_challenges_4", # what is it?
    "grazing_challenges__5":    "grazing_land_challenges_5", # what is it?
    "grazing_challenges__6":    "grazing_land_challenges_6", # what is it?
    "grazing_challenges__7":    "grazing_land_challenges_7", # what is it?
    "grazing_challenges__8":    "grazing_land_challenges_8", # what is it?
    "grazing_challenges__9":    "grazing_land_challenges_9", # what is it?
    "grazing_challenges__10":   "grazing_land_challenges_10", # what is it?
    "grazing_challenges__11":   "grazing_land_challenges_11", # what is it?
    # "grazing_challenge_other":  "grazing_land_challenges_other",
}

LIFESTOCK_INCOME_2023 = {
    "interview__key":       "interview_key",
    "liv_pdtsal":           "livestock_products_sold_last_12_months",
    # "which_liv_pdts__1":    "livestock_products_sold_meat",
    # "which_liv_pdts__2":    "livestock_products_sold_milk",
    # "which_liv_pdts__3":    "livestock_products_sold_cheese",
    # "which_liv_pdts__4":    "livestock_products_sold_yogurt",
    # "which_liv_pdts__5":    "livestock_products_sold_wool",
    # "which_liv_pdts__6":    "livestock_products_sold_honey_wax",
    # "which_liv_pdts__7":    "livestock_products_sold_eggs",
    # "which_liv_pdts_oth":   "livestock_products_sold_other",
    "liv_buyer":            "livestock_products_buyer",
    # "liv_buyer_oth":        "livestock_products_buyer_other",
    "liv_buyer_where":      "livestock_products_market_type",
    "livmkt_dist":          "livestock_market_distance_in_km",
    "liv_pdt_inc":          "livestock_income_last_12_months",
    # "liv_contract":         "livestock_contract",
}

LIFESTOCK_EXPENDITURE_2023 = {
    "interview__key":     "interview_key",
    "vexp01_11":          "livestock_exp_feed_fodder",
    "lvexp02_12":         "livestock_exp_rent_gazing_land",
    "lvexp03_13":         "livestock_exp_veterinary_services",
    "lvexp04_14":         "livestock_exp_shelter",
    "lvexp05_15":         "livestock_exp_hired_labor",
    # "lvexp06_16":         "livestock_exp_other",
}

HOUSING_CONDITIONS_2023 = {
    "interview__key":    "interview_key",
    "h02":               "house_room_number",
    "h03":               "house_roof_material",
    # "h03_oth":           "house_roof_material_other",
    # "h04":               "house_wall_material",
    # "h04_oth":           "house_wall_material_other",
    # "h05":               "house_floor_material",
    # "h05_oth":           "house_floor_material_other",
    "h06":               "house_water_source",
    # "h06_oth":           "house_water_source_other",
    "h07":               "house_toilet_type",
    # "h07_oth":           "house_toilet_type_other",
}

ENERGY_ACCESS_2023 = {
    "interview__key":    "interview_key",
    "h09":               "house_energy_source",
    # "h09_oth":           "house_energy_source_other",
    # "h10":               "house_energy_source_for_cooking",
    # "h10_1":             "house_energy_source_for_cooking_other",
    # "h11":               "house_energy_source_for_lighting",
    # "h11_1":             "house_energy_source_for_lighting_other",
}

ASSETS_OWNED_2023 = {
    "interview__key":    "interview_key",
    "r_asset_own__id":   "asset_type",
    # "ha0_1":             "asset_number_owned",
}

INTERNET_ACCESS_2023 = {
    "interview__key":    "interview_key",
    "access_internet":   "internet_access",
    # "internet_home":     "internet_access_at_home",
    # "distance_internet": "internet_access_distance_in_meters",
    #ToDo: What Types of Online Activities Do you Engage in when using the Internet? Available
}

SHOCKS_AND_COPING_2023 = {
    "interview__key":   "interview_key",
    # "r_shocks__id":     "shock_id",
    "r_shocks":         "shock_type_affected_last_12_months",
    # "sh_1":             "shock_frequency_last_12_months",
    # "sh_2":             "shock_severity_last_12_months",

    #COPING
    # "sh_3__1":           "shock_coping_strategy_relatives",
    # "sh_3__2":           "shock_coping_strategy_government",
    # "sh_3__3":           "shock_coping_strategy_food_reduction", 
    # "sh_3__4":           "shock_coping_strategy_changed_cropping_practices",
    # "sh_3__5":           "shock_coping_strategy_off_farm_empl", #ToDo: Check if its true
    # "sh_3__6":           "shock_coping_strategy_hh_member_migration",
    # "sh_3__7":           "shock_coping_strategy_savings",
    # "sh_3__8":           "shock_coping_strategy_insurance",
    # "sh_3__9":           "shock_coping_strategy_credit",
    # "sh_3__10":          "shock_coping_strategy_sold_hh_assets",
    # "sh_3__11":          "shock_coping_strategy_sold_livestock",
    # "sh_3__12":          "shock_coping_strategy_migration",
    # "sh_3__13":          "shock_coping_strategy_police_report",
    # "sh_3__14":          "shock_coping_strategy_nothing",
    # "sh_3_oth":          "shock_coping_strategy_other",
    
    # "sh_4":              "shock_future_likelihood_1", #what is it?
    # "sh_5":              "shock_future_likelihood_2", #what is it?
    # "sh_6":              "shock_future_likelihood_3", #what is it?
}

SOCIAL_NETWORK_2023 = {
    "interview__key":   "interview_key",
    "as19":             "mobile_money_access",
    # "as18__1":          "membership_farmers_group",
    # "as18__2":          "membership_agricultural_cooperative",
}

SOCIAL_EMBEDDEDNESS_2023 = {
    # ONYL RESPONDAND ASEKD:CAN BE USED AS A PROXY FOR THE OPTIMISM OF THE HH
    "interview__key":   "interview_key",
    "as_loc01_in":      "my_life_course_depends_on_me",
    "as_loc02_in":      "success_is_hard_work",
    "as_loc03_in":      "ability_is_more_important_than_effort",
    "as_loc04_in":      "my_plans_will_work",
    "as_loc06_in":      "I_can_shape_my_future_positively",
    "as_loc12_in":      "I_am_optimistic_about_my_future",
    "as_loc13_in":      "I_am_optimistic_about_my_familys_future",
    "exp_ev1_01":       "worry_about_job_loss_or_economic_livelihood"
}

FOOD_INSECURITY_2023 = {
    "interview__key":       "interview_key",
    "food_sufficent":       "sufficent_food_number_of_month"
    #ToDo: During the Last 12 Months, Was There a Time When, Because of Lack of Money or Ot... available!
}

OTHER_INCOME_SOURCES_2023 = {
    "interview__key":       "interview_key",
    # "r_otherincome__id":    "other_income_source",
    "inc_oth_amt":          "other_income_amount",
    # "nt_oth_income":        "other_income_frequency"
}

ROAD_CONNECTIVITY_2023 = {
    "interview__key":       "interview_key",
    "road_1":               "road_type",
    "road_2":               "road_condition",
    "road_6":               "road_distance_in_minutes"
}



#INDIVIDUAL-LEVEL FEATURES
HH_MEMBERS_2023 = {
    "interview__key":   "interview_key",
    "r_members__id":    "members_id", 
    "ha03":             "gender",
    "ha_rel":           "relation_to_head",
    "age":              "age",
    # "ha07":             "ethnic_group",
    # "ha07_other":       "ethnic_group_new",
    # "religio":          "religion",
    # "religio_1":        "religion_other",
    "educ1":            "education_level",
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