from ckan.plugins import toolkit

ignore_missing = toolkit.get_validator('ignore_missing')
list_of_strings = toolkit.get_validator('list_of_strings')
boolean_validator = toolkit.get_validator('boolean_validator')
empty = toolkit.get_validator('empty')
not_empty = toolkit.get_validator('not_empty')
isodate = toolkit.get_validator('isodate')
natural_number_validator = toolkit.get_validator('natural_number_validator')


def event_base_schema():
    schema = {
        'name': [not_empty, unicode],
        'url': [ignore_missing, unicode],
        'location': [ignore_missing, unicode],
        'date': [not_empty, isodate],
        'free': [not_empty, boolean_validator],
        'topic_tags': [ignore_missing, list_of_strings]
    }
    return schema


def event_create_schema():
    schema = event_base_schema()
    schema.update({
        'id': [empty]
    })
    return schema


def event_update_schema():
    schema = {
        'id': [not_empty, unicode],
        'name': [ignore_missing, unicode],
        'url': [ignore_missing, unicode],
        'location': [ignore_missing, unicode],
        'date': [ignore_missing, isodate],
        'free': [ignore_missing, boolean_validator],
        'topic_tags': [ignore_missing, list_of_strings]
    }
    return schema


def event_delete_schema():
    schema = {
        'id': [not_empty, unicode]
    }
    return schema


def event_show_schema():
    schema = {
        'id': [not_empty, unicode]
    }
    return schema


def event_list_schema():
    schema = {
        'limit': [ignore_missing, natural_number_validator],
        'offset': [ignore_missing, natural_number_validator]
    }
    return schema