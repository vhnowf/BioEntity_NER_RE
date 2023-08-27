import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Row, Col, Card, CardHeader, CardBody } from "reactstrap";
import { useParams } from "react-router-dom";
import BioConceptTabs from "./BioConceptTabs";

export default function ArticleInfo() {
  const { articleId } = useParams();
  const [data, setData] = useState([]);
  const [highlightGene, setHighlightGene] = useState(true);
  const [highlightChemical, setHighlightChemical] = useState(true);
  const [highlightMutation, setHighlightMutation] = useState(true);
  const [highlightDisease, setHighlightDisease] = useState(true);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/api/v1/article/${articleId}`)
      .then((response) => {
        const apiData = response.data;
        setData(apiData);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  const handleCheckboxChange = (name, checked) => {
    switch (name) {
      case "gene":
        setHighlightGene(checked);
        break;
      case "chemical":
        setHighlightChemical(checked);
        break;
      case "mutation":
        setHighlightMutation(checked);
        break;
      case "disease":
        setHighlightDisease(checked);
        break;
      default:
        break;
    }
  };

  const highlightEntities = (title, abstract, entityAnnotations) => {
    let highlightedTitle = title;
    let highlightedAbstract = abstract;

    const sortedAnnotations = [...entityAnnotations].sort(
      (a, b) => b.start_offset - a.start_offset
    );

    sortedAnnotations.forEach((entity) => {
      const { start_offset, end_offset, entity_type } = entity;
      const entityText = entity.entity_name;
      const className = getEntityClassName(entity_type);

      const highlightedEntity = `<span class="${className}">${entityText}</span>`;

      if (start_offset >= title.length) {
        // Entity is in the abstract section
        const abstractStartOffset = start_offset - (title.length + 1);
        const abstractEndOffset = end_offset - (title.length + 1);
        highlightedAbstract =
          highlightedAbstract.slice(0, abstractStartOffset) +
          highlightedEntity +
          highlightedAbstract.slice(abstractEndOffset);
      } else {
        // Entity is in the title section
        highlightedTitle =
          highlightedTitle.slice(0, start_offset) +
          highlightedEntity +
          highlightedTitle.slice(end_offset);
      }
    });

    return { highlightedTitle, highlightedAbstract };
  };

  const getEntityClassName = (entityType) => {
    if (entityType === "Gene" && highlightGene) {
      return "highlighted-entity gene_or_gene_product";
    } else if (entityType === "Disease" && highlightDisease) {
      return "highlighted-entity disease_or_phenotypic_feature";
    } else if (entityType === "Chemical" && highlightChemical) {
      return "highlighted-entity chemical_entity";
    } else if (entityType === "Mutation" && highlightMutation) {
      return "highlighted-entity sequence_variant";
    } else {
      return "un-highlighted-entity";
    }
  };

  return (
    <div className="section section-tabs" id="main-section-left">
      <Container id = "article-container">
        <Row>
          <Col lg="3" sm="6">
              <BioConceptTabs handleCheckboxChange={handleCheckboxChange} />
            </Col>
            <Col lg="9" sm="6">          
              {data.map((item, index) => {
                const { highlightedTitle, highlightedAbstract } = highlightEntities(
                  item.article.title,
                  item.article.abstract,
                  item.entity_annotation
                );
                const articleUrl = `https://pubmed.ncbi.nlm.nih.gov/${articleId}`;

                return (
                  <Row key={index}>
                    <Col className="col-article-info" md="12">
                      <Card>
                        <CardHeader>
                          <a className="meta-pmid-link" href={articleUrl}>
                            {" "}
                            PMID {item.article.pmid}
                          </a>
                          <div id="article-title">
                            <h2
                              dangerouslySetInnerHTML={{
                                __html: highlightedTitle,
                              }}
                            ></h2>
                          </div>
                          <div className="authors-list">
                            <span style={{"font-weight": 500}}>Authors: </span>
                            <span className="authors-item">
                              {item.article.authors}
                            </span>
                          </div>
                          <div className="passage abstract_title">Abstract</div>
                        </CardHeader>
                        <CardBody>
                          <div id="article-abstract">
                              <p
                                dangerouslySetInnerHTML={{
                                  __html: highlightedAbstract,
                                }}
                              ></p>
                          </div>
                        </CardBody>
                      </Card>
                    </Col>
                  </Row>
                );
              })}
            </Col>
        </Row>
        </Container>
      </div>
  );
}
