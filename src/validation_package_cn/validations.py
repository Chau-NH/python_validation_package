
from .validation_exception import ValidationException

def validate_type(value, expected_type):
    if  value is not None and not isinstance(value, expected_type):
        raise ValidationException(f"Expected type is {expected_type.__name__} but got {type(value).__name__}.")
    
def validate_min(value, min_value):
    if value is not None and value < min_value:
        raise ValidationException(f"Value {value} is less than minimum allowed {min_value}.")

def validate_max(value, max_value):
    if value is not None and value > max_value:
        raise ValidationException(f"Value {value} is greater than maximum allowed {max_value}.")
            
def validate_min_length(value, min_length):
    if value is not None and hasattr(value, "__len__") and len(value) < min_length:
        raise ValidationException(f"Length {len(value)} is less than minimum allowed {min_length}.")

def validate_max_length(value, max_length):
    if value is not None and hasattr(value, "__len__") and len(value) > max_length:
        raise ValidationException(f"Length {len(value)} is greater than maximum allowed {max_length}.")

def validate_in(value, choices):
    if value not in choices:
        raise ValidationException(f"Value {value} is not in allowed choices: {choices}.")

def validate_not_in(value, choices):
    if value in choices:
        raise ValidationException(f"Value {value} is in forbidden choices: {choices}.")
    
def validate_regex(value, pattern):
    import re
    if not re.match(pattern, value):
        raise ValidationException(f"Value {value} does not match pattern: {pattern}.")
    
def validate_required(value, required = True):
    if required and value is None:
        raise ValidationException(f"This field is required and can not be None")
    
def validate_file_extension(value, allowed_extensions=None):
    if value is not None:
        file_name = getattr(value, 'filename', getattr(value, 'name', None))
        if not file_name:
            raise ValidationException(f"Unable to determine the file name.")

        if allowed_extensions:
            if not any(file_name.lower().endswith(ext.lower()) for ext in allowed_extensions):
                raise ValidationException(f"Invalid file extension. Allowed extensions are: {', '.join(allowed_extensions)}")
    

    
# def validate_file(file_object, allowed_extensions=None, max_size=None):
#     if file_object is None:
#         raise ValidationException(f"No file uploaded.")
    
#     file_name = getattr(file_object, 'filename', getattr(file_object, 'name', None))
#     if not file_name:
#         raise ValidationException(f"Unable to determine the file name.")

#     if allowed_extensions:
#         if not any(file_name.lower().endswith(ext.lower()) for ext in allowed_extensions):
#             raise ValidationException(f"Invalid file extension. Allowed extensions are: {', '.join(allowed_extensions)}")

#     if max_size:
#         file_object.seek(0, 2)
#         file_size = file_object.tell()
#         file_object.seek(0)
#         if file_size > max_size:
#             raise ValidationException(
#                 f"File size exceeds the maximum limit of {max_size} bytes. Uploaded file size: {file_size} bytes."
#             )

def validate_datetime(value, format="%Y-%m-%d %H:%M:%S", before=None, before_or_equals=None, after=None, after_or_equals=None):
    from datetime import datetime
    try:
        date_value = datetime.strptime(value, format)
        if before and date_value >= datetime.strptime(before, format):
            raise ValidationException(f"Date {value} must be before {before}.")
        if before_or_equals and date_value > datetime.strptime(before_or_equals, format):
            raise ValidationException(f"Date {value} must be before or equals to {before_or_equals}.")
        if after and date_value <= datetime.strptime(after, format):
            raise ValidationException(f"Date {value} must be after {after}.")
        if after_or_equals and date_value < datetime.strptime(after_or_equals, format):
            raise ValidationException(f"Date {value} must be after or equals to {after_or_equals}.")

    except ValueError:
        raise ValidationException(f"Value {value} does not match the expected datetime format {format}.")
