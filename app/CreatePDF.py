from reportlab.graphics.charts.textlabels import Label, LabelOffset
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

        # Setting up sizing, position and colourings
        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 100
        bc.height = 150
        bc.width = 350
        bc.strokeColor = colors.black

        # Setting up axis
        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 300
        bc.valueAxis.valueStep = 25

        # Setting up position and angle of labels
        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 0
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 65

        # Adding bar labels
        bc.barLabelFormat = '%s'
        bc.barLabels.nudge = 5
        bc.barLabels.boxAnchor = 's'
        bc.barLabels.dy = -1

        # Changing bar colours
        bc.bars[0].fillColor = colors.green

        # Adding x and y data to the chart
        bc.categoryAxis.categoryNames = x_values
        bc.data = y_values

        return bc

    def getSpecificBarChart(self, type, month, year):
        """Gets a bar chart with accessions grouped by either Local Government Area or Taxons
            Parameters:
                self: the class instance
                type: str - choose from LGA or Taxons
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
        else:
            dictionary = {"Incorrect Entry": 100}
        x_values = self.getKeys(dictionary)
        y_values = [tuple(self.getValues(dictionary))]
        return self.getBarChart(x_values, y_values)

    def drawingToPDF(self, flowable, file):
        """Outputs drawing to selected pdf - testing method
            Parameters:
                self: the class instance
                flowable: reportlab Flowable - inserted into drawing for pdf
                file: str - filename and location, filename must end in .pdf
        """

        drawing = Drawing(400, 300)
        drawing.add(flowable)
        renderPDF.drawToFile(drawing, file, 'Test Drawing')

    def exportMonthlyReport(self, file, month, year):
        """Outputs the monthly report to the specified file location
            Parameters:
                self: the class instance
                file: str - file location and name ending in .pdf
                month: str - required month
                year: int - required year
        """

        # For conversion of month to three letter abbreviation
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Creating a title
        title = Label()
        title.setOrigin(300, 20)
        title.boxAnchor = 'ne'
        title.dx = 0
        title.dy = -5
        title.fontSize = 30
        title.setText("Monthly Report")

        # Adding title to a drawing
        draw_title = Drawing(0, 40)
        draw_title.add(title)

        # Creating a subtitle
        subtitle = Label()
        subtitle.setOrigin(320, 20)
        subtitle.boxAnchor = 'ne'
        subtitle.dx = 0
        subtitle.dy = -10
        subtitle.fontSize = 14

        # Converts month to three letter abbreviation
        str_month = months[int(month)-1]

        # Setting the subtitle's text
        subtitle.setText("Australia Zoo Wildlife Hospital, " +
                         str_month + " " + str(year))

        # Adding subtitle to a drawing
        draw_subtitle = Drawing(0, 30)
        draw_subtitle.add(subtitle)

        # Creating a label for the first chart
        label_lga = Label()
        label_lga.setOrigin(180, 20)
        label_lga.boxAnchor = 'ne'
        label_lga.dx = 0
        label_lga.dy = -20
        label_lga.setText("Local Government Area Totals")

        # Adding label to a drawing
        draw_label_lga = Drawing(0, 40)
        draw_label_lga.add(label_lga)

        # Creating drawing for the lga chart
        draw_lga = Drawing(0, 270)
        draw_lga.add(self.getSpecificBarChart("LGA", month, year))

        # Creating a label for the second chart
        label_taxons = Label()
        label_taxons.setOrigin(180, 20)
        label_taxons.boxAnchor = 'ne'
        label_taxons.dx = 0
        label_taxons.dy = -20
        label_taxons.setText("Taxon Grouping Totals")

        # Adding label to a drawing
        draw_label_taxons = Drawing(0, 40)
        draw_label_taxons.add(label_taxons)

        # Creating drawing for the taxons chart
        draw_taxons = Drawing(0, 270)
        draw_taxons.add(self.getSpecificBarChart("Taxons", month, year))

        # List of drawings in order of how to place them in the canvas
        drawlist = [draw_title, draw_subtitle, draw_label_lga, draw_lga,
                    draw_label_taxons, draw_taxons]

        # Creating a canvas (pdf file) and saving it to a location
        canvas = Canvas(file)

        # Creating a frame to add flowables (drawings) to
        frame = Frame(inch, 0, 15.92*cm, 29.7*cm)

        # Adding flowables
        frame.addFromList(drawlist, canvas)

        # Saving the pdf
        canvas.save()
