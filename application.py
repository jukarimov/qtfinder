#!/usr/bin/env python

import sys
from PyQt4 import QtGui
import sqlite3 as db


class Application(QtGui.QWidget):

	def __init__(self):
		super(Application, self).__init__()

		self.dbName = '.qtfinder.db'
		self.initDB()
		self.initUI()

	def initDB(self):
		con = None
		try:
			con = db.connect(self.dbName)
			cur = con.cursor()
			cur.execute('SELECT SQLITE_VERSION()')

			data = cur.fetchone()

			print "SQLite version: %s" % data
		except db.Error, e:
			print "Error %s:" % e.args[0]

		finally:
			if con:
				con.close()

	def findFile(self, name):
		con = None
		try:
			con = db.connect(self.dbName)
			cur = con.cursor()
			cur.execute("SELECT file FROM idx WHERE file LIKE '%%%s%%'" % name)

			data = cur.fetchall()

			self.results = QtGui.QListWidget()

			print len(data), 'rows'
			for i in data:
				print i
				self.results.addItem(i[0])
			self.results.show()
		except db.Error, e:
			print "Error %s:" % e.args[0]

		finally:
			if con:
				con.close()

	def getInput(self):
		print 'Input:', self.le.text()
		self.findFile(self.le.text())

	def initUI(self):

		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

		self.setToolTip('This is a <b>QWidget</b> widget')

		self.le = QtGui.QLineEdit(self)
		self.le.move(10, 22)
		self.le.resize(300, 25)

		button = QtGui.QPushButton('Find', self)

		button.setToolTip('Thisis a <b>QPushButton</b> widget')

		button.clicked.connect(self.getInput)

		button.resize(button.sizeHint())

		button.move(10, 50)

		self.setGeometry(300, 300, 250, 100)

		self.setWindowTitle('Application');

		self.show()

def main():

	app = QtGui.QApplication(sys.argv)
	ex = Application()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

