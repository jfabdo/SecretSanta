# SecretSanta
Secret Santa-generating Python class

# Origin
Last year, I decided to solve the age-old problem of "how do we choose Secret Santas" programatically. But I was short on time and feeling ill, so I wrote it as a Bozo sort. 

# Latest Version
This year, I decided to fix it and make it into a class as it should be. This can be pulled into any python program and used however you choose, whether you want it to text everyone their assigned recipient for a truely blind Secret Santa experience, or export it as a CSV. You choose.

# Advantages
Runs in N time, uses random choice without replacement for efficiency.

# Disadvantages
Since I used string-based comparison instead of position based comparison to make sure that people were not assigned to themeselves, if you have people with the same name, this will try not to let them be paired with each other, skewing the probability distribution for users keen to deduce who has whom. 

# The future
I gave some thought to doing it with position based comparision but decided that this was for a laugh and a bit of holiday cheer, regardless of denomination or religion. I may go back and fix this later. If I were to do that, I would rewrite this in Kotlin, so that it could be run on the JVM, and possibly be made into an app for ease of Secret Santa choosing.
