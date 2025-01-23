from . import validations

class Validator:
    def run_validation(self, rule, value):
        method_name = f"validate_{rule[0]}"
        if hasattr(validations, method_name):
            rule_value = rule[1]
            method = getattr(validations, method_name)
            method(value, rule_value)
        else:
            raise AttributeError(f"Method {method_name} not found in validators module")
        