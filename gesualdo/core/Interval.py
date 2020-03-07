"""
Intervals
"""

from gesualdo.core.Note import Note

class Interval:

  # as they appear in a major scale
  named_intervals = {
    'unison': 0,
    'second': 2,
    'third': 4,
    'fourth': 5,
    'fifth': 7,
    'sixth': 9,
    'seventh': 11,
    'octave': 12,
    'ninth': 14,
    'tritave': 19
  }

  modifiers = {
    'major': 0,
    'minor': -1,
    'diminished': -2,
    'doubly diminished': -3,
    'augmented': 1,
    'doubly augmented': 2
  }

  note_names_as_numbers = {'C': 0, 'D': 1, 'E': 2, 'F': 3, 'G': 4, 'A': 5, 'B': 6}

  @classmethod
  def new_by_name(self, name='perfect fifth', starting_pitch='C', direction='up'):
    split_name = name.split()
    if len(split_name)==1:
      size = self.named_intervals(name)
    elif len(split_name)==2:
      size = self.named_intervals(split_name[0]) + self.modifiers[split_name[1]]
    else:
      raise ValueError('Interval not found. Check spelling: {}'.format(name))

    return Interval(size, starting_pitch)

  @classmethod
  def new_from_size(self, size=7): # this won't return any diminished or augmented intervals
    pass

  def __init__(self, starting_pitch='C4', ending_pitch='G4'):
    # check starting pitch and make it a note
    if isinstance(starting_pitch, str):
      starting_pitch = Note(starting_pitch)
    elif isinstance(starting_pitch, int):
      starting_pitch = Note.new_from_number(starting_pitch)
    elif not isinstance(starting_pitch, Note):
      raise Exception('Pitch is neither a viable string, integer, or Note!')


    # check ending_pitch and make it a note
    if isinstance(ending_pitch, str):
      ending_pitch = Note(ending_pitch)
    elif isinstance(ending_pitch, int):
      ending_pitch = Note.new_from_number(ending_pitch)
    elif not isinstance(ending_pitch, Note):
      raise Exception('Pitch is neither a viable string, integer, or Note!')

    self.starting_pitch = starting_pitch
    self.ending_pitch = ending_pitch
    self.semitones = abs(starting_pitch.num-ending_pitch.num)
    self._name = self._find_name(starting_pitch, ending_pitch)

  def __repr__(self):
    return ('Interval({}->{}, \'{}\')'.format(self.starting_pitch, self.ending_pitch, self._name))

  def _find_name(self, starting_pitch, ending_pitch):
    names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    notes = [starting_pitch, ending_pitch]
    notes.sort(key=lambda x: x.num) # sort it
    idx_of_start = names.index(notes[0].str[0]) # get the starting index in note names
    size = 0
    while names[idx_of_start] != notes[1].str[0]:
      idx_of_start = (idx_of_start+1) % 7 # increment by 1, modulo 7
      size += 1 # add 1 to the size

    if size==0:
      if notes[0].octave==notes[1].octave:
        name = 'unison'
      else:
        name = 'octave'
    elif size==1:
      name = 'second'
    elif size==2:
      name = 'third'
    elif size==3:
      name = 'fourth'
    elif size==4:
      name = 'fifth'
    elif size==5:
      name = 'sixth'
    elif size==6:
      name = 'seventh'
    else:
      raise Exception('Cannot name interval. Something went wrong: size = {}'.format(size))

    quality = (self.semitones%12) - self.named_intervals[name]

    # octaves and unisons
    if name in ['octave', 'unison', 'fifth', 'fourth']:
      if quality is -1:
        quality = 'diminished'
      elif quality is -2:
        quality = 'doubly diminished'
      elif quality is 1:
        quality = 'augmented'
      elif quality is 2:
        quality = 'doubly augmented'
      else:
        quality = 'perfect'
    else:
      quality = [name for name, steps in self.modifiers.items() if steps==quality][0]

    if self.semitones > 12:
      if int(self.semitones/12) == 1:
        return '{} {} plus an octave'.format(quality, name)
      else:
        return '{} {} plus {} octaves'.format(quality, name, int(self.semitones/12))
    else:
      return '{} {}'.format(quality, name)

  # getter and setter
  @property
  def name(self):
    return self._name
