import requests

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVGVzdCIsImlkIjoiNjQ1NDdlMWY2ZTY5ZjdmNTYwYmExMzQ3IiwiaW50ZXJmYWNlIjoiYXBpIiwicm9sZSI6InVzZXIiLCJlbWFpbCI6InJpbGV5LnZlbmFibGVAYXRsYXMtYmVuY2guY29tIiwicGVybWlzc2lvbnMiOltdLCJpYXQiOjE2ODMyNTg5OTgsImV4cCI6MjE1NjYyMjk5OH0.JG0KiEmIpTMrYeFtPZ87cIOvDZ9nf37Cv_P1V2kPfOY'
}

upload_config_result = requests.post(
  'https://api.freeconvert.com/v1/process/import/upload',
  headers = headers
)

upload_config_json = upload_config_result.json()

payload = {
  'signature': upload_config_json["result"]["form"]["parameters"]["signature"]
}
files= [('file',("input.html" ,open("./input.html",'rb'),'html'))]

# URL will be dynamic and will differ from task to task
upload_result = requests.request('POST', upload_config_json['result']['form']['url'], headers=headers, data=payload, files=files)
print(upload_config_json['id'])

convert_request_body = {
  "input": upload_config_json['id'],
  "output_format": "docx",
}

print(convert_request_body)

convert_result = requests.post(
  'https://api.freeconvert.com/v1/process/convert',
  json = convert_request_body,
  headers = headers
)

convert_json = convert_result.json()

export_body = {
  "input": [
        convert_json['id']
  ],
  "filename": "some.zip",
  "archive_multiple_files": True
}

export_result = requests.post('https://api.freeconvert.com/v1/process/export/url', headers = headers, json = export_body)

print(export_result.json())

r = requests.get('https://api.freeconvert.com/v1/process/tasks', headers = headers)

print(r.json())