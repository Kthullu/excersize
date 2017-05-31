import json
import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://api.open-notify.org/iss-now.json')
a = json.loads(r.data.decode('utf-8'))


print (a['iss_position']['latitude'])
print (a['iss_position']['longitude'])
