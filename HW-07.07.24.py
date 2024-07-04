class TemperatureCelsius:
    def __init__(self, value):
        if value < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        self.value = value

    def __add__(self, other):
        if isinstance(other, TemperatureCelsius):
            return TemperatureCelsius(self.value + other.value)
        elif isinstance(other, (int, float)):
            return TemperatureCelsius(self.value + other)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, TemperatureCelsius):
            return TemperatureCelsius(self.value - other.value)
        elif isinstance(other, (int, float)):
            return TemperatureCelsius(self.value - other)
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other):
        if isinstance(other, TemperatureCelsius):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        else:
            raise TypeError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, TemperatureCelsius):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        else:
            raise TypeError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, TemperatureCelsius):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return f"{self.value}°C"

    def __float__(self):
        return self.value

class TemperatureFahrenheit:
    def __init__(self, value):
        if value < -459.67:
            raise ValueError("Температура ниже абсолютного нуля")
        self.value = value

    def __add__(self, other):
        if isinstance(other, TemperatureFahrenheit):
            return TemperatureFahrenheit(self.value + other.value)
        elif isinstance(other, (int, float)):
            return TemperatureFahrenheit(self.value + other)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, TemperatureFahrenheit):
            return TemperatureFahrenheit(self.value - other.value)
        elif isinstance(other, (int, float)):
            return TemperatureFahrenheit(self.value - other)
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other):
        if isinstance(other, TemperatureFahrenheit):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        else:
            raise TypeError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, TemperatureFahrenheit):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        else:
            raise TypeError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, TemperatureFahrenheit):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return f"{self.value}°F"

    def __float__(self):
        return self.value

class TemperatureKelvin:

    def __init__(self, value):
        if value < 0:
            raise ValueError("Температура ниже абсолютного нуля")
        self.value = value

    def __add__(self, other):
        if isinstance(other, TemperatureKelvin):
            return TemperatureKelvin(self.value + other.value)
        elif isinstance(other, (int, float)):
            return TemperatureKelvin(self.value + other)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, TemperatureKelvin):
            return TemperatureKelvin(self.value - other.value)
        elif isinstance(other, (int, float)):
            return TemperatureKelvin(self.value - other)
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other):
        if isinstance(other, TemperatureKelvin):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        else:
            raise TypeError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, TemperatureKelvin):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        else:
            raise TypeError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, TemperatureKelvin):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return f"{self.value}K"

    def __float__(self):
        return self.value

celsius = TemperatureCelsius(30)
fahrenheit = TemperatureFahrenheit((celsius.value * 9 / 5) + 32)
kelvin = TemperatureKelvin(celsius.value + 273.15)

print(celsius)
print(fahrenheit)
print(kelvin)
