from reportlab.graphics.charts.axes import XValueAxis
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from database.CSC100DB import CSC100DB
import sys


sys.path.config(1, '../database')


class CreatePDF():
    """Monthly Report PDF Generator for CSC100's Australia Zoo Wildlife Hospital"""

    def __init__(self):
        """Initializes class"""

        self.db = CSC100DB()

    def getDB(self):
        """Gets the Database API tool
            Returns:
                database api object
        """

        return self.db

    def getKeys(self, dictionary):
        """Gets the keys of a dictionary
            Parameters:
                self: the class instance
                dictionary: dict - any dictionary
            Returns:
                keys of the given dictionary in a list
        """

        return list(dictionary.keys())

    def getValues(self, dictionary):
        """Gets the values of a dictionary
            Parameters:
                self: the class instance
                dictionary: dict - any dictionary
            Returns:
                values of the given dictionary in a list
        """

        return list(dictionary.values())

    def getBarChart(self, x_values, y_values):
        """Gets a bar chart with the given values
            Parameters:
                self: the class instance
                x_values: list - x values for the bar chart
                y_values: list - y values for the bar chart
            Returns:
                reportlab Drawing - bar chart with inputted values
        """

        drawing = Drawing(400, 200)

        y_values = [tuple(y_values)]

        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 50
        bc.height = 125
        bc.width = 300
        bc.data = y_values
        bc.strokeColor = colors.black

        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 250
        bc.valueAxis.valueStep = 25

        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 8
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 45
        bc.categoryAxis.categoryNames = x_values

        drawing.add(bc)

        return drawing

    def getLGABarChart(self):
        """Gets a bar chart with Local Government Area data
            Returns:
                reportlab Drawing - bar chart with LGA data
        """
        dictionary = self.getDB().getMonthlyDataForLGA('01', 2018)
        x_values = self.getKeys(dictionary)
        y_values = self.getValues(dictionary)
        self.getBarChart(x_values, y_values)

    def getTaxonsBarChart(self):
        """Gets a bar chart with Taxons Grouping data
            Returns:
                reportlab Drawing - bar chart with Taxons Grouping data
        """
        dictionary = self.getDB().getMonthlyDataForTaxons('01', 2018)
        x_values = self.getKeys(dictionary)
        y_values = self.getValues(dictionary)
        self.getBarChart(x_values, y_values)

    def drawingToPDF(self, drawing, file):
        """Draws drawing to pdf
            Parameters:
                self: the class instance
                drawing: reportlab Drawing - drawing for pdf
                file: str - file to output to
        """
        renderPDF.drawToFile(drawing, file, 'Test Drawing')

    def createMonthlyReport(self, file):
        pass
