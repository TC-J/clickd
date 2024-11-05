import click

@click.command()
@click.argument("echo")
def j(echo):
    print(echo)