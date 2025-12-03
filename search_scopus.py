import requests
import json
from config import API_KEY

##API_KEY = "my key"

### Configuration
URL_DO_ENDPOINT = "https://api.elsevier.com/content/search/scopus"

def get_interactive_query():
    print("--- 🤖 Interactive Scopus Search Setup ---")
    
    print("\nWhich main field do you want to search in?")
    print("  1: Title only (TITLE)")
    print("  2: Title, Abstract, and Keywords (TITLE-ABS-KEY)")
    
    field_choice = input("Choice (default: 1): ").strip()
    search_field = "TITLE-ABS-KEY" if field_choice == '2' else "TITLE"
    print(f"-> Field selected: {search_field}")

    default_subjects = "chicken OR broiler OR poultry"
    subject_terms = input(f"\nEnter the SUBJECT terms (separated by OR)\n[Default: {default_subjects}]: ")
    if not subject_terms:
        subject_terms = default_subjects

    default_action = "weight W/5 prediction"
    action_terms = input(f"\nEnter the ACTION terms (e.g., weight, prediction, etc.)\n[Default: {default_action}]: ")
    if not action_terms:
        action_terms = default_action

    keywords_query = f"{search_field}( ({subject_terms}) AND ({action_terms}) )"
    print(f"-> Keywords Query: {keywords_query}")

    start_year = 0
    default_year = 2016
    while True:
        try:
            year_input = input(f"\nSearch articles published FROM which year?\n[Default: {default_year}]: ")
            
            if not year_input:
                start_year = default_year
                print(f"-> Default year selected: {start_year}")
                break
                
            start_year = int(year_input)
            
            if 1900 < start_year < 2050:
                break
            else:
                print("Please enter a valid year (e.g., 2016).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    date_filter_query = f"AND ( PUBYEAR > {start_year - 1} )"
    print(f"-> Date Filter: {date_filter_query}")
    
    print("------------------------------------------------------")
    
    return keywords_query, date_filter_query

# Removed result_count from the function return
keywords, date_filter = get_interactive_query()

### Exclude list
excluded_words = [
    "egg"
]

### String of excluded items
word_exclusion_str = " ".join([f'AND NOT TITLE-ABS-KEY({word})' for word in excluded_words])
exclusion_filter = word_exclusion_str


### All togheter
final_query = f"{keywords} {date_filter} {exclusion_filter}"


### Params e Headers
# Defined count here statically
result_count = 25 

params = {
    "query": final_query,
    "count": result_count 
}

headers = {
    "X-ELS-APIKey": API_KEY
}

### Requisition

print(f"\n🔎 Searching Scopus API...")
print("...loading...")

try:
    response = requests.get(URL_DO_ENDPOINT, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        search_results = data.get('search-results', {})
        total_found = search_results.get('opensearch:totalResults', '0')
        
        print(f"\n--- Total found: {total_found} ---")
        
        if int(total_found) == 0:
            print("\nNo articles found with these filters.")
        
        for entry in search_results.get('entry', []):
            title = entry.get('dc:title')
            publication = entry.get('prism:publicationName')
            date = entry.get('prism:coverDate')
            print(f"\n- Title: {title}")
            print(f"  Publication: {publication} ({date})")
            
    else:
        print(f"\nRequest error: {response.status_code}")
        print("The API returned:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Connection error: {e}")
