#############################################
#
# Calculates how much meat we should order from our caterer based on people's preferences,
# which were submitted via a google form and saved as a CSV
#
#############################################

# Import required libraries
import pandas as pd

# Import the csv as a pandas dataframe
df = pd.read_csv('./db/meat.csv')

# Create a dictionary containing every entree item so we can store the counts
meatOrder = {}

# The wedding is a self-serve bbq, and people can select multiple items, so we need to
# separate and properly weight each choice
for index, row in df.iterrows():
	# Check if there is a comma in the choice, which will indicate multiple choices
	choices = row['entree'].split(', ')
	numChoices = len(choices)
	
	# Loop through choices and add to dictionary
	for choice in choices:
		if meatOrder.has_key(choice):
			meatOrder[choice] += (1/float(numChoices))
		else: 
			meatOrder[choice] = (1/float(numChoices))





		
