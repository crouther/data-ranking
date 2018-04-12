import csv

#Variables
errorMessage = []
uniqueReasons = []
occurrence = []
uniqueOccurrence = []
column = 1

#Opens File
with open('customerio_sample_data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    #Scans through CSV file
    for row in csvReader:

        #Isolates Reasons from CSV file
        errorMessage.append(row[column])

    #Sets a new unique error message list
    uniqueReasons = list(set(errorMessage))

    #Counts occurrences of error messages
    for x in range(len(uniqueReasons)):
        occurrence.append(errorMessage.count(uniqueReasons[x]))
        
    #Combine List after printing elements
    for y in range(len(uniqueReasons)):
        uniqueOccurrence.append((uniqueReasons[y],occurrence[y]))

    #Sorts List by error frequency
    uniqueOccurrence.sort(key = lambda z: z[1], reverse=True)

    #Prints Decsending error popularity list
    for z in range(10):
        print(uniqueOccurrence[z])
