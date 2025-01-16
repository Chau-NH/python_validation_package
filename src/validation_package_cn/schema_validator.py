from .exceptions import ValidationError
from .validator import Validator

class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        errors = {}

        for field, rules in self.schema.items():
            value = data.get(field)
            try:
                if rules.get("required", False):
                    Validator.validate_required(field, value)
                if "type" in rules:
                    Validator.validate_type(field, value, rules["type"])
                if "range" in rules:
                    Validator.validate_range(field, value, *rules["range"])
                if "length" in rules:
                    Validator.validate_length(field, value, *rules["length"])
                if "choices" in rules:
                    Validator.validate_choices(field, value, rules["choices"])
                if "pattern" in rules:
                    Validator.validate_pattern(field, value, rules["pattern"])

            except ValidationError as e:
                errors[field] = str(e)
        
        if errors:
            raise ValidationError(errors)
