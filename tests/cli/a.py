import click

@click.group()
def a():
    pass


@click.command()
def v():
    print("v")


a.add_command(v)