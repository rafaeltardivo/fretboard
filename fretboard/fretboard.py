from dataclasses import dataclass
from enum import Enum
from typing import List


class Finger(Enum):
    """Enum for fingers.

    0 means NONE, which means none of the fingers
    is touching that string.
    """
    THUMB = 1
    INDEX = 2
    MIDDLE = 3
    RING = 4
    PINKY = 5


@dataclass
class Fret:
    """Guitar fret representation.
    
    Each fret will hold an array with 6 positions (one for
    each string). Octave frets are shorter.
    """

    is_octave: False
    strings: List[Finger]

    def __init__(self, is_octave=False):
        self.strings = [None] * 6
        self.is_octave = is_octave

    def set_note(self, string:int, finger:Finger=None):
        self.strings[string] = finger

    def get_note(self, string):
        if self.is_octave:
            return f"-{self.strings[string] or '-'}-|"
        return f"--{self.strings[string] or '-'}--|"

class Neck:
    """Guitar neck text generator."""

    def __init__(self, fret_count:int=21):
        self.frets = []

        for item in range(fret_count):
            is_octave = item > 11
            self.frets.append(Fret(is_octave=is_octave))

    def print_fretboard(self):
        for string in range(6):
            base = "|"
            for fret in self.frets:
                base += fret.get_note(string)
            print(base)

if __name__ == "__main__":
    n = Neck(21)
    n.print_fretboard()