import sys
import json
print(sys.version)
print(sys.executable)
items = json.loads('[{"id":1,"text":"Item1"}]')
for item in items:
    print(item['text'])