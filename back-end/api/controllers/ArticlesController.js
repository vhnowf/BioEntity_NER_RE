'use strict'

const util = require('util')
const mysql = require('mysql')
const db = require('./../db')

module.exports = {
    get: (req, res) => {
        let sql = 'SELECT * FROM documents'
        db.query(sql, (err, response) => {
            if (err) throw err
            res.json(response)
        })
    },
    detail: (req, res) => {
        let result = []
        let item = {}
        let sql = 'SELECT * FROM documents INNER JOIN biomedical_entity be ON pmid = be.document_id INNER JOIN  enity_type et ON et.id = be.entity_type_id WHERE  pmid = ?'
        db.query(sql, [req.params.articleId], (err, response) => {
            if (err) throw err
            item["article"] = {}
            item["article"]["pmid"] = response[0]['pmid']
            item["article"]["title"] = response[0]['title']
            item["article"]["abstract"] = response[0]['abstract']
            item["article"]["authors"] = response[0]['authors']
            item["entity_annotation"] = []
            for (let entity of response) {
                let ent_ann = {}
                ent_ann['entity_name'] = entity['name']
                ent_ann['entity_code'] = entity['code']
                switch (entity['type_name']) {
                    case 'gene_or_gene_product':
                        ent_ann['entity_type'] = 'Gene';
                        break;
                    case 'disease_or_phenotypic_feature':
                        ent_ann['entity_type'] = 'Disease';
                        break;
                    case 'chemical_entity':
                        ent_ann['entity_type'] = 'Chemical';
                        break;
                    case 'sequence_variant':
                        ent_ann['entity_type'] = 'Mutation';
                        break;
                    default:
                        ent_ann['entity_type'] = entity['type_name'];
                }
                ent_ann['start_offset'] = entity['start']
                ent_ann['end_offset'] = entity['end']
                item["entity_annotation"].push(ent_ann)
            }
            result.push(item)
            res.json(result)
        })
    },
    relation: (req, res) => {
        let sql = 'SELECT * FROM entity_relation WHERE document_id = ?'
        db.query(sql, [req.params.articleId], (err, response) => {
            if (err) throw err
            res.json(response)
        })
    },
    search: (req, res) => {
        let sql = "SELECT * FROM documents a WHERE a.title LIKE '%" + req.params.keyword  + "%'"
        db.query(sql, (err, response) => {
            if (err) throw err
            res.json(response)
        })
    }
}