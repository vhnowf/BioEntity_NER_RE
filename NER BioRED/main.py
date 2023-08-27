import torch
from ultil_ner import get_labels
from transformers import  AutoConfig, AutoTokenizer, AutoModelForTokenClassification
from function import predict_example
from typing import Dict
import os
import sys
sys.path.append('/media/data/namvh/BIO-modules')
from Annotation.bio_entity_annotation_id_mapping import get_pubtator_annotations
import re
from GeoBERT.NER_task import *

def find_word_location(text, paragraph, entity_list):
    start_idx = 0
    end_idx = 0
    pattern = r'\b{}\b(?![\Ww-])'.format(re.escape(text))
    matches = [(match.start(), match.end()) for match in re.finditer(pattern, paragraph, re.IGNORECASE)]

    if not entity_list:
        start_idx = matches[0][0]
        end_idx = matches[0][1]
    else:
        index = 0 
        for key, ent in entity_list.items():
            for value in ent:  
                if value[3] == text:
                    index = index + 1
        start_idx = matches[index][0]
        end_idx =  matches[index][1]
    return start_idx, end_idx
    
"""
Using for predict
"""
def main():
    
    file_path = "/media/data/namvh/install/pubrunner/workspace/PubMEDArticlesXMLs/test/PUBMED_UNCONVERTED/10491763.xml"
    text = preprocess(file_path)
    pmid = os.path.splitext(os.path.basename(file_path))[0]
    annotations = get_pubtator_annotations(pmid)
       
    # Load model
    parent_dir = os.path.dirname(os.getcwd())
    model_path= os.path.join(parent_dir, 'NER BioRED', 'model', 'Biobert') # Biobert đang tốt hơn pubmed bert
    labels = get_labels()
    label_map: Dict[int, str] = {i: label for i, label in enumerate(labels)}
    num_labels = len(labels)
    config = AutoConfig.from_pretrained( model_path, num_labels=num_labels, 
    id2label=label_map, label2id={label: i for i, label in enumerate(labels)})
    model = AutoModelForTokenClassification.from_pretrained(model_path, config=config)
    device= torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir=None)

    # add data
    # text = "Hepatocyte nuclear factor-6: associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion. The transcription factor hepatocyte nuclear factor (HNF)-6 is an upstream regulator of several genes involved in the pathogenesis of maturity-onset diabetes of the young. We therefore tested the hypothesis that variability in the HNF-6 gene is associated with subsets of Type II (non-insulin-dependent) diabetes mellitus and estimates of insulin secretion in glucose tolerant subjects.   We cloned the coding region as well as the intron-exon boundaries of the HNF-6 gene. We then examined them on genomic DNA in six MODY probands without mutations in the MODY1, MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants. An identified missense variant was examined in association studies and genotype-phenotype studies.   We identified two silent and one missense (Pro75 Ala) variant. In an association study the allelic frequency of the Pro75Ala polymorphism was 3.2% (95% confidence interval, 1.9-4.5) in 330 patients with Type II diabetes mellitus compared with 4.2% (2.4-6.0) in 238 age-matched glucose tolerant control subjects. Moreover, in studies of 238 middle-aged glucose tolerant subjects, of 226 glucose tolerant offspring of Type II diabetic patients and of 367 young healthy subjects, the carriers of the polymorphism did not differ from non-carriers in glucose induced serum insulin or C-peptide responses.   Mutations in the coding region of the HNF-6 gene are not associated with Type II diabetes or with changes in insulin responses to glucose among the Caucasians examined."

    # predict
    result, para= predict_example(model= model, text= text, tokenizer= tokenizer, labels= labels, max_seq_length= 512, device= device)
    """
    result: list of entity was predicted
    para: new paragraph from original paragraph, different with original paragraph is that it was detokenized
    ex:
        original paragraph: (STN5)
        new paragraph: ( STN 5 )
    """ 
    entity_list = {}
    annotations_list = []
    for annotation in annotations:
        annotations_list += annotation
    
    print(result)
    
    for item in result:
        entity = ()
        start, end = find_word_location(item[0], para, entity_list)
        entity = entity + (start,end,item[1],item[0])
        for annotation in annotations_list:
            if annotation['text'].replace(" ", "") == entity[3].replace(" ", ""):
                if entity_list.get(annotation['infons']['identifier']) is None:
                    entity_list[annotation['infons']['identifier']] = [entity]
                    break
                else:
                    entity_list[annotation['infons']['identifier']].append(entity)
                    break                 
    print(entity_list)
    print(para)
    
    
if __name__ == "__main__":
    main()


