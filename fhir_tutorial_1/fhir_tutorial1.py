from fhirclient import client

settings={
'app_id':'test_app',
'api_base': 'http://test.fhir.org/r4/'

}

smart=client.FHIRClient(settings=settings)

import fhirclient.models.patient as p
import fhirclient.models.humanname as hn
import fhirclient.models.contactpoint as cp


patient1=p.Patient()

contact=cp.ContactPoint()
contact.system='phone'
contact.value='00999811119'
patient1.telecom=[contact]

name=hn.HumanName()
name.given=['Peter2']
name.family='Man'
patient1.name=[name]
patient1.gender='male'

#This won't show as it's not part of the FHIR spec
patient1.gender2='male'

print("Preview resource as JSON\n")
print(patient1.as_json())
print("\n")
print("Return from FHIR test server\n")
pt1_created=patient1.create(smart.server)
print(pt1_created)
