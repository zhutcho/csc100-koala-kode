from CSC100DB import CSC100DB 

db = CSC100DB()

# UI Population queries.
species = db.getSpeciesIds()
print("Species: ")
#print(species)
print ("----------------------------------------")
suburbIDs, suburbToLGAIds = db.getSuburbsInfo()
print("Suburb name to ids:")
#print(suburbIDs)
print("Suburb ids to Lga:")
#print(suburbToLGAIds)
print ("----------------------------------------")

# Monthly report searches 

taxonData = db.getMonthlyDataForTaxons('01',2018)
print("Taxon data:")
print(taxonData)
print ("----------------------------------------")


LGAData = db.getMonthlyDataForLGA('01',2018)
print("local govt:")
print(LGAData)
print ("----------------------------------------")

twelveMonthData = db.previousMonths('01',2018)
print("12 months previous:")
print(twelveMonthData)
print ("----------------------------------------")

# Recoring a new hospital admission - note you need the appropriate suburb, jurisdiction and species IDs.

rescueID = db.AddOrGetRescuerId('Erica', 'Mealy', 'Dr', '0754594484','0400123456', 'name@email.com', '1 Moreton Parade',1883)
print("rescuer")
print(rescueID)
print ("----------------------------------------")

accessID = db.createAccession(rescueID, 469, "dane's koala", '2020-10-19', '14:30', 'Y', 'Y', 'Y', 'Y',1847, \
	99,"On Ground", "Run in with a trolley", "1 hour",'N','','','BIG HEADACHE!')
print("Accession Id: ")
print(accessID)
print ("----------------------------------------")
