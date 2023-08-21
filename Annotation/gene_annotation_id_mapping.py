from Bio import Entrez

# Set your email address (required by NCBI)
Entrez.email = "vhnowflearning@gmail.com"

# Specify the database to query (gene)
db = "gene"

# Specify the search term or keyword
keyword = "ALD"

# Construct the query with the keyword and desired search fields

# Homo sapiens
query = f"({keyword}[Gene Name/alias] OR {keyword}[Gene Symbol/alias] OR {keyword}[Gene Abbreviation]) AND human[Organism]"

# Use Entrez.esearch to search for the keyword in the gene database
handle = Entrez.esearch(db=db, term=query)

# Read the search results
response = Entrez.read(handle)

# Close the handle
handle.close()

# Retrieve the list of gene IDs from the search results
gene_ids = response["IdList"]

# Retrieve the first gene in the gene family
if len(gene_ids) > 0:
    first_gene_id = gene_ids[0]
    # print(response["Gene Description"])
    print("First Gene ID:", first_gene_id)
else:
    print("No gene found for the search term.")



