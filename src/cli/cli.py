import click
import sys
import os

# This block ensures that the script can be run both as a module and standalone
if __package__ is None or __package__ == '':
    # Direct execution, not part of a package
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ingest.ingest import ingest_data
    from query.query import detect_encoding_and_query
    from visualize.visualize import visualize_data
else:
    # Part of a package (when run with -m)
    from ..ingest.ingest import ingest_data
    from ..query.query import detect_encoding_and_query
    from ..visualize.visualize import visualize_data

@click.group(help="ELD - Extremely Large Data handling tool for managing, querying, and visualizing large datasets.")
@click.version_option(version='0.1.0', help="Show the version of ELD.")
def cli():
    """Manage, query, and visualize extremely large datasets."""
    pass

@cli.command(help="Ingest data from a file into the system.")
@click.argument('filename', type=click.Path(exists=True))
def ingest(filename):
    """Ingest data from a file. Supports CSV and JSON formats."""
    ingest_data(filename)

@cli.command(help="Query data with a simple condition.")
@click.argument('filename', type=click.Path(exists=True))
@click.argument('condition')
def query(filename, condition):
    """Query data based on specified conditions. 

    Examples:
    - eld query sample.csv "Age > 30"
    - eld query data.json "Salary <= 50000"
    """
    return detect_encoding_and_query(filename, condition)

@cli.command(help="Visualize data from specified fields.")
@click.argument('fields', nargs=-1)
@click.argument('filename', type=click.Path(exists=True))
@click.option('--chart', default='bar', type=click.Choice(['bar', 'line', 'scatter'], case_sensitive=False),
              help="Type of chart to use for visualization. Defaults to 'bar'.")
def visualize(fields, filename, chart):
    """Visualize data fields from a dataset. 

    Examples:
    - eld visualize Age Salary sample.csv --chart bar
    - eld visualize Revenue data.json --chart line
    """
    visualize_data(fields, filename, chart)

if __name__ == '__main__':
    cli()