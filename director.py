from cakebuilder import CakeBuilder


class Director:
    #  let's say director is only giving 6 ingredients
    flour = 100  # grams
    salt = 5  # teaspoon
    milk = 2  # litres
    cream = 100  # half a cup
    eggs = 2  # no of eggs
    sweetener = 2  # teaspoon
    cake = (
        CakeBuilder()
        .add_flour(flour)
        .add_salt(salt)
        .add_milk(milk)
        .add_cream(cream)
        .add_eggs(eggs)
        .add_sweetener(sweetener)
        .make_a_cake()
    )
