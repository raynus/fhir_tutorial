from fhirclient import client

settings={
'app_id':'test_app',
'api_base': 'http://test.fhir.org/r4/'

}



## REMOVE ID FIELD 
gen_json={
  "resourceType": "Patient",
  "name": [
    {
      "use": "official",
      "given": [
        "Peter"
      ],
      "family": "Man"
    }
  ],
  "gender": "male"
}

smart=client.FHIRClient(settings=settings)

import fhirclient.models.patient as p
patient_gen=p.Patient(gen_json)



#Change gender to female
patient_gen.gender="female"



print("Preview resource as JSON\n")
print(patient_gen.as_json())
print("\n")
print("Return from FHIR test server\n")
pt1_created=patient_gen.create(smart.server)
print(pt1_created)
