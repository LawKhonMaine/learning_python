class ReataurantTable:

    menus = {
        'pizza': 5000,
        'cola': 1000,
        'apple jucie': 2000,
        'hamburgar': 2500,
        'fried chicken': 1500,
        'fried potato': 1000
    }

    def __init__(self):
        self.total = 0
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)
        self.total += self.menus[order]

    def printbill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}')

        print(f'Total price is {self.total} kyats.')


def startprogram():
    table = ReataurantTable()

    showMenus = input('Would you like to see menus? y/n :')
    if showMenus == 'y':
        for (key, value) in table.menus.items():
            print(f'{key} - {value} kyats')

    while True:

        order = input('write order exactly :')
        table.addOrder(order)

        another = input('order again ? y/n :')

        if another == 'y':
            continue
        if another == 'n':
            table.printbill()
            break


startprogram()
