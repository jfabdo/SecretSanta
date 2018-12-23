from random import sample

class SecretSanta: 
  
  def __init__(self, group=[]):
    self.group = group        # group of people that are involved
    
    def match_santas(self):
       #secsantalist will contain an unchecked list of secret santas
       poplen = len(self.group)  # population length
       secsantalist = sample(range(poplen),poplen) 
       
       
       #check and avoid collisions based on string comparisons
       for i in range(poplen):
         if i == secsantalist[i]:
           j = secsantalist[i+1]
           secsantalist[i+1] = i
           secsantalist[i] = j

       finalsantalist = []
       for i in range(poplen):
         finalsantalist.append(self.group[secsantalist[i]])
       
       return dict(zip(self.group,finalsantalist))
    
    self.Matches = match_santas(self)
    
    
