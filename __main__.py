import click


from _idea._idea import _idea

@click.group()
@click.pass_context
def main(ctx):
    pass


if __name__ == '__main__':
    main()
