import json
import io
from datetime import datetime,timezone,timedelta
res_data = {
    "commit_at":datetime.strftime(datetime.now(timezone.utc),"%Y-%m-%d %H:%M:%S-%Z"),
    "ctime":"2018-10-25 01:14:19-UTC",
    "disease_id":"1836sahf57y",
    "first_doctor_contact":"+861372587791",
    "first_doctor_name":u"医生",
    "first_hospital":u"人民医院",
    "hospital_id":"766fhgytc5",
    "note":"Something",
    "patient_id":"275dmsj875",
    "res_id":"1927cngl90",
    "time_slot_id":"1mdhs5fb78",
    "user_id":"1mcn5330km",
}
user_data = {
    "user_id":"1mcn5330km",
    "name": u"张三",
    "email": "123456789@qq.com",
    "phone": "13801234567",
    "wechat": "wxid_123456789",
}
disease_data = {
    "disease_id":"1836sahf57y",
    "name":"Demo Disease",
}
hospital_data = {
    "hospital_id":"766fhgytc5",
    "name":"Demo Hospital",
    "address": u"美国纽约市",
}
patient_data =  {
    "patient_id":"275dmsj875",
    "name":u"张三丰",
    "pinyin": "Zhang Sanfeng",
    "gender": 1,
    "birthdate": "1960-01-01",
    "relationship": "parent",
    "passport": "E12346789",
}
time_slot_data = {
    "time_slot_id":"1mdhs5fb78",
    "week":"2"
}

quick_json_dump = lambda obj: json.dumps(obj, ensure_ascii=False)
quick_open = lambda fname, mode: io.open(fname, mode, encoding='utf-8')

with quick_open('reservation','w') as out:
    out.write(quick_json_dump(res_data))

with quick_open('disease/'+disease_data['disease_id'],'w') as out:
    out.write(quick_json_dump(disease_data))

with quick_open('hospital/'+hospital_data['hospital_id'],'w') as out:
    out.write(quick_json_dump(hospital_data))

with quick_open('user/%s/patient/%s' % (user_data['user_id'], patient_data['patient_id']),'w') as out:
    out.write(quick_json_dump(patient_data))

with quick_open('user/%s/info' % (user_data['user_id']),'w') as out:
    out.write(quick_json_dump(user_data))

with quick_open('time_slot/'+time_slot_data['time_slot_id'],'w') as out:
    out.write(quick_json_dump(time_slot_data))
