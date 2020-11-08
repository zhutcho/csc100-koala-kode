import mysql.connector
import csv

__author__="Erica Mealy - Course Coordinator, CSC100, 2020."

class CSC100DB():
    """Database API for CSC100's Australia Zoo Wildlife Hospital
     Database UI project

    """
    # The database connection
    conn = None
    # the cursor for the database - way to execute statements
    cursor = None

    def __init__(self):
        """ Database API constructor 
        -- NOTE change values here if using password or differently named schema --
        """
        super(CSC100DB, self).__init__()
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="csc100",
                database="azwh"
            )
            self.cursor = self.conn.cursor()
            
        except Exception as e:
            print("Error:",e)
        
    def __del__(self):
        # Destructor is called as the reference to the class is deleted to do clean up
        if not self.cursor is None:
            self.cursor.close()
            self.conn.close()


    def callMonthlyProc(self, procedurename, month, year):
        """Private method for the collection of monthly report methods 
            Parameters:
                self: the class instance it's called on
                procedurename: string - the name of the database stored procedure to call
                month: string - the month that is being searched for as 'MM' - e.g. March as '03'
                year: int - the year that is being searched for in YYYY format - e.g. 2018     
            Returns:
                dictionary with mappings from the text value to the count for the requested month, year

        """
        try:
            outputs = {}
            args = [month,year]
            result_args = self.cursor.callproc(procedurename, args)
            # process the result
            for result in self.cursor.stored_results():
                for r in result:
                    outputs[r[0]] = r[1]
            return outputs
        except Exception as e:
            return "Error:" + e.message

    def getMonthlyDataForTaxons(self, month, year):
        """Function to get the taxon grouping totals for a supplied month, year  
            Parameters:
                self: the class instance it's called on
                month: string - the month that is being searched for as 'MM' - e.g. March as '03'
                year: int - the year that is being searched for in YYYY format - e.g. 2018     
            Returns:
                dictionary with mappings from each taxon to it's count for the requested month, year

        """
        return self.callMonthlyProc("monthly_by_type", month, year)

    def getMonthlyDataForLGA(self, month, year):
        """Function to get the Local Government Area totals for a supplied month, year  
            Parameters:
                self: the class instance it's called on
                month: string - the month that is being searched for as 'MM' - e.g. March as '03'
                year: int - the year that is being searched for in YYYY format - e.g. 2018     
            Returns:
                dictionary with mappings from each LGA to it's count for the requested month, year

        """
        return self.callMonthlyProc("monthly_by_juris", month, year)

        
    def previousMonths(self, month, year):
        """Function to get the total accessions for the previous 12 months from a supplied month, year  
            Parameters:
                self: the class instance it's called on
                month: string - the month that is being searched for as 'MM' - e.g. March as '03'
                year: int - the year that is being searched for in YYYY format - e.g. 2018     
            Returns:
                dictionary with mappings from month, year pair in the period to it's 
                count for the 12 months prior to the supplied month, year

        """
        try:
            prevMonths = []
            args = [month,year]
            months = ["Jan", "Feb", "Mar", "Apr", "May", "June", 
                "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
            result_args = self.cursor.callproc("monthly_prev_months", args)
            for result in self.cursor.stored_results():
                for r in result:
                    prevMonths.append([months[r[0]-1]+ " " +str(r[1]),str(r[2])])

        except Exception as e:
            return "Error:" + e

    def getSpeciesIds(self):
        """ Gets the lists of species names mapped to their database ID
            Returns:
                dictionary of species, id pairs.

        """
        species = {}
        result_args = self.cursor.callproc("get_all_species")
        # process the result
        for result in self.cursor.stored_results():
            for r in result:
                #print(r)
                species[r[1]] = r[0]

        return species


    def getSuburbsInfo(self):
        """ 
            Retrieves the information on suburbs and local government areas.

            Returns:
                Two lists:
                - the first a dictionary of suburb names mapped to their id
                - the second a dictionary contains a mapping of suburb id to local govt area id.
        """
        suburbIds = {}
        suburbJurisdictions = {}
        result_args = self.cursor.callproc("get_all_suburb")
        # process the result
        for result in self.cursor.stored_results():
            for r in result:
                suburbName = r[1]
                suburbId = r[0]
                jurisId = r[3]

                suburbIds[suburbName] = suburbId
                suburbJurisdictions[suburbId] = jurisId

        return suburbIds, suburbJurisdictions


    def createAccession(self, rescuer_id, species_id, animal_name, 
        date_admitted, time_admitted, admitter_signoff, can_call, 
        registered_carer, interested_in_becoming, rescue_suburb_id, 
        rescue_juris_id, rescue_situation, rescue_reason, time_in_capt,
        fed_medicated, fed_what, fed_when, affliction = ""):
        """ Inserts into the database a new patient and accession.

        Pre-conditions:
            Rescuer must exist in database and have valid rescuer id
            suburb and local government area must exist in database and have valid id
            Species id must correspond to a valid id of the animal's species

        Parameters:
            self: the instance of the database this was called on, 
            rescuer_id: of the previously added contact (use addOrGetRescuerID(..) to obtain, 
            species_id: int matched to the species of the animal, 
            animal_name: string - the name the admitter is giving the animal, 
            date_admitted: date - in format 'YYYY-MM-DD', e.g. 2020-10-19, 
            time_admitted: time - in format 'HH:mm:ss', 
            admitter_signoff 'Y' or 'N' - if the Admitter has waived rights to the animal, 
            can_call 'Y' or 'N' - if the hospital can call the rescuer to return the animal once healed, 
            registered_carer 'Y' or 'N' - if the rescuer is a wildlife carer with a registere organisation, 
            interested_in_becoming: 'Y' or 'N' - if the rescuer is interested in becoming a wildlife carer, 
            rescue_suburb_id: int - id of the suburb the animal was rescued in, 
            rescue_juris_id: int - the database id of the local government area the animal was rescued in, 
            rescue_situation: string - the check boxes from the form, e.g. On Ground etc, 
            rescue_reason: string - form field "What do you feel happened to this animal?",
            time_in_capt: string - how long the animal was with the rescuer before being brought in,
            fed_medicated: 'Y' or 'N' - if the animal has been given any food, water or medicine, 
            fed_what: string - what the animal was fed if any, 
            fed_when: string - when the animal was fed, 
            affliction - cause of affliction if known- defaults to empty


        Returns:
            string: Accession number if successful.
            string: error message if not successful.

        """
        accessionNumber = None
        args = [rescuer_id, species_id, animal_name, 
        date_admitted, time_admitted, admitter_signoff, can_call, 
        registered_carer, interested_in_becoming, rescue_suburb_id, 
        rescue_juris_id, rescue_situation, rescue_reason, time_in_capt,
        fed_medicated, fed_what, fed_when, affliction]
        try:
            result_args = self.cursor.callproc("create_accession", args)
            # process the result
            for result in self.cursor.stored_results():
                for r in result:
                    # this should be the accession number if success
                    accessionNumber = r[0]
                    #else error message caught
            self.conn.commit()
            return accessionNumber
        except Exception as e:
            return "Error:" + e.message

    def AddOrGetRescuerId(self, firstname, lastname, title, phone, 
        mobile, email, address, suburbId):
        """ 
            Retrieves the id of a contact, adding them to the database if they aren't already part.

            Parameters:
                firstname: string - the rescuer's first name
                lastname: string - the rescuer's last name
                title: string - the title to address the rescuer with
                phone: string - the rescuer's phone number (note String because leading zeros!)
                mobile: string - the rescuer's mobile number (string for leading zeros)
                email: string - the rescuer's email address
                address: string - the number and street part of the rescuer's address
                suburbId: int - the database Id of the suburb the rescuer lives in

            Returns:
                The ID of the rescuer being looked for.

        """
        rescuerID = None
        args = [firstname, lastname, title, phone, 
        mobile, email, address, suburbId]
        try:
            result_args = self.cursor.callproc("add_or_get_rescuer", args)
            # process the result
            for result in self.cursor.stored_results():
                for r in result:
                    # this should be the rescuer's id number if success
                    rescuerID =  r[0]
                    #else error message caught
            self.conn.commit()
            return rescuerID
        except Exception as e:
            return "Error:" + e.message




