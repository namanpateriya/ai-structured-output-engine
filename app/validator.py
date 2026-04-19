def validate_output(output: dict, schema: dict):
    validated = {}

    for key, default in schema.items():
        value = output.get(key)

        if isinstance(default, list):
            if not isinstance(value, list):
                value = []
        elif isinstance(default, str):
            if not isinstance(value, str):
                value = ""
        elif isinstance(default, int):
            if not isinstance(value, int):
                value = default

        validated[key] = value if value is not None else default

    return validated
