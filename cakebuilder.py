from cake import Cake


class CakeBuilder:
    flour = None
    sweetener = None
    fats = None
    eggs = None
    salt = None
    milk = None
    cream = None
    chocolate = None
    coko_powder = None

    def add_salt(self, salt):
        self.salt = salt
        return self

    def add_flour(self, flour):
        self.flour = flour
        return self

    def add_fats(self, fats):
        self.fats = fats
        return self

    def add_eggs(self, eggs):
        self.eggs = eggs
        return self

    def add_coko_powder(self, coko_powder):
        self.coko_powder = coko_powder
        return self

    def add_chocolate(self, chocolate):
        self.chocolate = chocolate
        return self

    def add_cream(self, cream):
        self.cream = cream
        return self

    def add_milk(self, milk):
        self.milk = milk
        return self

    def add_sweetener(self, sweetener):
        self.sweetener = sweetener
        return self

    def make_a_cake(self):
        if self.flour or self.salt or self.milk or self.cream or self.eggs:
            cake = Cake()
            cake.flour = self.flour
            cake.sweetener = self.sweetener
            cake.fats = self.fats
            cake.eggs = self.eggs
            cake.salt = self.salt
            cake.milk = self.milk
            cake.cream = self.cream
            cake.chocolate = self.chocolate
            cake.coko_powder = self.coko_powder
            return cake
        else:
            raise RuntimeError("All required properties are not present.")

