from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.renderPDF import draw
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.units import cm, inch
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus.frames import Frame
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
                y_values: list of tuples - y values for the bar chart
            Returns:
                reportlab Vertical Bar Chart - bar chart with inputted values
        """

        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 100
        bc.height = 150
        bc.width = 350
        bc.data = y_values
        bc.strokeColor = colors.black

        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 275
        bc.valueAxis.valueStep = 25

        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 0
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 65
        bc.categoryAxis.categoryNames = x_values

        return bc

    def getPreviousMonths(self, month, year):
        """Gets a dictionary with the total accessions for the trailing twelve months
            Parameters:
                self: the class instance
                month: str - month required
                year: int - year required
            Returns:
                dict - month year as key with total accessions for that month as value
        """

        previous_months = {}
        month = int(month)
        year = year
        for months in range(12):
            if month > 10:
                str_month = str(month)
            else:
                str_month = "0" + str(month)
                print(str_month)
            month_list = self.getDB().getSpecificMonth(str_month, year)
            print(month_list)
            key = str(month_list[0])
            value = int(month_list[1])
            print(key)
            print(value)
            previous_months[key] = value
            if month != 1:
                month -= 1
            else:
                month = 12
                year -= 1
        return previous_months

    def getSpecificBarChart(self, type, month, year):
        """Gets a bar chart with accessions grouped by either Local Government Area, 
        Taxons Grouping, Trailing Twelve Months or the Same Month in Previous Years
            Parameters:
                self: the class instance
                type: str - choose from LGA, Taxons, Twelve or Prev
                month: str - month required
                year: int - year required
            Returns:
                reportlab Drawing - bar chart with data grouped as specified
        """

        dictionary = {}
        if type == "LGA":
            dictionary = self.getDB().getMonthlyDataForLGA(str(month), year)
        elif type == "Taxons":
            dictionary = self.getDB().getMonthlyDataForTaxons(str(month), year)
        elif type == "Twelve":
            dictionary = getPreviousMonths(str(month), year)
        elif type == "Prev":
            pass
        else:
            dictionary = {"Incorrect Entry": 100}
        x_values = self.getKeys(dictionary)
        y_values = [tuple(self.getValues(dictionary))]
        return self.getBarChart(x_values, y_values)

    def getSameMonthsBarChart(self, month, year):
        """Gets a bar chart with the same month in previous years' totals
            Parameters:
                self: the class instance
                month: str - month required
                year: int - year required
            Returns:
                reportlab Drawing - bar chart with the same month in previous years' totals
        """

        # Use something
        pass

    def drawingToPDF(self, flowable, file):
        """Outputs drawing to selected pdf - testing method
            Parameters:
                self: the class instance
                flowable: reportlab Shape - inserted into drawing for pdf
                file: str - filename and location, filename must end in .pdf
        """

        drawing = Drawing(400, 300)
        drawing.add(flowable)
        renderPDF.drawToFile(drawing, file, 'Test Drawing')

    def getMonthlyReport(self, file, month, year):
        """Outputs the monthly report to the specified file location
            Parameters:
                self: the class instance
                file: str - file location and name ending in .pdf
                month: str - required month
                year: int - required year
        """

        label_lga = Label()
        label_lga.setOrigin(180, 20)
        label_lga.boxAnchor = 'ne'
        label_lga.dx = 0
        label_lga.dy = -20
        label_lga.setText("Local Government Area Totals")

        draw_label_lga = Drawing(0, 40)
        draw_label_lga.add(label_lga)

        draw_lga = Drawing(0, 270)
        draw_lga.add(self.getSpecificBarChart("LGA", month, year))

        label_taxons = Label()
        label_taxons.setOrigin(180, 20)
        label_taxons.boxAnchor = 'ne'
        label_taxons.dx = 0
        label_taxons.dy = -20
        label_taxons.setText("Taxon Grouping Totals")

        draw_label_taxons = Drawing(0, 40)
        draw_label_taxons.add(label_taxons)

        draw_taxons = Drawing(0, 270)
        draw_taxons.add(self.getSpecificBarChart("Taxons", month, year))

        drawlist = [draw_label_lga, draw_lga, draw_label_taxons, draw_taxons]

        canvas = Canvas(file)

        frame = Frame(inch, 0, 15.92*cm, 29.7*cm, showBoundary=1)

        frame.drawBoundary(canvas)
        frame.addFromList(drawlist, canvas)

        canvas.save()
