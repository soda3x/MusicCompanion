from sys import int_info
from midiutil import MIDIFile
import MidiHelper


def generate_midi_file(key: str, scale: str, octave: int, bpm: int, bars:int):
    degrees = MidiHelper.get_scale(key=key, scale=scale, octave=octave)
    track = 0
    channel = 0
    duration = bars * 4  # In beats, currently only 4/4 timing
    time = 0   # In beats, where on timeline to add note
    tempo = bpm  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    midi = MIDIFile(1)  # create MIDI file with 1 track

    midi.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        midi.addNote(track, channel, pitch, time + i, duration, volume)
    
    with open("output.mid", "wb") as output_file:
        midi.writeFile(output_file)

generate_midi_file("cs", "major", 3, 120, 1)

def generate_progression(key:str, scale:str, octave:int, bpm: int, note_length, output_file:str):
    degrees = MidiHelper.get_chords_in_scale(key=key, scale=scale, octave=octave)
    track = 0
    channel = 0
    duration = note_length  # In beats, currently only 4/4 timing
    time = 0   # In beats, where on timeline to add note
    tempo = bpm  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    midi = MIDIFile(1)

    midi.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        for note in degrees[i]:
            midi.addNote(track, channel, note, time + i, duration, volume)

    with open(output_file, "wb") as output_file:
        midi.writeFile(output_file)

generate_progression("c", "minor", 2, 120, note_length=0.5, output_file="progression_minor.mid")
