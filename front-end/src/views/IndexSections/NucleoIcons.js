import React from "react";
// reactstrap components
import { Container, Row, Col } from "reactstrap";

export default function NucleoIcons() {
  return (
    <div className="section section-nucleo-icons">
      <img alt="..." className="path" src={require("assets/img/path3.png")} />
      <Container>
        <Row className="justify-content-center">
          <Col lg="8" md="12">
            <br/>
            <br/>
            <br/>
            <h2 className="title">Named entity recognition & relation extraction for biodemical enitities in cancer related articles tool</h2>
            <h4 className="description">
            Until now, cancer remains one of the significant and top priorities in the field of healthcare, both in Vietnam and worldwide. This website provides a tool to assist in the identification of biomedical entities and the extraction of their relationships from research articles from PubMed.
            </h4>
            <br/>
            <br/>
            <br/>
          </Col>
        </Row>
        <div className="blur-hover">
          <a href="https://demos.creative-tim.com/blk-design-system-react/#/documentation/icons">
            <div className="icons-container blur-item on-screen mt-5">
              {/* Center */}
              <i className="icon tim-icons icon-atom" />
              {/* Right 1 */}
              <i className="icon icon-sm tim-icons icon-paper" />
              <i className="icon icon-sm tim-icons icon-money-coins" />
              <i className="icon icon-sm tim-icons icon-link-72" />
              {/* Right 2 */}
              <i className="icon tim-icons icon-send" />
              <i className="icon tim-icons icon-cloud-download-93" />
              <i className="icon tim-icons icon-pencil" />
              {/* Left 1 */}
              <i className="icon icon-sm tim-icons icon-key-25" />
              <i className="icon icon-sm tim-icons icon-atom" />
              <i className="icon icon-sm tim-icons icon-sound-wave" />
              {/* Left 2 */}
              <i className="icon tim-icons icon-tag" />
              <i className="icon tim-icons icon-tap-02" />
              <i className="icon tim-icons icon-zoom-split" />
            </div>
            <span className="blur-hidden h5 text-primary">
              Explore all the 33000+ articles
            </span>
          </a>
        </div>
      </Container>
    </div>
  );
}
