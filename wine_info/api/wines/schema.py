from wine_info.extensions import schemas


class VarietySchema(schemas.Schema):
    name = schemas.String()
    type = schemas.String()


class ClassificationSchema(schemas.Schema):
    name = schemas.String()
    type = schemas.String()


class WineSchema(schemas.Schema):
    id = schemas.Integer()
    name = schemas.String()
    brand = schemas.String()
    variety = schemas.Nested(VarietySchema)
    classification = schemas.Nested(ClassificationSchema)
