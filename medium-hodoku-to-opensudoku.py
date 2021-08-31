#!/usr/bin/python3

header =  """<?xml version="1.0" encoding="UTF-8"?>
<opensudoku>
  <name>Hodoku Medium</name>
  <author>rogerm4242</author>
  <description></description>
  <comment></comment>
  <created>2014-01-11</created>
  <source>hodoku</source>
  <level>Medium</level>
  <sourceURL>http://hodoku.sourceforge.net</sourceURL>
"""

footer = """</opensudoku>
"""

f = open("Medium.txt", 'r')
new_file = open("Medium.opensudoku", 'w')

new_file.write(header)

while 1:
    l = f.readline()
    if not l:
        break
    game = l.strip().replace('.', '0').split()[0]
    new_file.write(' <game data="' + game + '"/>\n')

new_file.write(footer)