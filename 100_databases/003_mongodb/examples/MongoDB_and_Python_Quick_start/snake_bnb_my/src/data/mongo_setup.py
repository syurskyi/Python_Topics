import mongoengine


def global_intit():
    mongoengine.register_connection(alias='core', name='snake_bnb')