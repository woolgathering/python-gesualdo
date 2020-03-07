"""
Key
"""

from gesualdo.core.Note import Note
from gesualdo.core.Interval import Interval

class Key:

  major_scale = [0, 2, 4, 5, 7, 9, 11]
  minor_scale = [0, 2, 3, 5, 7, 8, 10]
  harmonic_minor_scale = [0, 2, 3, 5, 6, 9, 11]

  def __init__(self, key='C', quality='maj'):
    self.key = self._format_key(key) # format the key
    self.quality = quality
    self._signature = self._get_signature(self.key, quality)

  def __repr__(self):
    return ('Key({} {}, signature: {})'.format(self.key, self.quality, self._signature))

  def _get_signature(self, key, quality):
    major_sharp_keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
    major_flat_keys = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb']
    minor_sharp_keys = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'G#']
    minor_flat_keys = ['A', 'D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab']

    if quality is 'maj':
      if key is 'C':
        type = None
        number = 0
      elif key in major_sharp_keys:
        type = 'sharps'
        number = major_sharp_keys.index(key)
      elif key in major_flat_keys:
        type = 'flats'
        number = major_flat_keys.index(key)
      else:
        raise Exception('No such major key {}'.format(key))
    elif quality is 'min':
      if key is 'A':
        type = None
        number = 0
      elif key in minor_sharp_keys:
        type = 'sharps'
        number = minor_sharp_keys.index(key)
      elif key in minor_flat_keys:
        type = 'flats'
        number = minor_flat_keys.index(key)
      else:
        raise Exception('No such minor key {}'.format(key))
    else:
      raise TypeError('No such key quality as {}'.format(quality))

    return (type, number)

  def _format_key(self, key):
    if len(key) is 1:
      key = key[0].upper()
    else:
      key = key[0].upper() + key[1].lower()
    return key

  def scale(self, octave=4):
    if self.quality is 'maj':
      return self._major_scale(octave)
    else:
      return self._minor_scale(octave)

  def _major_scale(self, octave=4):
    f = Note('{}{}'.format(self.key, octave))
    return [Note.from_number(f.num+n) for n in self.major_scale]

  def _minor_scale(self, octave=4):
    f = Note('{}{}'.format(self.key, octave))
    return [Note.from_number(f.num+n) for n in self.minor_scale]

  @property
  def signature(self):
    return self._signature
