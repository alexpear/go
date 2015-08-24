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

closeReponses = {'closeUi', 'quit', 'close', 'exit', 'done'}

def closeUi():
  return closeResponses[0]

def universalInputMap():
  return {
    'quit': closeUi
  }

class App:
  def __init__(self):
    self.inputMap = universalInputMap()

  def parseInput(self, rawInput):
    if len(rawInput) <= 0:
      return 'invalid'

    # print ''
    cleanedInput = rawInput.lower().strip()
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
