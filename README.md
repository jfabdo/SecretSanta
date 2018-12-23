# SecretSanta
Secret Santa-generating Python class

# Origin
Last year, I decided to solve the age-old problem of "how do we choose Secret Santas" programatically. But I was short on time and feeling ill, so I wrote it as a Bozo sort, which I knew wouldn't scale well for larger organizations.

# Latest Version
This year, I decided to fix it as well as making it into a class as it should be. This can be pulled into any python program and used however you choose, whether you want it to text everyone their assigned recipient for a truely blind Secret Santa experience, or export it as a CSV. You choose.

# Advantages
Runs in N time. Uses random choice without replacement for efficiency. Users can be represented by any python or binary object, even employees with the same name, and the system will be able to differentiate them.

# Usage
Ex:  

      from secretsanta import SecretSanta as sesan  

      test = ["Ada","Luna","Alice","Carol","Jim","Bob","Frank","Sam"]  
      
      santaobj = sesan(test)  
      
      for i in santaobj.Matches.keys():
         
         print("{}: {}".format(i,santaobj.Matches[i]))
