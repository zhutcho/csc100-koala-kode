from gui.CreatePDF import CreatePDF
import sys


sys.path.config(1, '../gui')

pdf = CreatePDF()

print(pdf.getDB())

print(pdf.getKeys(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

print(pdf.getValues(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))

LGABarChart = pdf.getLGABarChart()
pdf.drawingToPDF(LGABarChart, 'test_reports/test_lgabc.pdf')

taxonsBarChart = pdf.getTaxonsBarChart()
pdf.drawingToPDF(taxonsBarChart, 'test_reports/test_taxonsbc.pdf')

pdf.createMonthlyReport('test_reports/test_monthlyreport')
