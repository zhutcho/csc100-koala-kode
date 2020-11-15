from CreatePDF import CreatePDF


pdf = CreatePDF()

print(pdf.getDB())

print(pdf.getKeys(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

print(pdf.getValues(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

lga_bar_chart = pdf.getLGABarChart('01', 2018)
pdf.drawingToPDF(lga_bar_chart, 'app/tests/test_lgabc.pdf')

taxons_bar_chart = pdf.getTaxonsBarChart('01', 2018)
pdf.drawingToPDF(taxons_bar_chart, 'app/tests/test_taxonsbc.pdf')

pdf.getMonthlyReport('app/tests/test_monthlyreport.pdf', '01', 2018)
