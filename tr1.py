#*************************
#**** lire les donnes****

FileRead = open("tr1.txt","r")
#stocker les donnes dans une liste
infoTab=[]
for line in FileRead:
    fields =line.split('\t')
    infoTab.append(fields)
    
    
num=len(infoTab)

#*****************************
#*** page web  ***************


htmlD = "<!DOCTYPE html><html><head><meta charset=\"utf-8\">" \
          "<title> travieel a domicile </title></head><body><table border=\"solid\"><tr></tr>"

htmlFin = "</table></body></html>"




FileWrite = open("addd.html", "w")
FileWrite.write(htmlD)



#*******************************
#*********** les calcules ******

nbrAdmis = 0
nbrAdDettes = 0
nbrAjournee = 0
listMoy = []

#infoLine = info.split("\n")
infoTab=[x+[0] for x in infoTab]
infoTab[0][9]="resltat"
for i in range(1,num-1):
  if (float(infoTab[i][5]))>= 10:
    infoTab[i][9]="admis"
    nbrAdmis += 1
  elif (float(infoTab[i][5]))<10 and (float(infoTab[i][6])+float(infoTab[i][7]))>= 45:
    infoTab[i][9]="admis avec dettes"
    nbrAdDettes += 1
  else:
    infoTab[i][9]="ajournee"
    nbrAjournee += 1
    
tot=nbrAdmis+nbrAdDettes +nbrAjournee
#*******liste de myn*****
mx=float(infoTab[1][5])
mn=float(infoTab[1][5])
for i in range(1,num-1):
  if(float(infoTab[i][5]))>mx:
    mx=(float(infoTab[i][5]))
  if(float(infoTab[i][5]))<mn:
    mn=(float(infoTab[i][5]))

          



#****************************
#**** l'affichage**********

for i in range(0,num-1):
   FileWrite.write("<TR>") 
   FileWrite.write(  "<td >" + str(infoTab[i][0]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][1]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][2]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][3]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][4]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][5]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][6]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][7]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][8]) + " </td>")
   FileWrite.write(  "<td >" + str(infoTab[i][9]) + " </td>")
   FileWrite.write("</TR>")
FileWrite.write(htmlFin)


FileWrite.write("<h5>  - La meilleure moyenne est:  " + str(mx) + "</h5>")
FileWrite.write("<h5>  - La mauvaise moyenne est:   " + str(mn) + "</h5>")

FileWrite.write("<h5>  - Le nbr des etudiants Admits: " + str(nbrAdmis) + "  ( " + str(round((nbrAdmis * 100) / tot, 3)) + "% )</h5>")
FileWrite.write("<h5>  - Le nbr des etudiants Admits avec dettes: " + str(nbrAdDettes) + "  ( " + str(round((nbrAdDettes * 100) / tot, 3)) + "% )</h5>")
FileWrite.write("<h5>  - Le nbr des etudiants Admits ajournee: " + str(nbrAjournee) + "  ( " + str(round((nbrAjournee * 100) / tot, 3)) + "% )</h5>")
FileRead.close()