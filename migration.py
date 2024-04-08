import csv

test = open("Test.csv", "r")

test = ''.join([i for i in test])

test = test.replace("api.spacesusa.com/api", "vapi-stg.spacesusa.com/voice-api")

x = open("output.csv", "w")

x.writelines(test)
x.close

