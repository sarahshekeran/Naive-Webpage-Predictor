############################################################################################
##########################################STATISTICS########################################
############################################################################################

def statistics(actualClassList, predictedClassList):
    try:
        if len(actualClassList) != len(predictedClassList):
            raise ValueError('Error: actualCLassList and predictedClassList do not match.')

        global DClasses, DClasses_len;

        length = len(actualClassList);

        tpr = [0]*DClasses_len;
        tnr = [0]*DClasses_len;
        precision = [0]*DClasses_len;
        accuracy = [0]*DClasses_len;

        confusionMatrix = [[copy.deepcopy(0) for x in range(DClasses_len)] for y in range(DClasses_len)]

        for i in range(length):
            confusionMatrix[actualClassList[i]][predictedClassList[i]] +=1;

        # formatted confusion matrix
        tableCM = Texttable();
        printCM = copy.deepcopy(confusionMatrix);
        printCM.insert(0,DClasses)
        tableCM.add_rows(printCM)  
        print("***************************CONFUSION MATRIX***************************")  
        print(tableCM.draw())

        results = [[copy.deepcopy(0) for x in range(4)] for y in range(DClasses_len)]

        total = 0;
        for i in range(DClasses_len):
            tp = confusionMatrix[i][i]

            fn = 0
            fp = 0
            tn = 0
            for j in range(DClasses_len):
                total += confusionMatrix[i][j];
                if i!=j:
                    fn += confusionMatrix[i][j];
                    fp += confusionMatrix[j][i];
                    #tn += confusionMatrix[j][j]; 
                    
            for k in range(DClasses_len):
                if k!=i:
                    for l in range(DClasses_len):
                        if l!= i:
                           tn += confusionMatrix[k][l];  
                                               

            if tp!=0:
                results[i][0] = tp/(tp+fn);
                results[i][1] = tp/(tp+fp);
            else:
                results[i][0] = 0
                results[i][1] = 0

            if tn!=0:
                results[i][2] = tn/(tn+fp);
            else:
                results[i][2]

            results[i][3] = (tp+tn)/total;

        tableResults = Texttable();
        results.insert(0,["TP Rate", "Precision", "TN Rate", "Accuracy"])
        tableResults.add_rows(results)
        print("*******************************RESULTS*******************************")     
        print(tableResults.draw())
        print("*********************************************************************")


    except ValueError as e:
        print(e);
    else:
        pass
    finally:
        pass
    

############################################################################################
############################################TEST############################################
############################################################################################

def test():
    actualClassList = []
    predictedClassList = []

    base = "test/"
    for i in DClasses:
        dir = os.listdir(base + i)
        for file in dir:
            res = p.Probability(base + i + "/" + file)
            print("Tested: " + i + ": " + file)
            actualClassList.append(DClasses.index(i))
            predictedClassList.append(DClasses.index(res[0][0]))

    statistics(actualClassList,predictedClassList)

    # file = "test/Arts/Arts1.txt";
    # res = p.Probability(file)
    # print(file + ": " + str(res[0]))

    # base = "test/"
    # dir = os.listdir(base + 'Arts')
    # for file in dir:
    #     res = p.Probability(base + 'Arts' + "/" + file)
    #     print("Tested: " + i + ": " + file)
    #     actualClassList.append(DClasses.index('Arts'))
    #     predictedClassList.append(DClasses.index(res[0][0]))

    # statistics(actualClassList,predictedClassList)


############################################################################################
##########################################PREDICT###########################################
############################################################################################

def predict():

    site = input('Enter URL: ')

    result = getSiteContent(site)

    if result == '':
        print("%d. Failed to get content for %s" % (count, site))
               
    #create a file for each webpage
    with open('input.txt', 'wb') as temp_file:
        temp_file.write(result.encode('utf8'))

    base = 'input.txt'
    res = p.Probability(base)

    print("*******************************RESULTS*******************************")
    print("Tested: "+site)
    print("Category: "+ res[0][0])
    print("*********************************************************************")


############################################################################################
##########################################PREDICT###########################################
############################################################################################

def quit():
    print('main exiting');
    sys.exit(0)


############################################################################################
############################################MAIN############################################
############################################################################################


from naiveBayes import  Pool
import os
import re
import copy
import sys
from texttable import Texttable
import readcsvfile
import requests
from getsitecontent import getSiteContent


if __name__ == "__main__":

    DClasses = ["Arts",  "Business",  "Computers",  "Health",  "News", "Recreation",  "Sports"]
    DClasses_len = len(DClasses)

    base = "learn/"
    p = Pool()
    for i in DClasses:
        p.learn(base + i, i)

    menu = {0: test, 1: predict, 2: quit};

    while(1):

        for key in menu.keys():
            print(str(key)+". "+menu[key].__name__)

        choice = int(input('Enter Your Option: '))
        menu[choice]()


        


