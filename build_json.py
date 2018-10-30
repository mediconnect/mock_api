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
	"time_slot_id":"1mdhs5fb78",
	"user_id":"1mcn5330km",
}
disease_data = {
	"disease_id":"1836sahf57y",
	"name":"Demo Disease",
}
hospital_data = {
	"hospital_id":"766fhgytc5",
	"name":"Demo Hospital"
}
patient_data =  {
	"patient_id":"275dmsj875",
	"name":"Deom Patient"
}
time_slot_data = {
	"time_slot_id":"1mdhs5fb78",
	"week":"2"
}

with open('reservation.json','w',encoding='utf-8') as out:
	out.write(json.dumps(res_data,ensure_ascii=False))

with open('disease.json','w') as out:
	out.write(json.dumps(disease_data))

with open('hospital.json','w') as out:
	out.write(json.dumps(hospital_data))

with open('patient.json','w') as out:
	out.write(json.dumps(patient_data))

with open('time_slot.json','w') as out:
	out.write(json.dumps(time_slot_data))