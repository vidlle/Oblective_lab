def readfile (From,Confidence):
    File = open('DatabaseM.txt','r')
    
    i = 0
    length = 1
    datalines = []

    while i <= 132041:
        datalines += File.readlines(length)
        data_lines = datalines[i]

        fFrom = data_lines.find('From:')
        #result = data_lines.find('X-DSPAM-Result:')
        #proc = data_lines.find('X-DSPAM-Processed:')
        conf = data_lines.find('X-DSPAM-Confidence:')
        #prob = data_lines.find('X-DSPAM-Probability:')

        if fFrom == 0:
            From.append(data_lines)
        #if result == 0:
        #    Result.append(data_lines)
        #if proc == 0:
        #    Processed.append(data_lines)
        if conf == 0:
            Confidence.append(data_lines)
        #if prob == 0:
        #    Probability.append(data_lines)

        length += len(data_lines)
        i += 1
        
    File.close()
    SortConf(From,Confidence,SpamConf)

def SortConf(From,Confidence,SpamConf):
    i = 0
    cons = 0.8500
    for p in Confidence:
        div = p.split()
        answ = float(div[1])
        if cons < answ:
            SpamConf.append(From[i])
            i += 1
        else:
            i += 1
    print("Спам:",SpamConf)

From = []
#Result = []
#Processed = []
Confidence = []
#Probability = []

SpamConf = []
readfile(From,Confidence)


