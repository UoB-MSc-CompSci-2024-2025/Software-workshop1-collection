class ElectronicDevice:
    def __init__(self, voltage, weight, height, color):
        self.voltage = voltage
        self.weight = weight
        self.height = height
        self.color = color


class Computer(ElectronicDevice):
    def __init__(self, voltage, weight, height, color, ram, rom, processor):
        self.ram = ram
        self.rom = rom
        self.processor = processor
        super().__init__(voltage, weight, height, color)



class Desktop(Computer):
    def __init__(self, voltage, weight, height, color, ram, rom, processor, display):
        self.display = display
        super().__init__(voltage, weight, height, color, ram, rom, processor)



class Laptop(Computer):
    def __init__(self, voltage, weight, height, color, ram, rom, processor, display_with_touch):
        self.display_with_touch = display_with_touch
        super().__init__(voltage, weight, height, color, ram, rom, processor)

