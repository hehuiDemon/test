#/usr/bin/env python3
import json

data = {
        "opt": {
            "hosts": [
                "192.168.3.61"
            ]
        }
}
print(json.dumps(data))