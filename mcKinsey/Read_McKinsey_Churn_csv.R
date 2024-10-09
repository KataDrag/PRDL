########################################
# Reading McKinsey Bank Churn data in csv file
#
#

# Clear the working space
rm(list=ls())

Input_file <- "bankingchurn_data_modif.csv"

Data_Directory <- "D:\\McKinsey\\"

Filename_with_Dir <- paste(Data_Directory, Input_file, sep = "")

data <- read.csv(Filename_with_Dir, sep =";")

class(data)

lapply(data,class)

# convert columns to date class
data$contract_start <- as.Date(data$contract_start)
data$date_of_birth <- as.Date(data$date_of_birth)

# contract_end has EMPTY CELLS that could be those
# users that do not quit!
# ... you could use this to create an outcome column data$churm

data$churn <- data$contract_end != ""

# Now you can imagine how to create features (feature engineering)
