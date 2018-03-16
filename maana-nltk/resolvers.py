import os
import uuid
import schema
from shared.kinddbsvc.KindDBSvc import KindDBSvc

kindDB = KindDBSvc(0, os.getenv('KINDDB_SERVICE_URL', 'http://localhost:8008/graphql'))


def info():
    return schema.Info(
        id="ab739864-c0ff-40aa-bcdf-972c0bc794dd",
        name="Maana NLTK service",
        description="This is a service for using NLTK with MaanaQ"
    )

async def all_sentences():
    sentences_res = await kindDB.getAllInstances(kindName="Sentence")
    base = sentences_res.get("allInstances")
    sentences = []
    if base is not None:
        records = base.get["records"]
        for r in records:
            sentences.append(schema.Sentence(id=r[0].get("ID"), text=r[1].get("STRING")))
    return sentences

async def sentence(input):
    sentences_res = await kindDB.getInstance(kindName="Sentence", instanceId=input.id)
    base = sentences_res.get("instance")
    r = base.get["records"][0]
    return schema.Sentence(id=r[0].get("ID"), text=r[1].get("STRING"))


async def add_sentence(sentence):
    new_sentence = schema.Sentence(id=sentence.get("id", str(uuid.uuid4())), text=sentence.get("text"))
    await kindDB.addInstanceByKindName(
        "Employee",
        {
            "id": new_sentence.id,
            "name": new_sentence.text
        }
    )

    return new_sentence
