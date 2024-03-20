"""Contains item router functions."""

from django.http import HttpRequest
from ninja import Router

from authentication.auth.api_key import ApiKey
from items.schemas.input import NewItem
from items.schemas.output import ItemSchema
from items.services import item_service

item_router = Router(tags=["Items"], auth=ApiKey())


@item_router.post("/create", response={201: ItemSchema})
async def create_item(request: HttpRequest, new_item: NewItem) -> ItemSchema:
    """
    Create a new item.

    Args:
        request (HttpRequest): The HTTP request.
        new_item (NewItem): The new item data.

    Returns:
        ItemSchema: The created item.
    """
    user = request.user
    store_id = new_item.store_id
    item_name = new_item.name
    item_price = new_item.price
    item_description = new_item.description
    item = await item_service.create_item(
        user=user,
        store_id=store_id,
        name=item_name,
        price=item_price,
        description=item_description,
    )
    return item