import re

def find_word_location(word, paragraph):
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)))  # Create a regular expression pattern for the word
    match = re.search(pattern, paragraph)  # Search for the word in the paragraph
    if match:
        start = match.start()  # Start index of the matched word
        end = match.end()  # End index of the matched word
        return start, end
    else:
        return None

def main():
    text = "Hepatocyte nuclear factor - 6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion."
    start, end = find_word_location('insulin', text)
    print(start,end)
    entity_list = {}
    result =   [('Hepatocyte nuclear factor - 6', 'GeneOrGeneProduct'), ('type II diabetes', 'DiseaseOrPhenotypicFeature'), ('insulin', 'GeneOrGeneProduct')]

    for item in result:
        # print(item)
        entity = ()
        start, end = find_word_location(item[0], text)
        entity = entity + (start,end,item[1],item[0])
        # print(entity)
        # start, end = find_word_location(item[0], para)
    #  entity_list= {'3175':[(0,29,'GeneOrGeneProduct','Hepatocyte nuclear factor - 6')],
    #               'D003924':[(77,93,'DiseaseOrPhenotypicFeature','type II diabetes')],
    #               '3630':[(143,150,'GeneOrGeneProduct','insulin')]}
    # for item in result:
    #     start, end = find_word_location(item[0], para)
    #     # print(item[0])
    #     data_1 = {}
    #     data_1["code"] = (start,end,item[0],item[1])
    #     data = data + (data_1)
        # print(item[1])

if __name__ == "__main__":
    main()
