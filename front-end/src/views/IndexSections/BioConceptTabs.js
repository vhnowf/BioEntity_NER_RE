// import React, { useState } from "react";
// import {
//   Container,
//   Row,
//   Col,
//   Label,
//   FormGroup,
//   Input,
//   Card,
//   CardBody,
// } from "reactstrap";


// export default function BioConceptTabs({ handleCheckboxChange }) {
//   const [checkboxes, setCheckboxes] = useState({
//     bioconcepts: false,
//     gene: true,
//     disease: true,
//     chemical: true,
//     mutation: true,
//   });

//   const handleCheckbox = (event) => {
//     const { name, checked } = event.target;
//     setCheckboxes((prevState) => ({ ...prevState, [name]: checked }));
//     handleCheckboxChange(name, checked);
//   };

//   return (
//     <div className="section section-tabs">
//       <Container>
//         <Row>
//           <Col className="col-bio-concept">
//             <Card>
//               <CardBody>
//                 <FormGroup check> 
//                   <Label check id="bio-concept-checkbox">
//                     <Input type="checkbox" name="bioconcepts" checked={checkboxes.bioconcepts}
//                       onChange={handleCheckbox} id="checkbox-id"/>
//                     <span className="form-check-sign" />
//                     BIOCONCEPTS
//                     </Label>
//                 </FormGroup>
//                 <FormGroup check>
//                   <Label check id="gene-checkbox">
//                     <Input defaultChecked type="checkbox" name="gene"
//                       checked={checkboxes.genes}
//                       onChange={handleCheckbox}/>
//                     <span className="form-check-sign" />
//                     GENE
//                   </Label>
//                 </FormGroup>
//                 <FormGroup check>
//                   <Label check id="disease-checkbox">
//                     <Input defaultChecked type="checkbox" name="disease"
//                       checked={checkboxes.disease}
//                       onChange={handleCheckbox}/>
//                     <span className="form-check-sign" name="disease"
//                       checked={checkboxes.disease}
//                       onChange={handleCheckbox} />
//                     DISEASE
//                   </Label>
//                 </FormGroup>
//                 <FormGroup check>
//                   <Label check id="chemical-checkbox">
//                     <Input defaultChecked type="checkbox" />
//                     <span className="form-check-sign" name="chemical"
//                       checked={checkboxes.chemical}
//                       onChange={handleCheckbox}/>
//                     CHEMICAL
//                   </Label>
//                 </FormGroup>
//                 <FormGroup check>
//                   <Label check id="mutation-checkbox">
//                     <Input defaultChecked type="checkbox" name="mutation"
//                       checked={checkboxes.mutation}
//                       onChange={handleCheckbox}/>
//                     <span className="form-check-sign" />
//                     MUTATION
//                   </Label>
//                 </FormGroup>
//               </CardBody>
//             </Card>
//           </Col>
//         </Row>
//       </Container>
//     </div>
//   );
// }

import React, { useState } from "react";
import { Container, Row, Col, Label, FormGroup, Input, Card, CardBody } from "reactstrap";

export default function BioConceptTabs({ handleCheckboxChange }) {
  const [checkboxes, setCheckboxes] = useState({
    gene: true,
    disease: true,
    chemical: true,
    mutation: true,
  });

  const handleCheckbox = (event) => {
    const { name, checked } = event.target;
    setCheckboxes((prevState) => ({ ...prevState, [name]: checked }));
    // Notify the parent component of the checkbox changes
    // Only if handleCheckboxChange is a function
    if (typeof handleCheckboxChange === "function") {
      handleCheckboxChange(name, checked);
    }
  };

  return (
    <div className="section section-tabs" id="bio-concept-section">
      <Container>
        <Row>
          <Col className="col-bio-concept">
            <Card>
              <CardBody>
                <FormGroup check>
                  <Label check id="gene-checkbox">
                    <Input
                      type="checkbox"
                      name="gene"
                      checked={checkboxes.gene}
                      onChange={handleCheckbox}
                    />
                    <span className="form-check-sign" />
                    GENE
                  </Label>
                </FormGroup>
                <FormGroup check>
                  <Label check id="disease-checkbox">
                    <Input
                      type="checkbox"
                      name="disease"
                      checked={checkboxes.disease}
                      onChange={handleCheckbox}
                    />
                    <span className="form-check-sign" />
                    DISEASE
                  </Label>
                </FormGroup>
                <FormGroup check>
                  <Label check id="chemical-checkbox">
                    <Input
                      type="checkbox"
                      name="chemical"
                      checked={checkboxes.chemical}
                      onChange={handleCheckbox}
                    />
                    <span className="form-check-sign" />
                    CHEMICAL
                  </Label>
                </FormGroup>
                <FormGroup check>
                  <Label check id="mutation-checkbox">
                    <Input
                      type="checkbox"
                      name="mutation"
                      checked={checkboxes.mutation}
                      onChange={handleCheckbox}
                    />
                    <span className="form-check-sign" />
                    MUTATION
                  </Label>
                </FormGroup>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
