import strawberry


# Schema:


@strawberry.type
class Task:
    id_: int
    content: str
    is_done: bool = False
    number: int


# =============================

# Input Schema:


@strawberry.input
class UpdateTaskInput:
    content: str | None = None
    is_done: bool | None = None
    number: int | None = None


@strawberry.input
class PaginationInput:
    offset: int
    limit: int
