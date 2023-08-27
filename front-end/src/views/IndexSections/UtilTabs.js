import React, { useState, useEffect }  from "react";
import classnames from "classnames";
import axios from 'axios';
import {
    TabContent,
    TabPane,
    Container,
    Row,
    Col,
    Card,
    CardBody,
    Table,
    Nav,
    NavItem,
    NavLink,
} from "reactstrap";
import { useParams } from 'react-router-dom';

export default function UtilTabs() {

    const [currentActiveTab, setCurrentActiveTab] = React.useState('1');
    const { articleId } = useParams();
    const [data, setData] = useState([]);
    const [relationData, setRelationData] = useState([]);
    
    useEffect(() => {
        axios.get(`http://localhost:8000/api/v1/article/${articleId}`) 
            .then(response => {
                const apiData = response.data[0].entity_annotation;
                setData(apiData);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }, [articleId]);
        
    useEffect(() => {
        axios.get(`http://localhost:8000/api/v1/article/${articleId}/relations`)
            .then(response => {
                const apiData = response.data; 
                console.log(apiData);
                setRelationData(apiData);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, [articleId]);

    // Toggle active state for Tab
    const toggle = tab => {
        if (currentActiveTab !== tab) setCurrentActiveTab(tab);
    }

    const getRelationType = (relationTypeId) => {
        // Define the mapping of relation type IDs to the desired types
        const relationTypeMapping = {
            1: 'Positive Correlation',
            2: 'Negative Correlation',
            3: 'Association',
            4: 'Bind',
            5: 'Cause',
            6: 'Cotreatment',
            7: 'Drug Interaction',
            8: 'Comparison',
        };

        // Return the corresponding relation type for the given relation type ID
        return relationTypeMapping[relationTypeId] || 'Unknown';
    };

    return (
    <div className="section section-tabs" id="main-section-right">
        <Container id="util-tabs-container">
            <Card>
                <CardBody>
                    <Row>
                    {/* <Col className="ml-auto mr-auto" > */}
                    <Col className="col-util-tabs">
                        <Nav tabs>
                                <NavItem>
                                    <NavLink
                                        className={classnames({
                                            active:
                                                currentActiveTab === '1'
                                        })}
                                        onClick={() => { toggle('1'); }}
                                    >
                                        Annotation
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        className={classnames({
                                            active:
                                                currentActiveTab === '2'
                                        })}
                                        onClick={() => { toggle('2'); }}
                                    >
                                        Relation
                                    </NavLink>
                                </NavItem>
                        </Nav>
                        <TabContent activeTab={currentActiveTab}>
                            <TabPane tabId="1">
                            <div style={{ maxHeight: '700px', overflow: 'auto' }}>
                                <Table >
                                    <thead>
                                        <tr>
                                            <th>Type</th>
                                            <th>ID</th>
                                            <th>Text</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {data.map((item, index) => {
                                            return(
                                                <tr>
                                                    <td>{item.entity_type}</td>
                                                    <td>{item.entity_code}</td>
                                                    <td>{item.entity_name}</td>
                                                </tr>   
                                            )
                                        })}
                                    </tbody>
                                </Table>
                            </div>
                            </TabPane>
                            <TabPane tabId="2">
                                <div style={{ maxHeight: '500px', overflow: 'auto' }}>
                                    <Table >
                                        <thead>
                                            <tr>
                                                <th>Type</th>
                                                <th>Entities</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {relationData.map((item, index) => {
                                                console.log(item);
                                                return (
                                                    <tr key={index}>
                                                        <td>{getRelationType(item.relation_type_id)}</td>
                                                        <td><span class="entity_span_pair">{item.first_entity_id}</span>, <span class="entity_span_pair">{item.second_entity_id}</span></td>
                                                    </tr>
                                                );
                                            })}
                                        </tbody>
                                    </Table>
                                </div>
                            </TabPane>
                        </TabContent>
                    </Col>
                    </Row>
                </CardBody>
            </Card>
        </Container>
    </div>
  );
}
