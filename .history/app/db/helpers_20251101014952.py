from sqlalchemy.orm import Query
from app.db.base import SoftDeleteMixin

def not_deleted(query: Query, model_class):
    if hasattr(model_class, 'deleted'):
        return query.filter(model_class.is_deleted.is_(False))
    return query