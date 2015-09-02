#!/usr/bin/python

# Parent class for python games and tools that have repls and user commands
# Intended as an abstract class: don't instantiate this, rather instantiate an extension of this.

# Example usage from python repl:
# (Where class Game extends App in commander.py)
#
# import commander as c
# g = c.Game()
# g.do('ls')
# g.ui()
#

# I could standardize, i know.
# Eg i could just list out all possible messages like an enum.
# I'm allowing several so i dont have to look up what i chose, when extending.
# TODO could store these as all lowercase.

# If parseInput() returns one of these strings, end the repl.
closeResponses = ['closeUi', 'quit', 'close', 'exit', 'done']
parseFailResponses = ['cantParse', 'parseFail', 'noParse']

# One of the app's command functions.
def closeUi(paramsList=[]):
  # Arbitrary element.
  return closeResponses[0]

def makeUniversalInputMap():
  return {
    'quit': closeUi
  }

class App:
  def __init__(self):
    self.inputMap = makeUniversalInputMap()

  def parseInput(self, rawInput):
    if len(rawInput) <= 0:
      return 'cantParse'

    words = rawInput.lower().split()
    firstWord = words[0]

    if firstWord in self.inputMap:
      # self.inputMap[firstWord](words[1:])
      # TODO transform string input to params in some way
      pass

  # Convenience function
  def do(self, command):
    return self.parseInput(command)

  # Launch the app-specific repl for ease of typing
  def ui(self):
    print ''
    done = False
    while not done:
      print ''
      rawinput = raw_input('> ')
      print ''
      commandResponse = self.parseinput(rawinput)
      if commandResponse in closeResponses:
        done = True
    print 'Closing app interface. Farewell.\n'
