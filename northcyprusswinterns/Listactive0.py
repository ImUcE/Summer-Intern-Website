#!/Python/Python38/python
import cgi
import sqlite3
import os
import http.cookies as Cookie
import time

def printHeader(title):

    print("Content-type: text/html")
    print("")
    print("""<html><head>
    <title>Internship</title>
          <link rel="stylesheet" type="text/css" href="style.css"></head><body>""")
def printFooter():
    print("</body></html>")

printHeader("List Active")
conn=sqlite3.connect("internship.db")
c=conn.cursor()
print("<form>")
print("""<div class="tablebox"><h1>Active in Girne</h1>""")
print("""<table class="content-table "><thead><tr><th>Company Name</th><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
<tbody>""")
c.execute("SELECT companyName,positioName,description,expectations,deadline FROM internships INNER JOIN companies ON internships.companyName=companies.name WHERE companies.city='Girne'") #ORDER BY strftime('%Y-%m-%d', internships.deadline)
rows = c.fetchall()
for row in rows:
    print("""<tr class="clickable text-center"
               onclick="window.location='http://localhost/northcyprusswinterns/companydetails.html'">""")
    for col in row:
        print("<td>{}</td>".format(col))
    print("</tr>")
print("""</tbody></table>""")
print("<br>")
#print("""<div class="tablebox"><p>Active in Girne</p>""")
#print("""<table class="content-table "><thead><tr><th>Company Name</th><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
#<tbody>""")
#c.execute("SELECT companyName,positioName,description,expectations,deadline FROM internships INNER JOIN companies ON internships.companyName=companies.name WHERE companies.city='Girne'") #ORDER BY strftime('%Y-%m-%d', internships.deadline)
#rows = c.fetchall()
#for row in rows:
#    print("<tr>")
#    for col in row:
#        print("<td>{}</td>".format(col))
#    print("</tr>")
#print("""</tbody></table>""")
#print("""<div class="tablebox"><h1>Active in Guzelyurt</h1>""")
#print("""<table class="content-table "><thead><tr><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
#<tbody>""")
#c.execute("SELECT positioName,description,expectations,deadline FROM internships ORDER BY strftime('%Y-%m-%d', deadline)")
#SELECT doctors.doctor_id,doctors.doctor_name,visits.patient_name
#FROM doctors
#ON doctors.doctor_id=visits.doctor_id
#WHERE doctors.degree='MD';
#rows = c.fetchall()
#for row in rows:
#    print("<tr>")
    #for col in row:
    #    print("<td>{}</td>".format(col))
   #print("</tr>")
#print("""</tbody>
#</table>""")
#print("""<div class="tablebox"><h1>Active in Iskele</h1>""")
#print("""<table class="content-table "><thead><tr><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
#<tbody>""")
#c.execute("SELECT positioName,description,expectations,deadline FROM internships ORDER BY strftime('%Y-%m-%d', deadline)")
#SELECT doctors.doctor_id,doctors.doctor_name,visits.patient_name
#FROM doctors
#ON doctors.doctor_id=visits.doctor_id
#WHERE doctors.degree='MD';
#rows = c.fetchall()
#for row in rows:
#    print("<tr>")
    #for col in row:
    #    print("<td>{}</td>".format(col))
   #print("</tr>")
#print("""</tbody>
#</table>""")
#print("""<div class="tablebox"><h1>Active in Lefke</h1>""")
#print("""<table class="content-table "><thead><tr><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
#<tbody>""")
#c.execute("SELECT positioName,description,expectations,deadline FROM internships ORDER BY strftime('%Y-%m-%d', deadline)")
#SELECT doctors.doctor_id,doctors.doctor_name,visits.patient_name
#FROM doctors
#ON doctors.doctor_id=visits.doctor_id
#WHERE doctors.degree='MD';
#rows = c.fetchall()
#for row in rows:
#    print("<tr>")
    #for col in row:
    #    print("<td>{}</td>".format(col))
   #print("</tr>")
#print("""</tbody>
#</table>""")
#print("""<div class="tablebox"><h1>Active in Lefkosa</h1>""")
#print("""<table class="content-table "><thead><tr><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
#<tbody>""")
#c.execute("SELECT positioName,description,expectations,deadline FROM internships ORDER BY strftime('%Y-%m-%d', deadline)")
#SELECT doctors.doctor_id,doctors.doctor_name,visits.patient_name
#FROM doctors
#ON doctors.doctor_id=visits.doctor_id
#WHERE doctors.degree='MD';
#rows = c.fetchall()
#for row in rows:
#    print("<tr>")
    #for col in row:
    #    print("<td>{}</td>".format(col))
   #print("</tr>")
#print("""</tbody>
#</table>""")
print("</form>")
printFooter()