from CreatePDF import CreatePDF


pdf = CreatePDF()

print(pdf.getDB())

print(pdf.getKeys(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

print(pdf.getValues(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

LGABarChart = pdf.getLGABarChart()
pdf.drawingToPDF(LGABarChart, 'LGABarChart.pdf')

taxonsBarChart = pdf.getTaxonsBarChart()
pdf.drawingToPDF(taxonsBarChart, 'TaxonsBarChart.pdf')

pdf.createPDF()
