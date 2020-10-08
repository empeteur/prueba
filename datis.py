import csv
with open ("Incidencia_casos.csv","r") as f:
    red=csv.reader(f,delimiter=",")
    D=0
    for i in red:
        
        print("este es",D,len(i))
        D+=1

