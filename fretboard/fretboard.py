from dataclasses import dataclass, field
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

    def add_note(self, string: int, finger: int = 0):
        """Adds a note to the fretboard.
        
        Args:
            string (int): The string index (0-5).
            finger (int, optional): The finger pressing the string. Defaults to 0.
        """
        self.strings[string] = finger

    def get_note(self, string: str):
        """Gets a note from the fret.
        
        Args:
            string (str): The string index.

        Returns:
            str: The note representation for this fret and string.
        """
        if self.is_octave:
            note = f"-{self.strings[string] or '-'}-|"
        else:
            note = f"--{self.strings[string] or '-'}--|"
        return note

class Neck:
    """Guitar neck representation."""

    def __init__(self, fret_count: int = 21):
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
        """Adds a chord to the fretboard.
        
        Chords are lists of tuples. Each tuple contains three
        items: fret, string and finger.

        Strings and fingers are mapped out for better usability.

        Args:
            chord (List[Tuple]): List of (fret, string, finger) tuples.
        """
        for note in chord:
            fret, string, finger = note
            self.frets[fret - 1].add_note(
                self.strings[string],
                self.fingers[finger],
            )

    def print_fretboard(self):
        """Prints the fretboard."""
        for string, key in enumerate(self.strings.keys()):
            base = f"{key} |"
            for fret in self.frets:
                base += fret.get_note(string)
            print(base)

if __name__ == "__main__":
    n = Neck()

    print("Enter chord notes as comma-separated tuples (fret,string,finger).")
    print("Example: 1,G,index,2,D,ring,2,A,middle")
    user_input = input("Chord notes: ")

    items = user_input.split(",")
    if len(items) % 3 != 0:
        print("Invalid input. Please enter sets of 3 values (fret,string,finger).")
    else:
        chord = []
        valid = True
        for i in range(0, len(items), 3):
            try:
                fret = int(items[i].strip())
            except ValueError:
                print(f"Invalid fret value: '{items[i].strip()}'. Fret must be an integer.")
                valid = False
                break

            string = items[i+1].strip()
            finger = items[i+2].strip()

            if not (1 <= fret <= len(n.frets)):
                print(f"Invalid fret: {fret}. Must be between 1 and {len(n.frets)}.")
                valid = False
                break
            if string not in n.strings:
                print(f"Invalid string: {string}. Must be one of {list(n.strings.keys())}.")
                valid = False
                break
            if finger not in n.fingers:
                print(f"Invalid finger: {finger}. Must be one of {list(n.fingers.keys())}.")
                valid = False
                break

            chord.append((fret, string, finger))

        if valid:
            n.add_chord(chord)
            n.print_fretboard()