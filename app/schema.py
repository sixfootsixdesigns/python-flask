import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Application as ApplicationModel
from graphene import relay


class Application(SQLAlchemyObjectType):
    class Meta:
        model = ApplicationModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_applications = SQLAlchemyConnectionField(Application)


schema = graphene.Schema(query=Query)
