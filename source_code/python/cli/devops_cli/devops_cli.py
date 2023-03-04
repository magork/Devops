import click
import psutil

@click.group()
def cli():  
    """Simple command line tool to extract system information."""

@cli.command('cpu', short_help='Show CPU')
def cpu():
    """Shows CPU Resources."""
    click.echo(psutil.cpu_times())

@cli.command('disk', short_help='Show Disk')
def disk():
    """Shows Disk Status."""
    click.echo(psutil.disk_partitions())