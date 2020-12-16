from django.db import models

from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
# Create your models here.
# config.DATABASE_URL = 'bolt://neo4j:neo4j@127.0.0.1:7687'
# config.MAX_POOL_SIZE  = 50

class Domain(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    name = StringProperty(index=True, default="domain")

class Concept(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    # Relations :
    domain = RelationshipTo(Domain, 'EXISTS_IN')
    nodes = RelationshipTo('Concept','CONNECTED')