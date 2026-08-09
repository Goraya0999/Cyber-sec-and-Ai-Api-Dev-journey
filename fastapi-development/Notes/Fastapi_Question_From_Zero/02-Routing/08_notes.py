# ==========================================================
# FASTAPI NOTES — #025 & #026 (Professional Edition)
# ==========================================================

from fastapi import FastAPI, Response
from typing import List

app = FastAPI()


# ==========================================================
# #025 DELETE Route with No Response Body
# ==========================================================
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """
    PURPOSE:
        Handle deletion of a resource identified by `item_id`.

    BEHAVIOR:
        - Executes delete operation on the backend (DB, cache, etc.)
        - Returns HTTP 204 (No Content)

    WHY 204?
        - Indicates the request was successfully processed
        - No response body should be returned (as per HTTP standards)
        - Preferred for DELETE operations to reduce payload size

    BEST PRACTICES:
        - Ensure idempotency (multiple deletes should not break)
        - Validate existence before deletion (optional: raise 404)
        - Avoid returning unnecessary data

    RETURNS:
        Response:
            Empty response with status code 204
    """

    # Example (pseudo logic):
    # if not db_item_exists(item_id):
    #     raise HTTPException(status_code=404, detail="Item not found")
    # delete_item_from_db(item_id)

    return Response(status_code=204)


# ==========================================================
# #026 response_description in Route Decorator
# ==========================================================
@app.get(
    "/items",
    response_model=List[dict],
    response_description="A structured list of all available items",
    status_code=200
)
def get_items():
    """
    PURPOSE:
        Retrieve a collection of items.

    response_description:
        - Adds a human-readable explanation of the response
        - Displayed in Swagger UI (/docs) and OpenAPI schema
        - Improves API usability and developer experience

    WHY IMPORTANT?
        - Helps frontend/backend teams understand API quickly
        - Acts as lightweight documentation
        - Useful for public APIs and team collaboration

    BEST PRACTICES:
        - Keep descriptions concise but meaningful
        - Combine with `response_model` for strict schema validation
        - Use clear terminology aligned with business logic

    RETURNS:
        List[dict]:
            A list of item objects (example structure shown below)
    """

    return [
        {"id": 1, "name": "Item One"},
        {"id": 2, "name": "Item Two"}
    ]


# ==========================================================
