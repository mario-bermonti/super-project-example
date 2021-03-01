"""Console script for super-project-example."""
import click

from super_project_example import __version__
from super_project_example.super_project_example import hello_fun


@click.command()
@click.version_option(version=__version__)
def main() -> int:
    """Console script for super-project-example."""
    click.echo("Replace this message by putting your code into super_project_example.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    hello_fun(1)
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
