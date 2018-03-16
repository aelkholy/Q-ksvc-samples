import os
import json
import schema
import resolvers
from shared.kinddbsvc.KindDBSvc import KindDBSvc

kindDB = KindDBSvc(0, os.getenv('KINDDB_SERVICE_URL', 'http://localhost:8008/graphql'))

async def handle_file(x):
    # This is where you'd have more complicated logic for a handler on a file drop!
    out = json.loads(x)
    file_added = out["fileAdded"]
    file_name = file_added["name"]
    file_id = file_added["id"]
    mime = file_added["mime"]

    print("Got: kId: {} kName: {}".format(file_id, file_name))

    if mime == "text/plain":
        res = await kindDB.getAllInstances(kindId=id)
        base = res.get("allInstances")
        sentences = []
        if base is not None:
            records = base.get["records"]
            for r in records:
                sentences.append(resolvers.add_sentence(schema.Sentence(id=r[0].get("ID"), text=r[1].get("STRING"))))

        return sentences

    else:
        return []
