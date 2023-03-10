#spinningWords

def spinningWords(sentence):
    for string in sentence:
        if string >= 5:
           string[::-1]
    return string

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
