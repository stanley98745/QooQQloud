from fastapi import HTTPException
from sqlalchemy.orm import Session

def validate_id(model, id_value: int, db: Session, id_field: str = "id") -> object:
    """
    Validate that an entity with the given ID exists in the specified model.

    :param model: The SQLAlchemy model to query.
    :param id_value: The ID value to check.
    :param db: The database session.
    :param id_field: The field name for the ID (default: "id").
    :return: The instance if found, raises HTTPException otherwise.
    """
    if not id_value or not isinstance(id_value, int):
        raise HTTPException(status_code=400, detail=f"Invalid or missing {model.__name__} ID")

    query_filter = {id_field: id_value}
    instance = db.query(model).filter_by(**query_filter).first()
    if not instance:
        raise HTTPException(status_code=404, detail=f"{model.__name__} with {id_field} '{id_value}' not found")

    return instance

def validate_field_exists(model, field_name: str, field_value, db: Session, raise_error: bool = True) -> bool:
    """
    Validate that an entity with the specified field exists in the specified model.

    :param model: The SQLAlchemy model to query.
    :param field_name: The name of the field to check.
    :param field_value: The value of the field to match.
    :param db: The database session.
    :param raise_error: Whether to raise an exception if the field value does not exist.
    :return: True if the field exists, otherwise False.
    """
    query_filter = {field_name: field_value}
    instance = db.query(model).filter_by(**query_filter).first()

    if not instance:
        if raise_error:
            raise HTTPException(
                status_code=404,
                detail=f"{model.__name__} with {field_name}='{field_value}' not found"
            )
        return False

    return True
