# Octave Mapping Dictionary
octave_mapping = {
    -2: 0,
    -1: 12,
    0: 24,
    1: 36,
    2: 48,
    3: 60,
    4: 72,
    5: 84,
    6: 96,
    7: 108,
    8: 120
}

# Note Offset Mapping Dictionary
note_offset_mapping = {
    "c": 0,
    "cs": 1,
    "db": 1,
    "d": 2,
    "ds": 3,
    "eb": 3,
    "e": 4,
    "f": 5,
    "fs": 6,
    "gb": 6,
    "g": 7,
    "gs": 8,
    "ab": 8,
    "a": 9,
    "as": 10,
    "bb": 10,
    "b": 11
}

scale_mapping = {
    "major": [0, 2, 4, 5, 7, 9, 11, 12],
    "minor": [0, 2, 3, 5, 7, 8, 10, 12],
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11, 12]
}

midi_note_mapping = {
    0: "c",
    1: "cs",
    2: "d",
    3: "ds",
    4: "e",
    5: "f",
    6: "fs",
    7: "g",
    8: "gs",
    9: "a",
    10: "as",
    11: "b"
}

def get_midi_note_number(note:str, octave:int):
    """Get MIDI Note Number of Note in Octave

    Parameters
    ------------
    note : str
        note as string eg: "c" would be C, "cs" would be C#, and "eb" would be Eb
    octave : int 
        octave as integer from -2 to 8
    
    Note
    ------------
    Returns -1 if Note + Octave cannot be mapped to MIDI"""

    octave_val = octave_mapping.get(octave, -1)
    note_val = note_offset_mapping.get(note, -1)

    midi_note = octave_val + note_val

    # if either octave or note are invalid, return -1
    if octave_val == -1 or note_val == -1:
        return -1

    # last midi note is 127, if greater than 127, return -1
    if midi_note > 127:
        return -1
    else:
        return midi_note

def get_scale(key:str, scale:str, octave:int):
    """Get scale as midi notes in a specified key

    Parameters
    ------------
    key : str
        Root note of scale
    scale : str 
        Desired scale
    octave : int
        Octave ranging from -2 to 8
    home : bool
        Add root note of the next octave to end of scale

    Note
    ------------
    Returns -1 if scale cannot be mapped to MIDI"""

    bad_conversion = [-1, -1, -1, -1, -1, -1, -1]

    octave_val = octave_mapping.get(octave, -1)
    if octave_val == -1:
        return bad_conversion

    scale_val = scale_mapping.get(scale, -1)
    if scale_val == -1:
        return bad_conversion

    root_offset = note_offset_mapping.get(key, -1)
    if root_offset == -1:
        return bad_conversion

    converted_scale = []
    for note in scale_val:
        converted_note = note + (root_offset + octave_val)
        if (converted_note > 127):
            return bad_conversion
        else:
            converted_scale.append(converted_note)

    return converted_scale

def get_octaved_note(note:int, octave:int):
    return note + (octave * 12)

def get_chords_in_scale(key:str, scale:str, octave:int):
    chords = []
    scale_val = get_scale(key=key, scale=scale, octave=octave)
    scale_val.pop

    if (scale == "major"):
        chords.append([scale_val[0], scale_val[2], scale_val[4]])
        chords.append([scale_val[1], scale_val[3], scale_val[5]])
        chords.append([scale_val[2], scale_val[4], scale_val[6]])
        chords.append([scale_val[3], scale_val[5], scale_val[7]])
        chords.append([scale_val[4], scale_val[6], get_octaved_note(scale_val[1], 1)])
        chords.append([scale_val[5], scale_val[7], get_octaved_note(scale_val[2], 1)])
        chords.append([scale_val[6], get_octaved_note(scale_val[1], 1), get_octaved_note(scale_val[3], 1)])
        chords.append([scale_val[7], get_octaved_note(scale_val[2], 1), get_octaved_note(scale_val[4], 1)])
    
    if (scale == "minor"):
        chords.append([scale_val[0], scale_val[2], scale_val[4]])
        chords.append([scale_val[1], scale_val[3], scale_val[5]])
        chords.append([scale_val[2], scale_val[4], scale_val[6]])
        chords.append([scale_val[3], scale_val[5], scale_val[7]])
        chords.append([scale_val[4], scale_val[6], get_octaved_note(scale_val[1], 1)])
        chords.append([scale_val[5], scale_val[7], get_octaved_note(scale_val[2], 1)])
        chords.append([scale_val[6], get_octaved_note(scale_val[1], 1), get_octaved_note(scale_val[3], 1)])
        chords.append([scale_val[7], get_octaved_note(scale_val[2], 1), get_octaved_note(scale_val[4], 1)])

    if (scale == "harmonic_minor"):
        chords.append([scale_val[0], scale_val[2], scale_val[4]])
        chords.append([scale_val[1], scale_val[3], scale_val[5]])
        chords.append([scale_val[2], scale_val[4], scale_val[6]])
        chords.append([scale_val[3], scale_val[5], scale_val[7]])
        chords.append([scale_val[4], scale_val[6], get_octaved_note(scale_val[1], 1)])
        chords.append([scale_val[5], scale_val[7], get_octaved_note(scale_val[2], 1)])
        chords.append([scale_val[6], get_octaved_note(scale_val[1], 1), get_octaved_note(scale_val[3], 1)])
        chords.append([scale_val[7], get_octaved_note(scale_val[2], 1), get_octaved_note(scale_val[4], 1)])
    return chords
