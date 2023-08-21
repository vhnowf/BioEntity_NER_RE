from Bio import Entrez

def annotate_chemical_by_keyword(keyword):
    Entrez.email = 'vhnowflearning@gmail.com'  # Provide your email address

    # Perform a search query for the keyword in the MESH database
    search_term = f'{keyword}[All Fields]'
    handle = Entrez.esearch(db='mesh', term=search_term)
    record = Entrez.read(handle)

    # Retrieve the unique MESH ID for the first matching chemical
    mesh_id_list = record['IdList']
    if len(mesh_id_list) > 0:
        # Fetch the detailed information for the first MESH ID
        mesh_id = mesh_id_list[0]
        # Remove any leading characters from the MESH ID
        mesh_id = mesh_id.lstrip('0').lstrip('D')
        return mesh_id

    return None

# Example usage
keyword = 'Betaine'
mesh_id = annotate_chemical_by_keyword(keyword)
if mesh_id is not None:
    print('Keyword:', keyword)
    print('MESH ID:', mesh_id)
else:
    print('No MESH ID found for the keyword:', keyword)


# import urllib.request
# import xml.etree.ElementTree as ET

# def annotate_chemical_by_keyword(keyword):
#     # Construct the URL to retrieve the XML Descriptor records for the given keyword
#     url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=mesh&term={keyword}&retmax=1'

#     with urllib.request.urlopen(url) as response:
#         xml_data = response.read()

#     root = ET.fromstring(xml_data)

#     # Initialize the descriptor_name variable with a default value
#     descriptor_name = None

#     # Extract the MESH ID and other relevant information from the XML record
#     for child in root.iter('Id'):
#         mesh_id = child.text

#     for child in root.iter('DescriptorName'):
#         descriptor_name = child.text

#     # Return the extracted MESH ID and descriptor name
#     return mesh_id, descriptor_name

# # Example usage
# keyword = 'Chlorpromazine'
# mesh_id, descriptor_name = annotate_chemical_by_keyword(keyword)
# if mesh_id:
#     print('Keyword:', keyword)
#     print('MESH ID:', mesh_id)
#     if descriptor_name:
#         print('Descriptor Name:', descriptor_name)
#     else:
#         print('No descriptor name found for the keyword:', keyword)
# else:
#     print('No annotation found for the keyword:', keyword)