import graphene
import resolvers


class Info(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    description = graphene.String()


class Sentence(graphene.ObjectType):
    id = graphene.ID(required=True)
    text = graphene.String(required=True)


class Query(graphene.ObjectType):
    info = graphene.Field(Info)
    sentence = graphene.Field(Sentence)
    all_sentences = graphene.Field(graphene.List(Sentence))

    def resolve_info(self, _):
        return resolvers.info()

    async def resolve_sentence(self, input):
        return await resolvers.sentence(input)

    async def resolve_all_sentences(self, _):
        return await resolvers.all_sentences()


class AddSentenceInput(graphene.InputObjectType):
    id = graphene.ID()
    text = graphene.String(required=True)


class AddSentence(graphene.Mutation):

    class Arguments:
        input = AddSentenceInput(required=True)

    Output = Sentence

    async def mutate(self, _, input):
        return await resolvers.add_sentence(input)


class Mutation(graphene.ObjectType):
    add_sentence = AddSentence.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
