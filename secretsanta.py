from random import sample

class SecretSanta: 
  
  def __init__(self, group=[]):
    self.group = group        # group of people that are involved
    
    def match_santas(self):
       #secsantalist will contain an unchecked list of secret santas
       poplen = len(self.group)  # population length
       secsantalist = sample(self.group,poplen) 
       
       #check and avoid collisions based on string comparisons
       for i in range(poplen):
         while self.group[i] == secsantalist[i]:
           j = i % poplen
           k = (j + 1) % poplen
           
           tempsanta = secsantalist[k]
           secsantalist[k] = secsantalist[j]
           secsantalist[j] = tempsanta
           i = (i + 1) % poplen
       
       return dict(zip(self.group,secsantalist))
    
    self.Matches = match_santas(self)
    
    
