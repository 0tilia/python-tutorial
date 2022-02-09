# putem da copy paste la ce s-a scris inainte sau inherite the functions

#inheritance!! + daca sunt elemente identice, overwrite it

from Chef import Chef
class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")
