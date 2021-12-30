class Item(object):
    name = ''
    value = 0
    volume = 0
    density = 0
 
    def __init__(self, value, volume, name):
        self.value = value
        self.volume = volume
        self.name = name
        self.density = value / volume
    
    def __str__(self):
        return self.name + ' ' + str(self.density)
    
    def __eq__(self, other):
        if self.density == other.density:
            return True
        return False
    
    def __lt__(self, other):
        if self.density < other.density:
            return True
        return False
    
    def __gt__(self, other):
        if self.density > other.density:
            return True
        return False
 
item1 = Item(2, 1, 'A')
item2 = Item(5, 2, 'B')
item3 = Item(6, 4, 'C')
item4 = Item(10, 5, 'D')
item5 = Item(13, 7, 'E')
item6 = Item(16, 8, 'F')
 
items = [item1, item2, item3, item4, item5, item6]
tmp_items = sorted(items, reverse=True)
bag = []
max_bag = 8
for item in tmp_items:
    if item.volume <= max_bag:
        bag.append(item)
        max_bag -= item.volume
        print(item)
