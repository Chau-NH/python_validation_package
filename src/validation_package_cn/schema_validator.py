from .validation_exception import ValidationException
from .validator import Validator

class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema
        self.validator = Validator()

    def validate(self, data):
        errors = {}
        for field, rules in self.schema.items():
            value = data.get(field)
            try:
                for rule in rules.items():
                    self.validator.run_validation(rule, value)
                    
            except ValidationException as e:
                errors[field] = str(e)
        
        if errors:
            raise ValidationException(errors)
