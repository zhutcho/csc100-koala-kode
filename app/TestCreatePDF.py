from CreatePDF import CreatePDF


# Creating an instance of CreatePDF for testing purposes
pdf = CreatePDF()
print("------------------------------------")

# Prints database object
print("Database Object")
print(pdf.getDB())
print("------------------------------------")

# Prints keys of a given list
print("Keys for Taxons Dictionary")
print(pdf.getKeys(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))
print("------------------------------------")

# Prints values  of a given list
print("Values for Taxons Dictionary")
print(pdf.getValues(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))
print("------------------------------------")

# Exporting lga chart to a test pdf file
print("Exported LGA Chart to a PDF")
lga_bar_chart = pdf.getSpecificBarChart("LGA", '01', 2018)
pdf.drawingToPDF(lga_bar_chart, 'app/tests/test_lgabc.pdf')
print("------------------------------------")

# Export taxons chart to a test pdf file
print("Exported Taxons Chart to a PDF")
taxons_bar_chart = pdf.getSpecificBarChart("Taxons", '01', 2018)
pdf.drawingToPDF(taxons_bar_chart, 'app/tests/test_taxonsbc.pdf')
print("------------------------------------")

# Exports a test monthly report to a pdf
print("Exported Test Monthly Report to a PDF")
pdf.getMonthlyReport('app/tests/test_monthlyreport.pdf', '01', 2018)
print("------------------------------------")
