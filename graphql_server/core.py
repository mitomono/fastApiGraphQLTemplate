import strawberry
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from strawberry.fastapi import GraphQLRouter

from core.model.managers.resolvers import QueryResolver, MutationResolver
from core.schemas.schemas import Task


@strawberry.type
class Query:
    tasks: list[Task] = strawberry.field(QueryResolver.get_tasks)
    task: (Task | None) = strawberry.field(resolver=QueryResolver.get_task)
    numbers: int = strawberry.field(resolver=QueryResolver.get_numbers)


@strawberry.type
class Mutation:
    add_task: Task = strawberry.field(resolver=MutationResolver.add_task)
    update_task: (Task | None) = strawberry.field(resolver=MutationResolver.update_task)
    delete_task = strawberry.field(resolver=MutationResolver.delete_task)


api_router = APIRouter()

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, path="/graphql")

api_router.include_router(graphql_app)


@api_router.get("/", include_in_schema=False)
async def base():
    return RedirectResponse(url="/docs")
