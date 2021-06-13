import json

from elasticsearch import Elasticsearch

from app.actions import BaseActions
from app.models import Post
from app.db.session import SessionLocal

# actions = BaseActions(Post)

session = SessionLocal()

posts = session.query(Post).all()

# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# i = 0
# for instance in posts:
#     body = json.dumps(instance.__dict__)
#     es.index(index='posts', doc_type='_doc', id=i, body=body)
#     i = i+1
