import json
from datetime import datetime,timezone,timedelta
res_data = {
	"commit_at":datetime.strftime(datetime.now(timezone.utc),"%Y-%m-%d %H:%M:%S-%Z"),
	"ctime":"2018-10-25 01:14:19-UTC",
	"disease_id":"1836sahf57y",
	"first_doctor_contact":"+861372587791",
	"first_doctor_name":"医生",
	"first_hospital":"人民医院",
	"hospital_id":"766fhgytc5",
	"note":"Something",
	"patient_id":"275dmsj875",
	"res_id":"1927cngl90",
	"slot_id":"1mdhs5fb78",
	"customer_id":"1mcn5330km",
	"document_id":"378shfn890"
}
disease_data = {
	"id":"1836sahf57y",
	"name":"Demo Disease",
}
hospital_data = {
	"id":"766fhgytc5",
	"name":"Demo Hospital"
}
patient_data =  {
	"id":"275dmsj875",
	"name":"Deom Patient"
}
slot_data = {
	"id":"1mdhs5fb78",
	"week_start":"2018-10-29",
	"week_end":"2018-11-04"
}
customer_data = {
	"id":"1mcn5330km",
	"address":"北京市朝阳区",
	"age":58,
	"email":"demo@gmail.com",
	"name":"Demo Customer",
	"gender":"M"
}
document_data =  {
	"id":"378shfn890",
	"description":"A demo document",
	"name":"A demo document"
}

with open('reservation','w',encoding='utf-8') as out:
	out.write(json.dumps(res_data,ensure_ascii=False))

with open('disease','w') as out:
	out.write(json.dumps(disease_data))

with open('hospital','w') as out:
	out.write(json.dumps(hospital_data))

with open('patient','w') as out:
	out.write(json.dumps(patient_data))

with open('slot','w') as out:
	out.write(json.dumps(slot_data))

with open('cusomter','w',encoding='utf-8') as out :
	out.write(json.dumps(customer_data,ensure_ascii=False))

with open('document','w') as out:
	out.write(json.dumps(document_data))