# Fretboard

A simple Python module to represent and visualize a guitar fretboard in the terminal.  
You can input chord shapes interactively, and the program will render the fretboard with your chosen notes and fingers.

## Usage

Run the script:

```sh
python fretboard.py
```

You will be prompted to enter chord notes as comma-separated tuples in the format `(fret,string,finger)`.

### Example

To display an E major chord, enter:

```
1,G,index,2,D,ring,2,A,middle
```

**Output:**

```
e |--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
B |--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
G |--1--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
D |--0--|--2--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
A |--0--|--0--|--2--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
E |--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|--0--|
```

## Notes

- Valid string names: `e`, `B`, `G`, `D`, `A`, `E`
- Valid finger names: `thumb`, `index`, `middle`, `ring`, `pinky`
- Frets are numbered from 1 (nut) up to 21 by default.
