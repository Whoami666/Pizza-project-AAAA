import click


class Pizza:
    def __init__(self, name, ingredients, icon="🍕", size="L"):
        self.name = name
        self.ingredients = ingredients
        self.icon = icon
        self.size = size
        self.icon_printer = icon
        if size == "XL":
            self.cooking_time = len(ingredients) * 3
        else:
            self.cooking_time = len(ingredients) * 2

    def beautifier(func):
        def new_menu(self):
            output = "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n" + func(self) + "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n"
            return output

        return new_menu

    @beautifier
    def menu(self):
        """
        >>> menu(Pizza("Margherita", ["tomatoes", "tomato sauce", "mozzarella"], "🍟"))
        💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫
        Pizza Margherita 🍟:
        🥄tomatoes
        🥄tomato sauce
        🥄mozzarella
        💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫
        """

        beautiful_string = ""
        for ingredient in self.ingredients:
            beautiful_string += '🥄' + str(ingredient) + '\n'

        self.icon_printer = self.icon
        if self.size == 'XL':
            self.icon_printer += self.icon * 2
        return f"Pizza {self.name} {self.icon_printer}:\n{beautiful_string}"

    def order(self):
        return f"Will cook {self.name} {self.icon_printer} in {self.cooking_time} minutes\n"


@click.command()
@click.argument('name', default='guest')
def hello(name):
    click.echo(f'Hello {name}')


@click.command()
def menu():
    for pizza in pizzas:
        click.echo(pizza.menu())


@click.command()
@click.argument('name')
def order(name):
    for pizza in pizzas:
        if pizza.name == name:
            click.echo(pizza.order)


@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    pizzas = [Pizza("Margherita", ["tomatoes", "tomato sauce", "mozzarella"], "🍟"),
              Pizza("Pepperoni", ["tomato sauce", "pepperoni", "mozzarella"], size="XL"),
              Pizza("Hawaiian", ["tomato sauce", "chicken", "mozzarella", "pineapples"], "🧀")]

    for pizza in pizzas:
        print(pizza.menu())
