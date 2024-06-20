from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:
    @staticmethod
    def _base_speed():
        return 12.0


class EuropeanParrot(Parrot):

    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def _load_factor(self):
        return 9.0

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage, nailed):
        self._voltage = voltage
        self._nailed = nailed

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."


def parrot_factory(parrot_type, number_of_coconuts=0, voltage=0, nailed=False):
    match parrot_type:
        case ParrotType.EUROPEAN:
            return EuropeanParrot()
        case ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(voltage, nailed)

    raise ValueError(f"Invalid parrot type: {parrot_type}")
