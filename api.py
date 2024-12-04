import json
import uuid
import secrets

class Api:
    def __init__(self):
        self.uid = uuid.uuid4()
        self.str_uid = str(self.uid)
        self.api = self.uid.hex
        self.pk = secrets.token_hex(16)
        self.js = {"id":self.str_uid,"api-key":self.api,"private_key":self.pk}

    def save(self):
        with open("api_details.json",'w') as f:
            f.write(json.dumps(self.js))

    def info(self):
        return self.js

eht = "0x29F12Fef3D76f9d113A9a6f2D9c3D8314FD948cc"
api = Api()
print(api.info())

