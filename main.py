import json
from wf import wf

print(json.dumps(wf.to_dict(), indent=4))
