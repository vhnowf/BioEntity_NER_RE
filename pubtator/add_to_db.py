import argparse
import os
import sys

from bioc import biocxml
from dotenv import load_dotenv
from mongoengine import *

from schema import PubmedDocument, PubmedAnnotation, AnnotationType

load_dotenv()
MONGO_DB = os.getenv('MONGO_DB')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PWD = os.getenv('MONGO_PWD')


def get_kb_id(ann_info):
    kbid = None
    if 'Chemical' in ann_info['type'] or 'Disease' in ann_info['type']:
        if ann_info.get('MESH'):
            kbid = [{'kb_type': 'MESH', 'kb_id': ann_info.get('MESH')}]
    elif 'Gene' in ann_info['type']:
        if ann_info.get('NCBI Gene'):
            kbid = [{'kb_type': 'NCBI Gene ID', 'kb_id': ann_info.get('NCBI Gene')}]
    elif ann_info.get('Identifier'):
        identifiers = ann_info.get('Identifier', '')
        l_identifier = identifiers.split(';')
        has_rs_id = False
        for kb_id in l_identifier:
            if 'RS' in kb_id.split(':')[0]:
                has_rs_id = True
        if has_rs_id:
            kbid = [{'kb_type': mut_kb_id.split(':')[0], 'kb_id': mut_kb_id.split(':')[1]} for mut_kb_id in
                     l_identifier]
    return kbid


def get_ann_type(ann_info):
    annotation_type = None
    if 'Chemical' in ann_info['type']:
        annotation_type = AnnotationType.Chemical
    elif 'Disease' in ann_info['type']:
        annotation_type = AnnotationType.Disease
    elif 'Gene' in ann_info['type']:
        annotation_type = AnnotationType.Gene
    elif ann_info.get('Identifier'):
        annotation_type = AnnotationType.Mutation
    return annotation_type


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add processed data to database')
    parser.add_argument('--inBioc', required=True, type=str, help='Input BioC XML file')

    args = parser.parse_args()
    in_bioc = os.path.abspath(args.inBioc)

    assert os.path.isfile(in_bioc), "Could not access input: %s" % in_bioc
    if not os.path.getsize(in_bioc):
        sys.exit()
    input_file = open(in_bioc)
    input_data = biocxml.load(input_file)
    # with SSHTunnelForwarder(
    #     (SERVER_HOST, SERVER_PORT),
    #     ssh_username=MONGO_USER,
    #     ssh_password=MONGO_PWD,
    #     remote_bind_address=(MONGO_HOST, MONGO_PORT)) as server:
    #     server.start()
    connect(MONGO_DB, host=MONGO_HOST, port=int(MONGO_PORT), username=MONGO_USER, password=MONGO_PWD,
            authentication_source=MONGO_DB)

    for document in input_data.documents:
        pubmed_doc = PubmedDocument(pmid=document.id)
        for passage in document.passages:
            if 'title' in passage.infons.get('section', ''):
                pubmed_doc.title = passage.text

            if 'abstract' in passage.infons.get('section', ''):
                pubmed_doc.abstract = passage.text

            PubmedAnnotation.objects(pmid=document.id).delete()
            for i, ann in enumerate(passage.annotations):

                kb_ids = get_kb_id(ann.infons)
                if not kb_ids:
                    continue
                pubmed_ann = PubmedAnnotation(pmid=document.id)
                pubmed_ann.kb_ids = kb_ids
                pubmed_ann.ann_type = get_ann_type(ann.infons)
                pubmed_ann.start_offset = ann.locations[0].offset +1
                pubmed_ann.end_offset = ann.locations[0].offset + ann.locations[0].length +1
                pubmed_ann.ann_text = ann.text
                pubmed_ann.update(upsert=True,
                                  set__ann_type=pubmed_ann.ann_type,
                                  set__kb_ids=pubmed_ann.kb_ids,
                                  set__start_offset=pubmed_ann.start_offset,
                                  set__end_offset=pubmed_ann.end_offset,
                                  set__ann_text=pubmed_ann.ann_text,
                                  )
        pubmed_doc.update(upsert=True, set__title=pubmed_doc.title, set__abstract=pubmed_doc.abstract)
