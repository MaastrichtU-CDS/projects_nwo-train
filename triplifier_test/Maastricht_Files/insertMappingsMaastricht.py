import requests

endpoint = "http://localhost:7200/repositories/Maastricht_rep/statements"

def addMapping(localTerm, targetClass, superClass):
    query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        INSERT {
            GRAPH <http://annotation.local/> {
                ?term owl:equivalentClass [
                    rdf:type owl:Class;
                    owl:intersectionOf [
                        rdf:first ?superClass;
                        rdf:rest [
                            rdf:first [
                                rdf:type owl:Class;
                                owl:unionOf [
                                    rdf:first [
                                        rdf:type owl:Restriction;
                                        owl:hasValue ?localValue;
                                        owl:onProperty <http://um-cds/ontologies/databaseontology/has_value>;
                                    ];
                                    rdf:rest rdf:nil;
                                ]
                            ];
                            rdf:rest rdf:nil;
                        ]
                    ]
                ].
            }
        } WHERE { 
            BIND(<%s> AS ?term).
            BIND(<%s> AS ?superClass).
            BIND("%s"^^xsd:string AS ?localValue).

        }
        """ % (targetClass, superClass, localTerm)

    annotationResponse = requests.post(endpoint,
    data="update="+query, 
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })
    print(annotationResponse.status_code)

#T stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48719", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48720", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("2", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48724", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("3", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48728", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")
addMapping("4", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48732", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48885")

#N stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48705", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48706", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("2", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48786", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")
addMapping("3", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48714", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48884")

#M stage
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48699", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48883")
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48700", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C48883")

#gender
addMapping("female", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C16576", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28421")
addMapping("male", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C20197", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28421")

#survival
addMapping("1", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C28554", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25717")
addMapping("0", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C37987", "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C25717")
