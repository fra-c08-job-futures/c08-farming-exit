* =============================================================================
* clean_data.do
* Loads Stata's built-in auto dataset, performs basic cleaning, and saves
* a cleaned copy to data/auto_clean.dta for use in the EDA notebook.
* =============================================================================

* ── 0. Working directory ─────────────────────────────────────────────────────
* Stata sets the working directory to the folder containing this do-file
* when you run it with the VSCode extension (Run button / Ctrl+Shift+D).
* If that is not the case, uncomment and adjust the line below:
* cd "C:\Users\localuser\my_projects\demo_app"

* ── 1. Load raw data ──────────────────────────────────────────────────────────
sysuse auto, clear          // ships with every Stata installation

* ── 2. Inspect ───────────────────────────────────────────────────────────────
describe
summarize
list in 1/5                 // peek at the first five rows

* ── 3. Clean ─────────────────────────────────────────────────────────────────

* Drop exact duplicates (none expected here, but good practice on real data)
duplicates drop

* Rename for clarity
rename rep78 repair_record

* Drop observations with missing repair record (5 obs in the raw data)
drop if missing(repair_record)

* Improve the foreign label so it reads clearly in charts
label define origin 0 "Domestic" 1 "Foreign", replace
label values foreign origin

* Derive a cost-efficiency proxy: price per mile-per-gallon
generate price_per_mpg = price / mpg
label variable price_per_mpg "Price / MPG (cost-efficiency proxy)"

* ── 4. Final check ───────────────────────────────────────────────────────────
summarize
tabulate foreign

* ── 5. Save ──────────────────────────────────────────────────────────────────
capture mkdir "data"                       // create folder if absent
save "data/auto_clean.dta", replace

display as result _n "Done — cleaned data saved to data/auto_clean.dta"
