import csv
import re
def read_csv_file(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Skip lines starting with "#"
        for row in reader:
            if not row[0].startswith('#'):
                data.append(row)

    return data

# Example usage
filename = '/media/data/namvh/dataset/MEDIC/CTD_diseases.csv'

# Read the CSV file
csv_data = read_csv_file(filename)

def check_string_presence(string, target_string):
    # Split the strings into words
    string_words = re.split(r'[ ,!?|]', string)
    target_words = re.split(r'[ ,!?|]', target_string)
    
    # Convert the lists of words to sets
    string_word_set = set(string_words)
    target_word_set = set(target_words)

    # Check if the target_word_set is a subset of string_word_set
    if target_word_set.issubset(string_word_set):
        return True
    else:
        return False
    
def search_list(lst, search_value):
    results = []

    # Iterate over each row in the list
    for row in lst:
        # for data in row:
        # Check if the search value is present in the row
        if search_value.lower() == row[0].lower():
            results.append(row[1])
        elif search_value.lower() == row[7].lower():
            results.append(row[1])
    if len(results) == 0:
        for row in lst:
            if check_string_presence(row[7].lower(),search_value.lower()):
                results.append(row[1])
    return results

search_value = 'nodular goitre'

results = search_list(csv_data, search_value)

# Print the results
if results:
    print(f"Found the value ID of '{search_value}': " + results[0].split(":")[1])
else:
    print(f"The value '{search_value}' was not found in the list.")


# import requests

# def get_ctd_id_by_disease_name(disease_name):
#     base_url = 'https://ctdbase.org'
#     endpoint = '/browse/term/{}.json'.format(disease_name)

#     # Send a GET request to the CTD website
#     response = requests.get(base_url + endpoint)

#     # Parse the JSON response
#     data = response.json()

#     # Extract the CTD ID if the disease is found
#     if 'terms' in data and data['terms']:
#         ctd_id = data['terms'][0]['id']
#         return ctd_id

#     # Return None if the disease cannot be found
#     return None

# # Example usage
# disease_name = "Breast cancer"

# # Find CTD ID
# ctd_id = get_ctd_id_by_disease_name(disease_name)
# if ctd_id:
#     print(f"The CTD ID for '{disease_name}' is: {ctd_id}")
# else:
#     print(f"No CTD ID found for '{disease_name}'")

