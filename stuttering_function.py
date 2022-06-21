#https://edabit.com/challenge/gt9LLufDCMHKMioh2

#Write a function that stutters a word as if someone is struggling to read it.
#The first two letters are repeated twice with an ellipsis
#ex:
#stutter("incredible") ➞ "in... in... incredible?"

def stutter(word):
    return word[0:2] + '... ' + word[0:2] + '... ' + word + '?'
