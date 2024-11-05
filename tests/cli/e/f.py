import click

@click.command()
@click.argument("echo")
@click.option("--double", is_flag=True, default=False)
def f(echo, double):
    if double:
        print(echo)
    print(echo)