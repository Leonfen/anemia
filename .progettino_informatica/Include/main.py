import csv
import os
import matplotlib.pyplot as plt

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
    valueEmoglobina: list[str] = values[1]
    valueFerritina: list[str] = values[6]
    valueInterval: list[list[tuple[str, str]]] = values[5]
    for index, element in enumerate(valueInterval): 
        valueAnalisiMolecolari[index].insert(0, valueEmoglobina[index]) # insert the emoglobina's value in the first index of array
        valueAnalisiMolecolari[index].append(valueFerritina[index]) # insert the ferritina's value in the last index of array

    matrixValue: list[list[str]] | list[list[tuple[str, float]]] | list[list[tuple[str, float], str]] = [] # Create the matrix that contains all values
    for i, elements in enumerate(valueAnalisiMolecolari):
        singleValue: list[str] = [values[0][i]] # Temporary variable
        for j, element in enumerate(elements):
            intervalloSuperiore: float = float(valueInterval[i][j][1])
            intervalloInferiore: float = float(valueInterval[i][j][0])
            if float(element) < intervalloInferiore:
                singleValue.append(("Sotto intervallo", element, intervalloInferiore))
            elif float(element) > intervalloSuperiore:
                singleValue.append(("Sopra intervallo", element, intervalloSuperiore))
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
    with open(r"C:\Users\zuzup\Desktop\cartelle\code\anemia\.progettino_informatica\Include\output\valoriOltreIntervallo.csv", "w") as outfile:
        csvWriter = csv.writer(outfile, lineterminator='\n')

        # Add the list of column headers to the csv file.
        headers = ["Nome", "Emoglobina", "MCH", "MCHC", "MCV", "Ferritina"]
        csvWriter.writerow(headers)
        for index, row in enumerate(matrixValue):
            # Emoglobina
            emoglobina: str = row[1]
            if type(emoglobina) == tuple: emoglobina = f"L'emoglobina {emoglobina[0].lower()}; lower bound: {emoglobina[1]}; upper bound {emoglobina[2]}"
            # MCH
            MCH: str = row[2]
            if type(MCH) == tuple: MCH = f"L'MCH {MCH[0].lower()}; lower bound: {MCH[1]}; upper bound {MCH[2]}"
            # MCHC
            MCHC: str = row[3]
            if type(MCHC) == tuple: MCHC = f"L'MCHC {MCHC[0].lower()}; lower bound: {MCHC[1]}; upper bound {MCHC[2]}"
            # MCV
            MCV: str = row[4]
            if type(MCV) == tuple: MCV = f"L'emoglobina {MCV[0].lower()}; lower bound: {MCV[1]}; upper bound {MCV[2]}"
            # Ferritina
            ferritina: str = row[5]
            if type(ferritina) == tuple: ferritina = f"La ferritina {ferritina[0].lower()}; lower bound: {ferritina[1]}; upper bound {ferritina[2]}"

            csvWriter.writerow([matrixValue[index][0], emoglobina, MCH, MCHC, MCV, ferritina])

    return matrixValue


def checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, prefix, cause, sintomo = None):
    if (not sintomo in sintomi) and (not sintomo is None): sintomi.append(sintomo)
    for element in cause:
        if not element in probabiliCause:
            probabiliCause.append(element)
    valoriOltre.append((prefix, value))
    return ((probabiliCause, sintomi, valoriOltre))

def checkingValue(elements):
    "Check if the value is above or less the limit interval, return the illnesses of the patient"
    "It will return matrix created with:"
    '''
        - Sintomi, lista di stringhe
        - Cause, lista di stringhe
        - Valori oltre la soglia, tuple con prefisso e valore oltre la soglia del 10%
    '''
    sintomi: list[str] = []
    probabiliCause: list[str] = []
    valoriOltre: list[tuple[str, float]] = []
    

    for index, element in enumerate(elements):
        if type(element) != tuple: continue # The element is not a interval, continues to the next element
        intervalValue = float(element[2]) # take the regular interval of the element
        value = float(element[1]) # take the external value
        if type(element) == tuple:
            if index == 0: # Checking hemoglobin
                if (value < (intervalValue - (intervalValue / 10))):
                    probabiliCause.extend(['carenza di ferro', 'carenza di vitamina B12', 'carenza di folati', 'anemia emolitica', 'talassemia', 'malattie croniche']) # Using extend to insert multiple values in the main array
                    sintomi.append('anemia')
                    valoriOltre.append(('Emoglobina', value))

                if (value > (intervalValue + (intervalValue / 10))):
                    probabiliCause.extend(['policitemia vera', 'malattia di poliglobulia'])
                    valoriOltre.append(('Emoglobina', value))

            if index == 1: # Cheking MCH
                if (value < (intervalValue - (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCH', ['carenza di ferro', 'talassemia', 'anemia sideroblastica'], 'ipocromia')
                if (value > (intervalValue + (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCH', ['anemia perniciosa', 'malattie croniche'])

            if index == 2: # Cheking MCHC
                if (value < (intervalValue - (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCHC', ['carenza di ferro', 'talassemia', 'anemia sideroblastica'], 'ipocromia')
                if (value > (intervalValue + (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCHC', ['anasarca', 'iperlipidemia', 'ittero'], 'ipocromia')

            if index == 3: # Checking MCV
                if (value < (intervalValue - (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCV', ['carenza di ferro', 'talassemia', 'anemia sideroblastica'], 'microcitosi')                    
                if (value > (intervalValue + (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'MCV', ['carenza di vitamina B12', 'carenza di folati', 'alcolismo', 'problemi del midollo osseo'], 'macrocitosi')                    

            if index == 4: # Ferritina
                if (value < (intervalValue - (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'Ferritina', ['carenza di ferro'], 'anemia')                                    
                if (value > (intervalValue + (intervalValue / 10))):
                    probabiliCause, sintomi, valoriOltre = checkingSingleValue(probabiliCause, sintomi, valoriOltre, value, 'Ferritina', ['emocromatosi ereditaria', 'eccessivo accumulo di ferro'], 'sovraccarico di ferro')                                    

    if (len(sintomi) != 0 and len(probabiliCause) != 0 and len(valoriOltre) != 0): 
        return [sintomi, probabiliCause, valoriOltre]

    

    
def tiziMalatiAnemiaConMalattia():
    "Restituisce le persone malate di anemia con il loro tipo di anemia"
    valoriOltreIntervallo = valoriOltreReference()
    for index, elements in enumerate(valoriOltreIntervallo):
        valore = checkingValue(elements)
        if valore != None:
            with open(r"C:\Users\zuzup\Desktop\cartelle\code\anemia\.progettino_informatica\Include\output\valoriOltreIntervallo.csv", "w") as outfile:
                csvWriter = csv.writer(outfile, lineterminator='\n')
                # Add the list of column headers to the csv file.
                headers = ["Nome", "Sintomi", "Cause e malattie", "Valori oltre reference"]
                csvWriter.writerow(headers)
                nome: str = elements[0]
                sintomi: str = ", ".join(valore[0])
                cause_malattie: str = ", ".join(valore[1])
                valoriReference: list[str] = []
                for value in valore[2]:
                    valoriReference.append(f"{value[0]} = {value[1]}")
                valoriReference = ", ".join(valoriReference)
                csvWriter.writerow([nome, sintomi, cause_malattie, valoriReference])
            

def istogrammaAnalisiIstologiche():
    values = countAnalisiIstologica()
    # Estrarre le etichette sull'asse x
    labels = [item[0] for item in values]
    # Estrarre i valori sull'asse y
    values = [item[1] for item in values]
    # Creare il grafico a istogrammi
    plt.bar(labels, values)
    # Aggiungere una descrizione all'asse x
    plt.xlabel('Tipo di cellula')
    # Aggiungere una descrizione all'asse y
    plt.ylabel('Conteggio')
    # Aggiungere un titolo al grafico
    plt.title('Istogramma delle cellule')
    # Mostrare il grafico
    plt.show()

tiziMalatiAnemiaConMalattia()