import requests
import json
from config import API_KEY

### Config
##API_KEY = "PASTE KEY HERE"
URL_DO_ENDPOINT = "https://api.elsevier.com/content/search/scopus"

def get_interactive_query():
    """
    Coleta os parâmetros de busca do usuário de forma interativa
    e retorna as strings de query formatadas e o contador.
    """
    print("--- 🤖 Interactive Scopus Search Setup ---")
    
    # --- 1. Campo de Busca ---
    print("\nWhich main field do you want to search in?")
    print("  1: Title only (TITLE)")
    print("  2: Title, Abstract, and Keywords (TITLE-ABS-KEY)")
    
    field_choice = input("Choice (default: 1): ").strip()
    search_field = "TITLE-ABS-KEY" if field_choice == '2' else "TITLE"
    print(f"-> Field selected: {search_field}")

    # --- 2. Termos do Assunto ---
    default_subjects = "chicken OR broiler OR poultry"
    subject_terms = input(f"\nEnter the SUBJECT terms (separated by OR)\n[Default: {default_subjects}]: ")
    if not subject_terms:
        subject_terms = default_subjects

    # --- 3. Termos da Ação/Conceito ---
    default_action = "weight W/5 prediction"
    action_terms = input(f"\nEnter the ACTION terms (e.g., weight, prediction, etc.)\n[Default: {default_action}]: ")
    if not action_terms:
        action_terms = default_action

    # Monta a query de keywords
    keywords_query = f"{search_field}( ({subject_terms}) AND ({action_terms}) )"
    print(f"-> Keywords Query: {keywords_query}")

    # --- 4. Filtro de Data ---
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
    
    # --- 5. Contagem de Resultados (user_prompt 5) ---
    result_count = 0
    default_count = 25
    while True:
        try:
            count_input = input(f"\nHow many results per page do you want?\n[Default: {default_count}]: ")
            
            if not count_input:
                result_count = default_count
                print(f"-> Default count selected: {result_count}")
                break
                
            result_count = int(count_input)
            
            if 0 < result_count <= 200:
                break
            else:
                print("Please enter a valid number (e.g., 25, 50, 100).")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("------------------------------------------------------")
    
    return keywords_query, date_filter_query, result_count

keywords, date_filter, result_count = get_interactive_query()

### Exclude list
excluded_titles = [
    "Weight prediction method for individual live chickens based on single-view point cloud information",
    "Revealing in vivo broiler chicken growth state: Integrating CT imaging and deep learning for non-invasive reproductive phenotypic measurement",
    "Online chicken carcass volume estimation using depth imaging and 3D reconstruction",
    "In Vivo Prediction of Breast Muscle Weight in Broiler Chickens Using X-ray Images Based on Deep Learning and Machine Learning",
    "Estimating Ross 308 Broiler Chicken Weight Through Integration of Random Forest Model and Metaheuristic Algorithms",
    "Predicting body weight in Ross 308 broiler chickens using a data mining algorithm approach",
    "Automated precision weighing: Leveraging 2D video feature analysis and machine learning for live body weight estimation of broiler chickens",
    "Weight prediction of broiler chickens using 3D computer vision",
    "Development of transfer function for weight prediction of live broiler chicken using machine vision",
    "A method for weighing broiler chickens using improved amplitude-limiting filtering algorithm and BP neural networks",
    "In vivo prediction of abdominal fat and breast muscle in broiler chicken using live body measurements based on machine learning",
    "Several models combined with ultrasound techniques to predict breast muscle weight in broilers.",
    "An Improved Method for Broiler Weight Estimation Integrating Multi-Feature with Gradient Boosting Decision Tree",
    "Non-Invasive Live Chicken Weight Estimation Using Geometric Features and Random Forest Regression"
]

excluded_words = [
    "egg"
]



### String of excluded itens
title_exclusion_str = " ".join([f'AND NOT TITLE("{title}")' for title in excluded_titles])
word_exclusion_str = " ".join([f'AND NOT TITLE-ABS-KEY({word})' for word in excluded_words])


### combined excludings
exclusion_filter = f"{title_exclusion_str} {word_exclusion_str}"


### All togheter
final_query = f"{keywords} {date_filter} {exclusion_filter}"


### Params e Headers

params = {
    "query": final_query,
    "count": result_count 
}

headers = {
    "X-ELS-APIKey": API_KEY
}

### Req

print(f"\n🔎 Searching Scopus API...")
##print(f"Query: {final_query}")
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