import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click
from src.ingest import ingest_data
from src.query import query_data
from src.visualize import visualize_data

@click.group()
def cli():
    """ELD - Extremely Large Data handling tool"""
    pass

@cli.command()
@click.argument('filename')
def ingest(filename):
    """Ingest data from a file."""
    ingest_data(filename)

@cli.command()
@click.argument('filename')
@click.argument('condition')
def query(filename, condition):
    """Query data with a simple condition."""
    query_data(filename, condition)

@cli.command()
@click.argument('fields', nargs=-1)
@click.argument('filename')
@click.option('--chart', default='bar', help='Type of chart to use for visualization')
def visualize(fields, filename, chart):
    """Visualize data from specified fields."""
    visualize_data(fields, filename, chart)

if __name__ == '__main__':
    cli()