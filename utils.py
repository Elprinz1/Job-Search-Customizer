import os
from jobspy import scrape_jobs

def get_jobs(site_name, search_term, location, results_wanted, hours_old, country_indeed):
        return scrape_jobs(
            site_name=site_name,
            search_term=search_term,
            location=location,
            results_wanted=results_wanted,
            hours_old=hours_old,
            country_indeed=country_indeed
        )