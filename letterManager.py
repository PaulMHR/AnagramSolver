class NoLetter(Exception):
  def __init__(self, val):
      self.val = val
              
  def __str__(self):
    return str(self.val)
    

class LetterManager:
    
  def __init__(self, letters):
    self.letters = letters.lower()
    self.counts = [0] * 26
    self.sze = 0
    self.calculateCounts()
    
  def calculateCounts (self):
    for ch in self.letters:
      ch = ch.lower()
      if ord (ch) >= ord ('a') and ord (ch) <= ord ('z'):
        ind = ord(ch) - ord('a')
        self.counts[ind] = self.counts[ind] + 1
        self.sze += 1
      
  def Set (self, letter, value):
    if ord (letter) < ord ('a') or ord (letter) > ord ('z'):
      raise NoLetter (letter)
    self.sze = self.sze - self.counts[ord(letter) - ord ('a')] + value
    self.counts[ord(letter) - ord ('a')] = value

  def Get (self, letter):
    if ord (letter) < ord ('a') or ord (letter) > ord ('z'):
      raise NoLetter (letter)
    return (self.counts[ord(letter) - ord('a')])
  
  def Size (self):
    return (self.sze)
    
  def IsEmpty (self):
    return self.sze == 0
    
  def __str__ (self):
    temp = ""
    for i in range(26):
      #print i
      temp = temp + (chr(i + ord ('a')) * (self.counts[i]))
    return temp  
       
  def Add (self, other):
    newLett = LetterManager ("")
    for i in range (26):
      lett = chr(i + ord ('a'))
      newLett.Set (lett, self.Get (lett) + other.Get (lett))
    return (newLett)
  
  def Subtract (self, other):
    newLett = LetterManager ("")
    for i in range (26):
      lett = chr(i + ord ('a'))
      if self.Get (lett) - other.Get (lett) < 0:
        return (None)  
      newLett.Set (lett, self.Get (lett) - other.Get (lett))
    return (newLett)
