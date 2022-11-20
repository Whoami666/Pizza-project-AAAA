{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Whoami666/Pizza-project-AAAA/blob/my_final_pizza/AAA_Pizza_Project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "опишите рецепты классами\n",
        "— пусть будет два размера: L и XL\n",
        "— метод dict() выводит рецепт в виде\n",
        "словаря"
      ],
      "metadata": {
        "id": "n30WuVlp-PfZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Margherita\n",
        "* tomato sauce\n",
        "* mozzarella\n",
        "* tomatoes\n",
        "\n",
        "Pepperoni\n",
        "* tomato sauce\n",
        "* mozzarella\n",
        "* pepperoni\n",
        "\n",
        "Hawaiian\n",
        "* tomato sauce\n",
        "* mozzarella\n",
        "* chicken\n",
        "* pineapples"
      ],
      "metadata": {
        "id": "yt21K7UI-TRe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import click\n",
        "\n",
        "\n",
        "class Pizza:\n",
        "    def __init__(self, name, ingredients, icon=\"🍕\", size=\"L\"):\n",
        "        self.name = name\n",
        "        self.ingredients = ingredients\n",
        "        self.icon = icon\n",
        "        self.size = size\n",
        "        if size == \"XL\":\n",
        "            self.cooking_time = len(ingredients) * 3\n",
        "        else:\n",
        "            self.cooking_time = len(ingredients) * 2\n",
        "\n",
        "    def beautifier(func):\n",
        "      def new_menu(self):\n",
        "        output = \"💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\\n\" + func(self) + \"💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\\n\"\n",
        "        return output\n",
        "      return new_menu\n",
        "\n",
        "    @beautifier\n",
        "    def menu(self):\n",
        "        beautiful_string = \"\"\n",
        "        for ingredient in self.ingredients:\n",
        "            beautiful_string += '🥄' + str(ingredient) + '\\n'\n",
        "\n",
        "        icon_printer = self.icon\n",
        "        if self.size == 'XL':\n",
        "            icon_printer += self.icon * 2\n",
        "        return f\"Pizza {self.name} {icon_printer}:\\n{beautiful_string}\"\n",
        "\n",
        "    def order(self):\n",
        "        return f\"Will cook {self.name} {icon_printer} in {cooking_time} minutes\\n\"\n",
        "\n",
        "\n",
        "\n",
        "@click.command()\n",
        "@click.argument('name', default='guest')\n",
        "def hello(name):\n",
        "    click.echo(f'Hello {name}')\n",
        "\n",
        "\n",
        "@click.command()\n",
        "def menu():\n",
        "    for pizza in pizzas:\n",
        "        click.echo(pizza.menu())\n",
        "\n",
        "\n",
        "@click.command()\n",
        "@click.argument('name')\n",
        "def order(name):\n",
        "    for pizza in pizzas:\n",
        "        if pizza.name == name:\n",
        "            click.echo(pizza.order)\n",
        "\n",
        "\n",
        "@click.argument('name')\n",
        "def hello(count, name):\n",
        "    for x in range(count):\n",
        "        click.echo(f\"Hello {name}!\")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "\n",
        "  pizzas = [Pizza(\"Margherita\", [\"tomatoes\", \"tomato sauce\", \"mozzarella\"], \"🍟\"),\n",
        "            Pizza(\"Pepperoni\", [\"tomato sauce\", \"pepperoni\", \"mozzarella\"], size=\"XL\"),\n",
        "            Pizza(\"Hawaiian\", [\"tomato sauce\", \"chicken\", \"mozzarella\", \"pineapples\"], \"🧀\")]\n",
        "\n",
        "\n",
        "  for pizza in pizzas:\n",
        "      print(pizza.menu())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "URNPBxM6IVHh",
        "outputId": "424533ee-91ae-486e-bcb4-f316647dd71d"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "Pizza Margherita 🍟:\n",
            "🥄tomatoes\n",
            "🥄tomato sauce\n",
            "🥄mozzarella\n",
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "\n",
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "Pizza Pepperoni 🍕🍕🍕:\n",
            "🥄tomato sauce\n",
            "🥄pepperoni\n",
            "🥄mozzarella\n",
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "\n",
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "Pizza Hawaiian 🧀:\n",
            "🥄tomato sauce\n",
            "🥄chicken\n",
            "🥄mozzarella\n",
            "🥄pineapples\n",
            "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "nQfnrXaBIVju"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}