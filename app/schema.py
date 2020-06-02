from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Application as ApplicationModel
from graphene import relay, ObjectType, Schema


class Application(SQLAlchemyObjectType):
    class Meta:
        model = ApplicationModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    node = relay.Node.Field()
    all_applications = SQLAlchemyConnectionField(Application)


schema = Schema(query=Query)
