from unitTestFramework.utils.excelUtils import readExcelData

data = readExcelData()
testingData = data.readDateAsList(2)
print(testingData[0])

testingData2 = data.readDateAsDict(2)
print(testingData2)
print(testingData2.get("Name"))
print(testingData2.get("Address"))
print(testingData2.get("PostCode"))