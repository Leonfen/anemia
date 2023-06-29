import csv
import os

fileCartellaClinicheXlsx = "CartellaCliniche.xlsx"
fileCartellaClinicheCsv = "CartellaCliniche.csv"

def HeadCVS():
    f = open(fileCartellaClinicheCsv, "r")
    listHead = f.readline().split(",")
    f.close()
    return listHead

def AggiungiCartellaClinica():
    print("-----------------------------------------")
    listHead = HeadCVS()
    listNuovaCartella = []
    for elem in listHead:
        newElem = input("Inserisci "+ elem.strip() + " : " )
        listNuovaCartella.append(newElem)
    print(listNuovaCartella)
    conferma = input("Digitare s per confermare inserimento : ")

    if conferma == "s":
        f = open(fileCartellaClinicheCsv, "a")
        for i in range(len(listNuovaCartella)):
            if i == len(listNuovaCartella) - 1:
                f.write("\"" + listNuovaCartella[i] + "\"")
            else:
                f.write("\"" + listNuovaCartella[i] + "\"" + ',')
        f.write('\n')
        f.close()
    print("Inserimento cartella clinica eseguita con successo")


def CercaCartellaClinica():
    print("-----------------------------------------")
    testoDaCercare = input("Inserisci il testo cercare (invio per elencarli tutti): ")

    f = open(fileCartellaClinicheCsv, "r")
    count = 0
    f.readline()
    for riga in f:
        count += 1
        if testoDaCercare in riga:
            print("Riga", count, " :", riga, end="")
    f.close()
    print("Ricerca eseguita con successo")

def RimuoviCartellaClinica():
    CercaCartellaClinica()
    rigaDaEliminare = int(input("Inserire il numero di riga da eliminare : "))
    fin = open(fileCartellaClinicheCsv, "r")
    fout = open("tempfile.txt", "w")
    count = 0
    for riga in fin:
        if count != rigaDaEliminare:
            fout.write(riga)
        count += 1

    fin.close()
    fout.close()

    os.remove(fileCartellaClinicheCsv)
    os.rename("tempfile.txt", fileCartellaClinicheCsv)

    print("Rimozione eseguita con successo")

def ModificaCartellaClinica():
    CercaCartellaClinica()
    numeroRiga = int(input("Inserisci il numero della riga da modificare : "))
    fin = open(fileCartellaClinicheCsv, "r")
    fout = open("tempfile.txt", "w")
    count = 0
    for riga in fin:
        if count != numeroRiga:
            fout.write(riga)
        else:
            listHead = HeadCVS()
            listVecchiaCartella = riga.split(",")
            for i in range(len(listVecchiaCartella)):
                listVecchiaCartella[i]=listVecchiaCartella[i].replace("\"","").strip()
            listNuovaCartella = []

            for i in range(len(listHead)):
                newElem = input("Inserisci " + listHead[i].strip()  +"(" + listVecchiaCartella[i].strip() + ")  : ")
                if newElem == "":
                    listNuovaCartella.append(listVecchiaCartella[i])
                else:
                    listNuovaCartella.append(newElem)

            for i in range(len(listNuovaCartella)):
                if i == len(listNuovaCartella) - 1:
                    fout.write("\"" + listNuovaCartella[i] + "\"\n")
                else:
                    fout.write("\"" + listNuovaCartella[i] + "\"" + ',')

        count += 1

    fin.close()
    fout.close()

    os.remove(fileCartellaClinicheCsv)
    os.rename("tempfile.txt", fileCartellaClinicheCsv)

    print("Modifica eseguita con successo")

def PrintScelte():
    print("-----------------------------------------")
    print("1 : Aggiungi cartella clinica ")
    print("2 : Cerca cartella clinica ")
    print("3 : Rimuovi cartella clinica ")
    print("4 : Modifica cartella clinica ")
    print("5 : Converti XLSX in CSV ")
    print("6 : Esegui query ")
    print("7 : Chiudi ")


def Xlsx2Csv(inputXlsxFile, outputCsvFile):
    print("-----------------------------------------")
    ## opening the xlsx file
    xlsx = openpyxl.load_workbook(inputXlsxFile)

    ## opening the active sheet
    sheet = xlsx.active

    ## getting the data from the sheet
    data = sheet.rows

    ## creating a csv file
    csv = open(outputCsvFile, "w+")

    for row in data:
        l = list(row)
        for i in range(len(l)):
            if i == len(l) - 1:
                csv.write("\"" + str(l[i].value) + "\"")
            else:
                csv.write("\"" + str(l[i].value) + "\"" + ',')
        csv.write('\n')

    ## close the csv file
    csv.close()
    print("Conversione eseguita con successo")

def Query1(inputCsvFile, outputCsvFile):
    print("-----------------------------------------")
    # Open the two csv files.
    infile = open(inputCsvFile)
    csvReader = csv.reader(infile)

    outfile = open(outputCsvFile, "w")
    csvWriter = csv.writer(outfile, lineterminator='\n')

    # Add the list of column headers to the csv file.
    headers = ["Nome", "Cognome", "FerroMaggioreOUgualeA10"]
    csvWriter.writerow(headers)

    # Skip the row of column headers in the reader.
    next(csvReader)

    # Filter the rows of data.

    for row in csvReader:

        output = row[4].split(',')



    infile.close()
    outfile.close()
    print("Query 1 eseguita con successo")

def Query2(inputCsvFile, outputCsvFile):
    print("-----------------------------------------")
    # Open the two csv files.
    infile = open(inputCsvFile)
    csvReader = csv.reader(infile)

    outfile = open(outputCsvFile, "w")
    csvWriter = csv.writer(outfile, lineterminator='\n')

    # Add the list of column headers to the csv file.
    headers = ["Nome", "Cognome", "FerroMaggioreOUgualeA10"]
    csvWriter.writerow(headers)

    # Skip the row of column headers in the reader.
    next(csvReader)

    # Filter the rows of data.

    for row in csvReader:

        output = row[4].split(',')

        for elem in output:
            if elem.startswith("ferro="):
                valoreFerro = elem.split("=")[1]
                if int(valoreFerro) >= 10:
                    newRow = [row[0], row[1], valoreFerro]
                    csvWriter.writerow(newRow)

    infile.close()
    outfile.close()
    print("Query 2 eseguita con successo")

############### MAIN ################################################################
'''
scelta = -1
while scelta != 7:
    PrintScelte()
    scelta = int(input("Inserisci numero operazione : "))
    if scelta == 1:
        AggiungiCartellaClinica()
    elif scelta == 2:
        CercaCartellaClinica()
    elif scelta == 3:
        RimuoviCartellaClinica()
    elif scelta == 4:
        ModificaCartellaClinica()
    elif scelta == 5:
        Xlsx2Csv(fileCartellaClinicheXlsx, fileCartellaClinicheCsv)
    elif scelta == 6:
        Query1(fileCartellaClinicheCsv, "Query1.csv")
        Query2(fileCartellaClinicheCsv, "Query2.csv")
    elif scelta == 7:
        break
'''

def cambiamento(file1, file2, file3) -> None:
    print("-----------------------------------------")
    # Open the two csv files.
    infile1 = open(file1)
    infile2 = open(file2)
    csvReader1 = csv.reader(infile1)
    csvReader2 = csv.reader(infile2)

    outfile = open(file3, "w")
    csvWriter = csv.writer(outfile, lineterminator='\n')

    # Add the list of column headers to the csv file.
    headers = ["Nome", "Cognome", "Sesso", "Analisi Molecolari", "Analisi Istologiche", "Emoglobina"]
    csvWriter.writerow(headers)

    # Skip the row of column headers in the reader.
    next(csvReader1)
    next(csvReader2)

    # Filter the rows of data.

    for index, row in enumerate(csvReader1, 1):
                
        while row[0] == csvReader1[index - 1][0]:
            pass

    infile1.close()
    infile2.close()
    outfile.close()
    print("Query 2 eseguita con successo")


def leggereValori(inputFile: str) -> list[list[str, int]]:
    infile = open(inputFile)
    csvReader = csv.reader(infile)

    next(csvReader)

    # Declare all values
    emoglobina: list[float] = [] 
    analisiCorpuscolari: list[list[float]] = []
    analisiIstologiche: list[str] = []
    genere: list[str] = []
    intervallo: list[tuple[str, str]] = []
    ferritina: list[float] = []
    nome: list[str] = []

    for row in csvReader:   
        nome.append(row[0]) # Take name
        genere.append(row[1]) # Take gender
        analisiIstologiche.append(row[2]) # Take analisis as a single string
        # Take the values splitted by a comma
        MHC, MCHC, MCV = row[3], row[4], row[5]
        analisiCorpuscolari.append([MHC.split('=')[1], 
                                    MCHC.split('=')[1],
                                    MCV.split('=')[1]
                                    ]) #* Only take the value

        # Take the intervals
        intervalloCorpuscolato = row[6].split(';')
        intervalloMolecolare = row[9].split(';')
        intervallo.append([
                           (intervalloMolecolare[0].split('-')[0], intervalloCorpuscolato[0].split('-')[1]), # Hemoglobin
                           (intervalloCorpuscolato[0].split('-')[0], intervalloCorpuscolato[0].split('-')[1]), # MCH
                           (intervalloCorpuscolato[1].split('-')[0], intervalloCorpuscolato[1].split('-')[1]), # MCHC
                           (intervalloCorpuscolato[2].split('-')[0], intervalloCorpuscolato[2].split('-')[1]), # MCV
                           (intervalloMolecolare[1].split('-')[0], intervalloMolecolare[1].split('-')[1]) # Ferritina
                           ]) # Split the interval
                
        # Analisi molecolari
        ferritina.append(row[8].split('=')[1])
        emoglobina.append(row[7].split('=')[1])
        #* Only take the value

    infile.close()
    return [nome, emoglobina, analisiCorpuscolari, analisiIstologiche, genere, intervallo, ferritina]
    #* Returns with the same index all the values referring to the same person

def mediaEmoglobina():
    pass

def mediaEmoglobinaMvF():
    pass

def soggettiFerritinaMinore20():
    pass

def valoriMaggiori():
    "Segna i tizi con i valori maggiori di ogni singolo valore come MHC, MCHC etc etc"
    pass


def countAnalisiIstologica():
    analisiIstologiche: list[str] = leggereValori(r"C:\Users\zuzup\Desktop\cartelle\code\anemia\.progettino_informatica\Include\data\Anemia.csv")[3]
    counter: list[tuple(str, int)] = []
    for element in analisiIstologiche:
        value: int = analisiIstologiche.count(element)
        analisiIstologiche: list[str] = [analisi for analisi in analisiIstologiche if analisi != element]
        if value != 0: counter.append((element, value))
    return counter

def valoriOltreReference():
    # Analisi Corpuscolate represents the value "MCH", "MCHC", "MCV" in this order
    values = leggereValori(r"C:\Users\zuzup\Desktop\cartelle\code\anemia\.progettino_informatica\Include\data\Anemia.csv")
    valueAnalisiMolecolari: list[list[str]] = values[2] 
    valueEmoglobina = values[1]
    valueFerritina = values[6]
    valueInterval: list[list[tuple[str, str]]] = values[5]
    for index, element in enumerate(valueInterval): 
        valueAnalisiMolecolari[index].insert(0, valueEmoglobina[index]) # insert the emoglobina's value in the first index of array
        valueAnalisiMolecolari[index].append(valueFerritina[index]) # insert the ferritina's value in the last index of array

    matrixValue: list[list[str]] | list[list[tuple[str, float]]] | list[list[tuple[str, float], str]] = [] # Create the matrix that contains all values
    for i, elements in enumerate(valueAnalisiMolecolari):
        singleValue: list[str] = [] # Temporary variable
        for j, element in enumerate(elements):
            if float(element) < float(valueInterval[i][j][0]):
                singleValue.append(("Sotto intervallo", element))
            elif float(element) > float(valueInterval[i][j][1]):
                singleValue.append(("Sopra intervallo", element))
            else:
                singleValue.append("Dentro intervallo")    
        matrixValue.append(singleValue) # Create the full list, contain the single value of the interval 
    # * The matrix value confronts the values for the interval in this order:
    '''
        - Hemoglobin
        - MCH
        - MCHC
        - MCV
        - Ferritina
    '''
    return matrixValue

def tiziMalatiAnemiaConMalattia():
    "Restituisce le persone malate di anemia con il loro tipo di anemia"
    valoriOltreIntervallo = valoriOltreReference()
    sicknessValue: list = []
    for elements in valoriOltreIntervallo:
        temporaryValue: list = []
        for index, element in enumerate(elements):
            if type(element) == tuple:
                match index:
                    case 0:
                        # Emoglobina
                        if "Sotto" in element[0]:
                            print("Il paziente soffre di anemia")
                        else:
                            print("Il paziente soffre di policitemia vera")
                    case 1:
                        if "Sotto" in element[0]:
                            print("Il paziente soffre di ipocromia")
                        else:
                            print("Il paziente ha una malattia cronica")
                    case 2:
                        if "Sotto" in element[0]:
                            print("Il paziente soffre di ipocromia")
                        else:
                            print("Il paziente soffre di anasarca o iperlipidemia")
                    case 3: 
                        if "Sotto" in element[0]:
                            print("Il paziente soffre di microcitosi")
                        else:
                            print("Il paziente soffre di macrocitosi")
                    case 4:
                        if "Sotto" in element[0]:
                            print("Il paziente soffre di carenza di ferro")
                        else:
                            print("Il paziente soffre di sovraccarico di ferro, associato a emocromatosi ereditaria")



tiziMalatiAnemiaConMalattia()