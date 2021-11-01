import json
import os
import sys
from pathlib import Path

from jsonschema import Draft7Validator, ValidationError, validators
import yaml


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

for file_type in ("json", "yaml", "yml"):
    config = path / f"config.{file_type}"
    if config.exists():
        break

if not config.exists():
    print(f"::error ::Add-on configuration file not found in '{path}'")
    sys.exit(1)


with open(config) as fp:
    if config.suffix == "json":
        configuration = json.load(fp)
    else:
        configuration = yaml.load(fp, Loader=yaml.SafeLoader)

with open("/config.schema.json") as fp:
    schema = json.load(fp)

DefaultValidatingDraft7Validator = check_is_default(Draft7Validator)
v = DefaultValidatingDraft7Validator(schema)

exit_code = 0

for error in sorted(v.iter_errors(configuration), key=str):
    print(f"::error file={config}::{error.message}")
    exit_code = 1

if configuration.get("ingress", False):

    if configuration.get("webui"):
        print(f"::error file={config}::'webui' should be removed, Ingress is enabled.")
        exit_code = 1

    if (
        configuration.get("host_network", False)
        and configuration.get("ingress_port", 8099) != 0
    ):
        print(
            f"::error file={config}::'ingress_port' this add-on runs on the host network. "
            "Ingress port should be set to 0."
        )
        exit_code = 1

    if (
        not configuration.get("host_network", False)
        and configuration.get("ingress_port", 8099) == 0
    ):
        print(
            f"::error file={config}::'ingress_port' this does not run on the host network. "
            "In Ingress port doesn't have to be randomized (not 0)."
        )
        exit_code = 1

if "ports" in configuration and "ports_description" not in configuration:
    print(f"::error file={config}::'ports' is defined without 'ports_description'.")
    exit_code = 1

if set(configuration.get("ports", {})) != set(
    configuration.get("ports_description", {})
):
    print(f"::error file={config}::'ports' and 'ports_description' do not match.")
    exit_code = 1

if configuration.get("full_access") and any(
    item in ["devices", "gpio", "uart", "usb"] for item in configuration
):
    print(
        f"::error file={config}::'full_access', don't add 'devices', 'uart', 'usb' or 'gpio' this is not needed"
    )
    exit_code = 1

if configuration.get("full_access"):
    print(
        f"::warning file={config}::'full_access' consider using other options instead, like 'devices'"
    )

if "auto_uart" in configuration:
    print(f"::error file={config}::'auto_uart' is deprecated, use 'uart' instead.")
    exit_code = 1

if any(":" in line for line in configuration.get("devices", [])):
    print(
        f"::error file={config}::'devices' uses a deprecated format, the new format uses a list of paths only."
    )
    exit_code = 1

if not isinstance(configuration.get("tmpfs", False), bool):
    print(
        f"::error file={config}::'tmpfs' use a deprecated format, it is a boolean now."
    )
    exit_code = 1

if configuration.get("snapshot", "hot") == "cold":
    for option in ["snapshot_pre", "snapshot_post"]:
        if option in configuration:
            print(
                f"::error file={config}::'{option}' is not valid when using cold snapshots."
            )
            exit_code = 1

if configuration.get("backup", "hot") == "cold":
    for option in ["backup_pre", "backup_post"]:
        if option in configuration:
            print(
                f"::error file={config}::'{option}' is not valid when using cold backups."
            )
            exit_code = 1

if "snapshot" in configuration:
    print(f"::error file={config}::'snapshot' is deprecated, use 'backup' instead.")
    exit_code = 1

if "snapshot_exclude" in configuration:
    print(f"::error file={config}::'snapshot_exclude' is deprecated, use 'backup_exclude' instead.")
    exit_code = 1

if "snapshot_pre" in configuration:
    print(f"::error file={config}::'snapshot_pre' is deprecated, use 'backup_pre' instead.")
    exit_code = 1

if "snapshot_post" in configuration:
    print(f"::error file={config}::'snapshot_post' is deprecated, use 'backup_post' instead.")
    exit_code = 1

# Checks regarding build file(if found)
for file_type in ("json", "yaml", "yml"):
    build = path / f"build.{file_type}"
    if build.exists():
        break

if build.exists():
    with open(build) as fp:
        if build.suffix == "json":
            build_configuration = json.load(fp)
        else:
            build_configuration = yaml.load(fp, Loader=yaml.SafeLoader)

    with open("/build.schema.json") as fp:
        build_schema = json.load(fp)

    v = DefaultValidatingDraft7Validator(build_schema)

    for error in sorted(v.iter_errors(build_configuration), key=str):
        print(f"::error file={build}::{error.message}")
        exit_code = 1

# Start of additional community checks
if os.environ["INPUT_COMMUNITY"] != "true":
    sys.exit(exit_code)

if configuration["version"] != "dev":
    print(f"::error file={config}::Add-on version identifier must be 'dev'")
    exit_code = 1

if not build.exists():
    print(f"::error file={build}::The build.json file is missing")
    sys.exit(1)

if set(configuration["arch"]) != set(build_configuration["build_from"]):
    print(f"::error file={build}::Architectures in config and build do not match")
    exit_code = 1

# All good things, come to an end \o/!
sys.exit(exit_code)
