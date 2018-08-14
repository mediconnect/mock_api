define({ "api": [
  {
    "type": "get",
    "url": "/hospitals/:query",
    "title": "医院搜索列表",
    "name": "______",
    "group": "Hospital",
    "description": "<p>根据搜索词显示医院列表</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Srtring",
            "optional": false,
            "field": "query",
            "description": "<p>搜索词（模拟api中只有center、clinic两词有效）</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "hospital",
            "description": "<p>医院列表</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "hospital.name",
            "description": "<p>医院名</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "hospital.summary",
            "description": "<p>医院简介</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "hospital.rank",
            "description": "<p>医院排名</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "hospital.price",
            "description": "<p>预约和咨询费用</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "hospital.avail",
            "description": "<p>最近可约时间</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "api/hospital.py",
    "groupTitle": "Hospital"
  }
] });
