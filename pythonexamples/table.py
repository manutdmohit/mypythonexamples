from prettytable import PrettyTable
#Column Names Initialization
myTable= PrettyTable(["Student Name", "Class", "Section", "Percentage"])

#Adding Elements to Rows
myTable.add_row(["Ram","X","B","82.2%"])
myTable.add_row(["Sita","X","C","80.6%"])
myTable.add_row(["Hari","X","A","71.4%"])
myTable.add_row(["Baburao","B","B","75.8%"])
myTable.add_row(["Sandesh","X","A","81.5%"])
myTable.add_row(["Keshav","X","C","77.4%"])

print(myTable)