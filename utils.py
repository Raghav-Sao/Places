def validate_fields(field_names, params):
    return {key: params[key] for key in params if key in field_names}

def serialize(serializer_input):
    from django.db.models.query import QuerySet
    from django.db.models.base import ModelState
    import datetime
    if serializer_input.__class__ in [QuerySet, list, tuple]:
        result = []
        for each_object in serializer_input:
            result.append(serialize(each_object))
        return result
    elif '__dict__' in dir(serializer_input):
        return serialize(serializer_input.__dict__)
    elif serializer_input.__class__ in [ModelState]:
        return None
    elif isinstance(serializer_input, dict):
        result = {}
        for attr in serializer_input:
            if not attr.startswith('_'):
                result[attr] = serialize(serializer_input[attr])
        return result
    elif isinstance(serializer_input, datetime.datetime):
        return serializer_input.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(serializer_input, datetime.date):
        return serializer_input.strftime('%Y-%m-%d')
    else:
        return serializer_input