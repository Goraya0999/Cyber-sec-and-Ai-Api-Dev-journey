from datetime import datetime
from typing import Optional

contacts_db: dict[int, dict] = {}
_counter = 0


def get_all(search: Optional[str] = None, skip: int = 0, limit: int = 10):
    results = list(contacts_db.values())
    if search:
        q = search.lower()
        results = [c for c in results if q in c["name"].lower() or q in (c.get("email") or "").lower()]
    return results[skip : skip + limit]


def get_by_id(contact_id: int):
    return contacts_db.get(contact_id)


def create(data: dict) -> dict:
    global _counter
    _counter += 1
    contact = {
        "id":         _counter,
        "created_at": datetime.utcnow().isoformat(),
        **data
    }
    contacts_db[_counter] = contact
    return contact


def update(contact_id: int, data: dict) -> Optional[dict]:
    if contact_id not in contacts_db:
        return None
    contacts_db[contact_id] = {**contacts_db[contact_id], **data}
    return contacts_db[contact_id]


def delete(contact_id: int) -> bool:
    if contact_id not in contacts_db:
        return False
    del contacts_db[contact_id]
    return True