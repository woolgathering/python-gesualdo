"Note Class"

class Note:

  enharmonic_name_steps = {
    # C
    'B#': 0,'C': 0,'Dbb': 0,
    # C#
    'Bx': 1,'C#': 1,'Db': 1,
    # D
    'Cx': 2,'D': 2,'Ebb': 2,
    # Eb
    'D#': 3,'Eb': 3,'Fbb': 3,
    # E
    'Dx': 4,'E': 4,'Fb': 4,
    # F
    'E#': 5,'F': 5,'Gbb': 5,
    # F#
    'Ex': 6,'F#': 6,'Gb': 6,
    # G
    'Fx': 7,'G': 7,'Abb': 7,
    # Ab
    'G#': 8,'Ab': 8,
    # A
    'Gx': 9,'A': 9,'Bbb': 9,
    # Bb
    'A#': 10,'Bb': 10,
    # B
    'Ax': 11,'B': 11,'Cb': 11,
  }

  def __init__(self, pitch='A4'):
    # nameOct = self.check_pitch(pitch)
    self._str, self._octave = self.check_pitch(pitch)
    self._num = self.get_number()
    self._enharmonic_equivalents = self.get_enharmonic_equivalents() # a list of enharmonic equivalents

  def __repr__(self):
    return ('Note(\'{}{}\')'.format(self._str, self._octave))

  def get_number(self):
    st = self.get_steps() # need to get enharmonic equivalents here
    return ((self._octave+1)*12)+st

  # @private
  def get_steps(self):
    return self.enharmonic_name_steps[self._str]

  def get_enharmonic_equivalents(self):
    st = self.get_steps()
    return [name for name, steps in self.enharmonic_name_steps.items() if steps==st]

  def hz(self):
    print ("Not yet implemented!")

  def check_pitch(self, key):
    # pitch = key[0].upper()+key[1:].lower() # format it
    pitch = key[:-1]
    if len(pitch) > 1:
      pitch = pitch[0].upper() + pitch[1:]
    octave = int(key[-1]) # get the octave
    print (pitch, octave)
    if pitch in self.enharmonic_name_steps.keys():
      return [pitch, octave]
    else:
      KeyError("No such note! Use format: noteName+accidental.")

  # distance between this note and another
  def interval(self, note, return_type='semitones'):
    if return_type == 'semitones':
      return note.num - self._num
    elif return_type == 'interval':
      return Interval(self, note)
    else:
      raise Exception("Bad return_type: {}".format(return_type))

  ##############################
  # getters and setters
  ##############################
  @property
  def str(self):
    return self._str

  @property
  def octave(self):
    return self._octave

  @property
  def num(self):
    return self._num

  @property
  def enharmonic_equivalents(self):
    return self._enharmonic_equivalents
