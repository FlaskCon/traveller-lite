import click
from flask import current_app as app
from sqlalchemy import text

from app.extensions import db


def parse_bool(value):
    if value == "true" or value == "True":
        return True
    if value == "false" or value == "False":
        return False

    raise click.BadParameter(
        "You have set the column-type to bool, but the "
        "default value cannot be parsed to bool."
        "Please use 'true' or 'false'."
    )


def parse_int(value):
    try:
        _value = int(value)
    except ValueError:
        raise click.BadParameter(
            "You have set the column-type to int, but the "
            "default value cannot be parsed to int."
        )


@app.cli.command("alter-table-add-column")
@click.option("--table", required=True, type=str, help="The table to alter.")
@click.option("--column", required=True, type=str, help="The column to add.")
@click.option("--column-type", required=True, type=str, help="The type of the column.")
@click.option("--default", required=False, type=str, help="The default value of the column.")
def dev_seed_test_data(table, column, column_type, default):
    print(f"Altering table {table}...")
    print(f"Adding column {column}...")
    print(f"Type: {column_type}")

    raw_query = f"alter table {table} add {column} {column_type}"

    if default:
        if column_type == "int" or column_type == "integer":
            _default = parse_int(default)
        if column_type == "boolean" or column_type == "bool":
            _default = parse_bool(default)
        else:
            # Defaults to string.
            _default = default

        raw_query += f" default {_default}"

    raw_query += ";"

    db.session.execute(text(raw_query))

    print("Done.")
