from ultil_re import *
from typing import Dict
from transformers import AutoConfig, AutoTokenizer, AutoModelForTokenClassification, InputFeatures, AutoModelForSequenceClassification
import numpy as np
from tqdm import tqdm
import torch
from torch.utils.data import DataLoader
from function import *


def main():
    """
    this code using 2 model:
        - model1: predict the pair of entity is relation or not (0: no relation, 1: has relation)
        - model2: predict the type of relation (8 types)
    """
    # Load model and tokenizer

    device= torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    parent_dir = os.path.dirname(os.getcwd())
    model_path1= os.path.join(parent_dir, 'RE BioRED', 'model', 'PubmedBert_Task1') 
    model_path2= os.path.join(parent_dir, 'RE BioRED', 'model', 'PubmedBert_Task2')
    tokenize_path= os.path.join(parent_dir, 'RE BioRED', 'model', 'PubmedBertTokenizer')

    label1= ['No_Relation', 'Relation']
    label2= ['Association', 'Bind', 'Comparison', 'Conversion', 'Cotreatment', 'Drug_Interaction', 'Negative_Correlation', 'Positive_Correlation']
    label_map1: Dict[int, str] = {i: label for i, label in enumerate(label1)}
    label_map2: Dict[int, str] = {i: label for i, label in enumerate(label2)}
    num_label1= len(label1)
    num_label2= len(label2)

    label_map= {i: label for i, label in enumerate(get_labels())}

    config1 = AutoConfig.from_pretrained(model_path1, num_labels=num_label1, 
                                        id2label=label_map1, label2id={label: i for i, label in enumerate(label1)})
    tokenizer = AutoTokenizer.from_pretrained(tokenize_path)

    model1 = AutoModelForSequenceClassification.from_pretrained(model_path1, config=config1)

    config2 = AutoConfig.from_pretrained(model_path2, num_labels=num_label2, 
                                        id2label=label_map2, label2id={label: i for i, label in enumerate(label2)})

    model2 = AutoModelForSequenceClassification.from_pretrained(model_path2, config=config2)

    # Load data
    text= "Hepatocyte nuclear factor - 6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion. The transcription factor hepatocyte nuclear factor ( HNF ) - 6 is an upstream regulator of several genes involved in the pathogenesis of maturity - onset diabetes of the young. We therefore tested the hypothesis that variability in the HNF - 6 gene is associated with subsets of Type II ( non - insulin - dependent ) diabetes mellitus and estimates of insulin secretion in glucose tolerant subjects. We cloned the coding region as well as the intron - exon boundaries of the HNF - 6 gene. We then examined them on genomic DNA in six MODY probands without mutations in the MODY1, MODY3 and MODY4 genes and in 54 patients with late - onset Type II diabetes by combined single strand conformational polymorphism - heteroduplex analysis followed by direct sequencing of identified variants. An identified missense variant was examined in association studies and genotype - phenotype studies. We identified two silent and one missense ( Pro75 Ala ) variant. In an association study the allelic frequency of the Pro75Ala polymorphism was 3. 2 % ( 95 % confidence interval, 1. 9 - 4. 5 ) in 330 patients with Type II diabetes mellitus compared with 4. 2 % ( 2. 4 - 6. 0 ) in 238 age - matched glucose tolerant control subjects. Moreover, in studies of 238 middle - aged glucose tolerant subjects, of 226 glucose tolerant offspring of Type II diabetic patients and of 367 young healthy subjects, the carriers of the polymorphism did not differ from non - carriers in glucose induced serum insulin or C - peptide responses. Mutations in the coding region of the HNF - 6 gene are not associated with Type II diabetes or with changes in insulin responses to glucose among the Caucasians examined."

    """
    text: raw text
    """
    entity_list= {'3175': [(0, 29, 'GeneOrGeneProduct', 'Hepatocyte nuclear factor - 6'), (187, 224, 'GeneOrGeneProduct', 'hepatocyte nuclear factor ( HNF ) - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6'), (398, 405, 'GeneOrGeneProduct', 'HNF - 6')], 'MESH:D003924': [(77, 93, 'DiseaseOrPhenotypicFeature', 'type II diabetes'), (441, 496, 'DiseaseOrPhenotypicFeature', 'Type II ( non - insulin - dependent ) diabetes mellitus'), (800, 816, 'DiseaseOrPhenotypicFeature', 'Type II diabetes'), (800, 816, 'DiseaseOrPhenotypicFeature', 'Type II diabetes'), (1264, 1289, 'DiseaseOrPhenotypicFeature', 'Type II diabetes mellitus'), (1489, 1505, 'DiseaseOrPhenotypicFeature', 'Type II diabetic'), (800, 816, 'DiseaseOrPhenotypicFeature', 'Type II diabetes'), (800, 816, 'DiseaseOrPhenotypicFeature', 'Type II diabetes')], '3630': [(143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (1654, 1665, 'GeneOrGeneProduct', 'C - peptide'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin'), (143, 150, 'GeneOrGeneProduct', 'insulin')], 'MESH:D005947': [(535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose'), (535, 542, 'ChemicalEntity', 'glucose')], '3172': [(734, 739, 'GeneOrGeneProduct', 'MODY1')], '6927': [(741, 746, 'GeneOrGeneProduct', 'MODY3')], '3651': [(751, 756, 'GeneOrGeneProduct', 'MODY4')], 'rs74805019': [(1094, 1103, 'SequenceVariant', 'Pro75 Ala'), (1168, 1176, 'SequenceVariant', 'Pro75Ala')]}
    # as form: {code: (N, start, end, type, ent_text)}
    # about entity_list:
    """
    code: code of entity
    N: N entity has same code (because one code can have many entity)
    start: start of entity
    end: end of entity
    type: type of entity
    ent_text: text of entity
    """

    # Convert raw text to input features
    feature, code_pair= convert_text_to_input_bert(text= text, entity_list= entity_list, tokenizer= tokenizer, max_seq_length= 512)
    test_dataset= REDatasetForPredict(features= feature)
    data= DataLoader(test_dataset, batch_size= 1, shuffle= False, num_workers= 4)

    # Predict
    pred= predict(model1, model2, data, device)

    # Result
    result= []
    for i in range(len(pred)):
        if pred[i]!= 8:
            result.append((code_pair[i], label_map[pred[i]]))
    """
    result: list of tuple (code_pair, relation)
    """
    print(result)
    #[(('3175', 'MESH:D003924'), 'Association'), (('3175', '3172'), 'Association'), (('3175', '6927'), 'Association'), (('3175', '3651'), 'Association'), (('3175', 'rs74805019'), 'Association'), (('MESH:D003924', '3172'), 'Association'), (('MESH:D003924', '6927'), 'Association'), (('MESH:D003924', '3651'), 'Association'), (('MESH:D003924', 'rs74805019'), 'Association')]

if __name__ == "__main__":
    main()

    






