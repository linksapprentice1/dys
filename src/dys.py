# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *

def printGameTable(days, left_or_right):
   print """<table class=\"tableizer-table\" style=\"float:""" + left_or_right +"""\">
	<tbody>
		<tr class=\"tableizer-firstrow\">
			<th>DAY</th>
			<th>DATE</th>
			<th>&nbsp;TIME&nbsp;</th>
			<th>&nbsp;HOME TEAM&nbsp;</th>
			<th>&nbsp;AWAY TEAM&nbsp;</th>
		</tr> """
   for i, day in enumerate(days):
      day_line = day.strip().split("\n")
      print """    <tr>
			<td>""" + day_line[0] + """</td>
			<td>""" + day_line[1] +  """</td>
		        <td style="border:none">&nbsp</td>
			<td style="border:none">&nbsp</td>
			<td style="border:none">&nbsp</td>
                  </tr>"""
      for j, game in enumerate(day_line[2:]):
         game_parts = game.strip().split()
         print """<tr>
			<td style="border:none">&nbsp</td>
                       	<td style="border:none">&nbsp</td>	
                        <td>""" + game_parts[0] + """</td>
	                <td>""" + game_parts[1] + """</td>
	                <td>""" + game_parts[2] + """</td>
	          </tr>"""
#      if i < len(days)-1:
#         print """<tr>
#			<td>&nbsp;</td>
#			<td>&nbsp;</td>
#			<td>&nbsp;</td>
#			<td>&nbsp;</td>
#			<td>&nbsp;</td>
#            </tr>"""
		
   print """</tbody>
   </table>"""

def printCoachTable(coaches):
   print """<table class=\"tableizer-table\">
      <tbody>
		<tr class=\"tableizer-firstrow\">
			<th colspan="12">&nbsp;Coaches&nbsp;</th>
		</tr>
		<tr> """
   for index, coach in enumerate(coaches):
      print """<td>""" + str(index) + """</td>"""
      print """<td>""" + coach + """</td>"""
   print """</tr>
	</tbody>
    </table> """ 


#GUI


root = Tk()
root.wm_title("Generate Tables")

w = Label(root, text="Select template text file.") 
fileName = askopenfilename(parent=root, title="Select template text file")

#Enter data

input = open(fileName).read()

sections = [x for x in input.split('~')]
time, age_group = sections[0].strip().split("\n")[:2]
days = sections[1:len(sections)-2]
coaches = sections[len(sections)-2].strip().replace("\n", ":").strip().split(":")[1::2]
director = sections[len(sections)-1].strip().replace("\n", ":").strip().split(":")[1]

import base64
file_name_string = base64.urlsafe_b64encode(time + "_" + age_group)[:23]
sys.stdout = open(file_name_string + ".txt", "w")

print """<p>&nbsp;</p>

<h1>""" + time + """&nbsp;""" + age_group + """</h1>

<h2>GAMES AT RUSTCRAFT</h2>

<p><br />
<style type=\"text/css\">
h1,h2,p{
   text-align:center;
}
h2{
   margin-bottom: 0px;
}
table.tableizer-table {
    margin: 0 auto; 
	border: 1px solid #CCC; font-family: Arial, Helvetica, sans-serif
	font-size: 12px;
} 
.tableizer-table td {
    text-align: center;
	padding: 4px;
	margin: 3px;
	border: 1px solid #ccc;
}
.tableizer-table th {
	background-color: #B33333; 
	color: #FFF;
	font-weight: bold;
}
</style>
</p>"""

print """<div style=\"margin: 0 auto;display: table;\">"""

printGameTable(days[:len(days)/2], "left")

print """<div style=\"float:left;width:10px\">&nbsp;</div>"""

printGameTable(days[len(days)/2:], "right")

print """</div><div style=\"clear:both;height:10px\">&nbsp;</div>"""

printCoachTable(coaches)

print """<p>&nbsp;</p><h1>Director: """ + director + """</h1>"""

sys.stdout.flush()

import shutil
shutil.copy2(file_name_string + ".txt", file_name_string + ".html")

import webbrowser
import time

webbrowser.open(file_name_string + ".html")
time.sleep(2)

import subprocess
subprocess.call("cscript notepad.vbs " + file_name_string + ".txt", shell=True)

