import json
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, ValidationError, validators


def check_is_default(validator_class):
    """Check if a JSON property is using its default value."""
    validate_properties = validator_class.VALIDATORS["properties"]

    def is_default(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                if instance.get(property) == subschema["default"]:
                    yield ValidationError(
                        f"'{property}' should be removed, it uses a default value"
                    )

        for error in validate_properties(
            validator,
            properties,
            instance,
            schema,
        ):
            yield error

    return validators.extend(
        validator_class,
        {"properties": is_default},
    )


path = Path(os.environ["INPUT_PATH"])
if not path.exists():
    print(f"::error ::Add-on configuration path not found: {path}")
    sys.exit(1)

config = path / "config.json"
if not config.exists():
    print(f"::error ::Add-on configuration file not found: {config}")
    sys.exit(1)

with open(config) as fp:
    configuration = json.load(fp)

with open("/config.schema.json") as fp:
    schema = json.load(fp)

DefaultValidatingDraft7Validator = check_is_default(Draft7Validator)
v = DefaultValidatingDraft7Validator(schema)

for error in sorted(v.iter_errors(configuration), key=str):
    print(f"::error file={config}::{error.message}")

if os.environ["INPUT_COMMUNITY"] != "true":
    sys.exit()

if configuration["version"] != "dev":
    print(f"::error file={config}::Add-on version identifier must be 'dev'")
