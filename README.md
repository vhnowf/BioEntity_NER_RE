# Name Entity Recognition and Relation Extraction from BioRED dataset
### Introduction
The project focuses on the task of named entity recognition (NER) and relation extraction (RE) on the BioRED dataset. In this repository, I provide the training code, pre-trained models, and data processing code. Additionally, I have included a simple website for utilizing the NER&RE system.
## Content
- [Annotation](#annotation)
This folder contains all file to convert biomedical enitites to their indetifier codes.
- [PubRunner](#pubrunner)
Framework to download abstracts from PubMED
- [PubTator](#pubtator)
Run cmd: pubrunner --test . (to get abstract from config file)
- [BioRED-NER-RE](#ner-re-biored)
- [Named Entity Recognition](#named-entity-recognition)
    Firstly, run the rungeneratedata.sh to get dataset.
    Secondly, add variables into runcode.sh and run it to get result of NER task. 
- [Relation Extraction](#relation-extraction)
    Firstly, run the rungeneratedata.sh to get dataset.
    Secondly, add variables into run_re.sh and run it to get result of RE task. 
- [Combine Flow Run](#combine-run)
    Run file run.sh (in folder BioRED-NER-RE) to get a full flow from download an article to get enitites and their relations.
- [Website](#web-site)
    [Back-end]
    Run cmd: npm start
    [Front-end]
    Run cmd: npm run start 
- [Contact](#contact)
    If you have any questions or related concerns, please direct me to namvohoang.contact@gmail.com


