import React from "react";

// core components
import PageHeader from "components/PageHeader/PageHeader.js";
import Footer from "components/Footer/Footer.js";

import { Row, Col } from "reactstrap";

import ArticleInfo from "views/IndexSections/ArticleInfo.js"
import UtilTabs from "views/IndexSections/UtilTabs.js"

export default function ArticlePage() {
  React.useEffect(() => {
    document.body.classList.toggle("index-page");
    return function cleanup() {
      document.body.classList.toggle("index-page");
    };
  }, []);
  return (
    <>
      <PageHeader />
        <div className="wrapper">
          <div className="main">
            <Row>
              <Col lg="9" sm="6">
                <ArticleInfo />
              </Col>
              <Col lg="3" sm="6">
                <UtilTabs />
              </Col>
            </Row>
          </div>
            <Footer />
      </div>
    </>
  );
}
