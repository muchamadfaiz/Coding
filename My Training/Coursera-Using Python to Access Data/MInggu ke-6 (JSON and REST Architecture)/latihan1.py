import json
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type : "intl",
        "number" : "+1 734 303 456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)

