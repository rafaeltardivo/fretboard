from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple

@dataclass
class Fret:
    """Guitar fret representation.
    
    Each fret holds an array with 6 positions (one for
    each string). Octave frets are shorter.
    """
    is_octave: False
    strings: List[int]

    def __init__(self, is_octave=False):
        self.strings = [0] * 6
        self.is_octave = is_octave

    def add_note(self, string:int, finger:int=0):
        """Add a note to the fretboard.
        
        The note is represented by a finger pressing a string
        string on this fret.
        """
        self.strings[string] = finger

    def get_note(self, string:str):
        """Get a note from the fret.
        
        If no note is found (no finger pressing the string), a
        dash is returned. Octave frets are shorter.
        """
        if self.is_octave:
            note = f"-{self.strings[string] or '-'}-|"
        else:
            note = f"--{self.strings[string] or '-'}--|"
        return note

class Neck:
    """Guitar neck representation."""

    def __init__(self, fret_count:int=21):
        self.frets = []
        self.strings = {
            "e": 0,
            "B": 1,
            "G": 2,
            "D": 3,
            "A": 4,
            "E": 5
        }
        self.fingers = {
            "thumb": 1,
            "index": 2,
            "middle": 3,
            "ring": 4,
            "pinky": 5
        }

        for item in range(fret_count):
            is_octave = item > 11
            self.frets.append(Fret(is_octave=is_octave))

    def add_chord(self, chord: List[Tuple]):
        """Ädd a chord to the fretboard.
        
        Chords are lists of tuples. Each tuple contains three
        items: fret, string and finger.

        strings and fingers are mapped out for better usability.
        """
  
        for note in chord:
            fret, string, finger = note
            self.frets[fret - 1].add_note(
                self.strings[string],
                self.fingers[finger],
            )

    def print_fretboard(self):
        """Print the fretboard. """
        for string in range(6):
            base = "|"
            for fret in self.frets:
                base += fret.get_note(string)
            print(base)

if __name__ == "__main__":
    n = Neck(21)
    n.add_chord([
        (1, "G", "index"),
        (2, "D", "ring"),
        (2, "A", "middle"),
    ])
    n.print_fretboard()