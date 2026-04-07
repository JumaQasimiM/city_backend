from rest_framework import serializers
# validation the name of the model
def validate_name(value):
   
    pass

# validation the lenght of a field
def min_len_validator(min_length):
    def validator(value):
        # remove white space
        value = value.strip() 
        if value < min_length:
            raise serializers.ValidationError(f'must be at least {min_length} characters.')
        return value
    return validator

# validation the duplicate of a field
def unique_validator(model, field):
    pass
