#!/usr/bin/python

import app

class GoGame(app.App):
  # Go commands
  def drawGrid(self, params=[]):
  	pass

  def makeInputMap(self):
    return {
      'ls': self.drawGrid
    }

  def __init__(self):
    app.App.__init__(self)
    self.inputMap.update(self.makeInputMap())

# for testing
game = GoGame()
game.ui()
