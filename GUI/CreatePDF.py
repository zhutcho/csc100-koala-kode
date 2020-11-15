from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from database.CSC100DB import CSC100DB


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
                reportlab Vertical Bar Chart - bar chart with inputted values
        """

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

        return bc

    def getLGABarChart(self, month, year):
        """Gets a bar chart with Local Government Area data for the selected month
            Parameters:
                self: the class instance
                month: str - month required
                year: int - year required
            Returns:
                reportlab Drawing - bar chart with LGA data
        """

        dictionary = self.getDB().getMonthlyDataForLGA(str(month), year)
        x_values = self.getKeys(dictionary)
        y_values = self.getValues(dictionary)
        return self.getBarChart(x_values, y_values)

    def getTaxonsBarChart(self, month, year):
        """Gets a bar chart with Taxons Grouping data
            Parameters:
                self: the class instance
                month: str - month required
                year: int - year required
            Returns:
                reportlab Drawing - bar chart with Taxons Grouping data
        """

        dictionary = self.getDB().getMonthlyDataForTaxons(str(month), year)
        x_values = self.getKeys(dictionary)
        y_values = self.getValues(dictionary)
        return self.getBarChart(x_values, y_values)

    def drawingToPDF(self, shape, file):
        """Outputs drawing to selected pdf
            Parameters:
                self: the class instance
                shape: reportlab Shape - inserted into drawing for pdf
                file: str - filename and location, filename must end in .pdf
        """

        drawing = Drawing(400, 300)
        drawing.add(shape)
        renderPDF.drawToFile(drawing, file, 'Test Drawing')

    def createMonthlyReport(self, file):
        """Outputs the monthly report to the specified file location
            Parameters:
                self: the class instance
                file: str - filename and location, filename must end in .pdf
        """

        drawing = Drawing(800, 800)

        drawing.add(self.getLGABarChart('01', 2018))
        drawing.add(self.getTaxonsBarChart('01', 2018))

        renderPDF.drawToFile(drawing, file, 'Test Drawing')
