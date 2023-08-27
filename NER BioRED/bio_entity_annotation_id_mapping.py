import requests
import sys
import argparse
import json

def get_pubtator_annotations(pubmed_id):
    base_url = 'https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/biocjson?'
    
    params = {
        'pmids': pubmed_id,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data_json = json.loads(response.text)
        result = []
        for data in data_json['passages']:
            result.append(data['annotations'])
        return result
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description='Tool to mapping annotation with ID')
    parser.add_argument('--pmid',type=str,required=True,help='Pmid of article that you want to map')
    
    args = parser.parse_args()
   
    if args.pmid:
        annotations =  get_pubtator_annotations(args.pmid)
        if annotations:
            print(annotations)
        else:
            print("Failed to retrieve annotations.")

if __name__ == '__main__':
    main()  
        

