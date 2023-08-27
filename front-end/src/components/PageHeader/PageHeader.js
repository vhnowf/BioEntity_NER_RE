import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import axios from "axios";
// reactstrap components
import {
  Button,
  NavbarBrand,
  Navbar,
  NavItem,
  FormGroup,
  Input,
  Nav,
  Container,
  Row,
  Col,
} from "reactstrap";
import { useParams } from "react-router-dom";

export default function IndexNavbar() {
  const [collapseOpen, setCollapseOpen] = React.useState(false);
  const [color, setColor] = React.useState("navbar-transparent");
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState("");
  const { articleId } = useParams();
  const handleSearch = () => {
    if (searchTerm) {
      navigate(`/article/${searchTerm}`);
    }
  };

  const handleDownload = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/api/v1/article/download/${articleId}`, {
        responseType: "blob", // Specify that the response type is a binary blob
      });

      // Create a blob URL for the response data
      const blobUrl = URL.createObjectURL(response.data);

      // Create a downloadable link
      const downloadLink = document.createElement("a");
      downloadLink.href = blobUrl;
      downloadLink.download = `${articleId}.txt`; // Change the filename as needed
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    } catch (error) {
      console.error("Error downloading file:", error);
    }
  };

  React.useEffect(() => {
    window.addEventListener("scroll", changeColor);
    return function cleanup() {
      window.removeEventListener("scroll", changeColor);
    };
  }, []);
  const changeColor = () => {
    if (
      document.documentElement.scrollTop > 99 ||
      document.body.scrollTop > 99
    ) {
      setColor("bg-info");
    } else if (
      document.documentElement.scrollTop < 99 ||
      document.body.scrollTop < 99
    ) {
      setColor("bg-info");
    }
  };
  const toggleCollapse = () => {
    document.documentElement.classList.toggle("nav-open");
    setCollapseOpen(!collapseOpen);
  };
  return (

    <Navbar id="navbar-header" className={"fixed-top " + color} color-on-scroll="100" expand="lg">
      <Container>
        <Row id="header-navbar-container-row">
          <Col lg="3" sm="4">
            <div className="navbar-translate">
              <NavbarBrand to="/" tag={Link} id="navbar-brand">
                <span>BIO• </span>
                NER & RE tool
              </NavbarBrand> 
              <button
                aria-expanded={collapseOpen}
                className="navbar-toggler navbar-toggler"
                onClick={toggleCollapse}
              >
                <span className="navbar-toggler-bar bar1" />
                <span className="navbar-toggler-bar bar2" />
                <span className="navbar-toggler-bar bar3" />
              </button>
            </div>
          </Col>
          <Col lg="5" sm="4">
            <FormGroup>
            <Input
              defaultValue=""
              placeholder="Enter article ID"
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleSearch();
                }
              }}
            />
          </FormGroup>
          </Col>
          <Col lg="4" sm="4">
              <Nav navbar>        
              <NavItem>
                <Button
                  className="nav-link d-none d-lg-block"
                  color="default"
                  onClick={handleDownload}
                >
                  <i className="tim-icons icon-cloud-download-93" /> Download
                </Button>
              </NavItem>
            </Nav>
          </Col>
          </Row>

        {/* </Collapse> */}
      </Container>
    </Navbar>
  );
}
