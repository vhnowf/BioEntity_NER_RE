import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// reactstrap components
import {
  NavbarBrand,
  Navbar,
  FormGroup,
  Input,
  Container,
  Row,
  Col,
} from "reactstrap";

export default function IndexNavbar() {
  const [collapseOpen, setCollapseOpen] = React.useState(false);
  const [color, setColor] = React.useState("navbar-transparent");
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = () => {
    if (searchTerm) {
      navigate('/home');
      navigate(`/article/${searchTerm}`);
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
          <Col lg="7" sm="4">
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
          <Col lg="3" sm="4">
              {/* <Nav navbar>        
              <NavItem>
                <Button
                  className="nav-link d-none d-lg-block"
                  color="default"
                  onClick={scrollToDownload}
                >
                  <i className="tim-icons icon-cloud-download-93" /> Download
                </Button>
              </NavItem>
            </Nav> */}
          </Col>
          </Row>

        {/* </Collapse> */}
      </Container>
    </Navbar>
  );
}
