import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVGVzdCIsImlkIjoiNjQ1NDdlMWY2ZTY5ZjdmNTYwYmExMzQ3IiwiaW50ZXJmYWNlIjoiYXBpIiwicm9sZSI6InVzZXIiLCJlbWFpbCI6InJpbGV5LnZlbmFibGVAYXRsYXMtYmVuY2guY29tIiwicGVybWlzc2lvbnMiOltdLCJpYXQiOjE2ODMyNTg5OTgsImV4cCI6MjE1NjYyMjk5OH0.JG0KiEmIpTMrYeFtPZ87cIOvDZ9nf37Cv_P1V2kPfOY'
}

create_job_body = {
    'tag': 'html2docx',
    'tasks': {
        'upload-html': {
            'operation': 'import/upload',
        },
        'convert-to-docx': {
            'operation': 'convert',
            'input': 'upload-html',
            'output_format': 'docx'
        },
        'export-docx': {
            'operation': 'export/url',
            'input': 'convert-to-docx',
            'filename': 'some.zip'
        }
    }
}


result = requests.post(
    'https://api.freeconvert.com/v1/process/jobs',
    headers=headers,
    json=create_job_body
)

print(result.json())

# upload_config_result = result.json()['tasks'][0]

upload_config_json = result.json()['tasks'][0]

payload = {
  'signature': upload_config_json['result']['form']['parameters']['signature']
}
files= [('file',('input.html' ,open('./input.html','rb'),'html'))]

# URL will be dynamic and will differ from task to task
upload_result = requests.request('POST', upload_config_json['result']['form']['url'], headers=headers, data=payload, files=files)
print(upload_config_json['id'])

'''
convert_request_body = {
  'input': upload_config_json['id'],
  'output_format': 'docx',
}

print(convert_request_body)

convert_result = requests.post(
  'https://api.freeconvert.com/v1/process/convert',
  json = convert_request_body,
  headers = headers
)

convert_json = convert_result.json()
print(convert_json)
'''

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def job_started(data):
    print('the job started ', data)

@sio.event
def job_failed(data):
    print('the job failed ', data)
    sio.disconnect()

@sio.event
def job_completed(data):
    print('the job completed ', data)
    sio.disconnect()

@sio.event
def task_started(data):
    print('the task started ', data)
    
@sio.event
def task_failed(data):
    print('the task failed ', data)
    
@sio.event
def task_completed(data):
    print('the task completed ', data)

@sio.event
def disconnect():
    print('disconnected from server')

auth_header = {
    'token': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVGVzdCIsImlkIjoiNjQ1NDdlMWY2ZTY5ZjdmNTYwYmExMzQ3IiwiaW50ZXJmYWNlIjoiYXBpIiwicm9sZSI6InVzZXIiLCJlbWFpbCI6InJpbGV5LnZlbmFibGVAYXRsYXMtYmVuY2guY29tIiwicGVybWlzc2lvbnMiOltdLCJpYXQiOjE2ODMyNTg5OTgsImV4cCI6MjE1NjYyMjk5OH0.JG0KiEmIpTMrYeFtPZ87cIOvDZ9nf37Cv_P1V2kPfOY'
}

sio.connect('https://notification.freeconvert.com', transports= ["websocket"], auth=auth_header)
sio.emit('subscribe', 'job.' + result.json()['id'])
sio.emit('subscribe', 'user.' + upload_config_json['user']+'.tasks')
sio.wait()
