from tqdm import tqdm
import requests


def getFrequencyList():
	from os import getcwd
	xxx = getcwd()
	park_data_jan = open("./parkPlaceFinding/park_data/2016_01.csv", 'r')
	park_list_jan = park_data_jan.readlines()
	park_data_jan.close()

	address_list = []

	#gets list of all addresses
	for record in tqdm(park_list_jan):
		value_list = record.split(',')
		addFound = False
		for address in address_list:
			if (value_list[5] == address[0]):
				address[1] = address[1] + 1
				addFound = True
				break
		if (not addFound):
			address_list.append([value_list[5], 1])
				
	address_list.sort(key=lambda x: x[1])
	print(address_list)	
	return address_list
	
def getRisk(address):
	list = getFrequencyList()
	num_of_entries = 0
	list_of_vals = []
	for item in list:
		if (item[0] == address):
			num_of_entries = item[1]
		list_of_vals.append(item[1])
	if (num_of_entries == 0):
		return "Address not found"
	average = sum(list_of_vals) / (float(len(list_of_vals)))
	if (num_of_entries > (average * 1.5)):
		return "High Risk"
	elif (num_of_entries >= average):
		return "Increased Risk"
	elif (num_of_entries >= (average * 0.5)):
		return "Middle Risk"
	else:
		return "Low Risk"
		
		
#def main():
	#print(getRisk('"NEUSSER STR."'))
#	address = '"NEUSSER STR:"'
#	add_list = address.split(' ')
#	url_add = add_list[0]
#	for word in add_list[1:]:
#		url_add += "+"
#		url_add += word
#	number = 8
#	
#	url = "http://nominatim.openstreetmap.org/search?q=" + str(number) + "+" + url_add + ",köln&highway=road&near"
#	h1 = requests.get(url)
#	print(h1.text)
#	print(url)

#main()