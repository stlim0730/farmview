# A string matching script to classify ownership as public and private

# Current problems: #here is a problem with the 'SCHOOL' substring .. there both public and private schools. 
# There is a problem with USA .. needs to be an exact match as andy SUSAN is getting the public title
# Need to add this :  coast$`detailed_ownership_type` <- ifelse(coast$public/private == "no_data", 'no_data', '')

# Read data and add two columns, make sure data is in R directory

coast <- read.csv('/Users/bofanchen1/Desktop/central_coast.csv', header = TRUE)
coast['detailed_ownership_type'] <- ''
coast['public/private'] <- ''


# verify rows
nrow(coast)
sum(coast$owner != '')
sum(coast$detailed_ownership_type != '')

### give null values no data value ###
coast$`public/private` <- ifelse(coast$owner == "", 'no_data', '')



# Classify all rows into no_data, public and private
coast$`public/private`[grepl('STATE OF CALIFORNIA|CALIFORNIA STATE OF|\\bCITY\\b|\\bCOUNTY\\b|OPEN SPACE|MIDPENINSULA REGIONAL OPEN SPA', coast$owner)] <-'public'
coast$`public/private`[grepl('U S A|\\bUSA\\b|United States of America', coast$owner)] <- 'public'
coast$`public/private`[grepl('UNIVERSITY OF CALIFORNIA|REGENTS|STATE PARK|SCHOOL|WATER DISTRICT|FLOOD DISTRICT|DISTRICT|STATE PRISON|REGIONAL PARK', coast$owner)] <- 'public'
coast$`public/private`[grepl('OF SANTA CRUZ|MONTEREY|SAN BENITO', coast$owner)] <- 'public'
coast$`public/private`[coast$owner == ''] <- 'no_data'
coast$`public/private`[coast$`public/private` == ''] <- 'private'

#Rearrange the order of the following according to the hierarchy
# The category with a higher hierarchy is placed lower, because the lower string functions will replace the previous entry

#Give more detail to ownership type
coast$detailed_ownership_type[grepl('ETAL|ET AL', coast$owner)] <- 'individual_etal'
coast$detailed_ownership_type[grepl('\\bASS\\b|ASSOC|ASSOCIATION', coast$owner)] <- 'association'
coast$detailed_ownership_type[grepl('FOUNDATION', coast$owner)] <- 'foundation'
coast$detailed_ownership_type[grepl('TRUST|\\bTRS\\b|\\bTRUS\\b|\\bTR\\b|\\bTRU\\b', coast$owner)] <- 'trust_individual'
coast$detailed_ownership_type[grepl('FAMILY TRUST', coast$owner)] <- 'trust_family'
coast$detailed_ownership_type[grepl('STATE OF CALIFORNIA|CALIFORNIA STATE OF|\\bCITY\\b|\\bCOUNTY\\b|OPEN SPACE', coast$owner)] <-'public_state'
coast$detailed_ownership_type[grepl('U S A', coast$owner)] <- 'public_federal'
coast$detailed_ownership_type[grepl('COMPANY|RANCH|RAILROAD|CORP|\\bINC\\b|\\bCO\\b|\\bLP\\b|VINEYARD|PROPERTIES', coast$owner)] <- 'company'
coast$detailed_ownership_type[grepl('REGENTS|SCHOOL|WATER DISTRICT', coast$owner)] <- 'public_institution'
coast$detailed_ownership_type[grepl('LLC', coast$owner)] <- 'LLC_commercial'
coast$detailed_ownership_type[grepl('\\/', coast$owner)] <- 'individual_plus'
coast$detailed_ownership_type[coast$owner == ''] <- 'no_data'

write.csv(coast, file = '/Users/bofanchen1/Desktop/categorized.csv')

sample(coast$owner[coast$detailed_ownership_type == '' ], 100)

