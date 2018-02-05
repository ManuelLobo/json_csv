import csv
import json

def json_input(jsonfile, csvfile):
	with open(jsonfile) as json_data:
		json_file = json.load(json_data)
		headers = [field for field in json_file[0]]
		csv_file = open(csvfile, "w")
		for field in headers:
			csv_file.write("{},".format(field))
		csv_file.write("\n")
		print(headers)
		for obj in json_file:
			for field in headers:
				csv_file.write("{},".format(obj[field]))
			csv_file.write("\n")

	csv_file.close()

json_input("sample_json.json", "output_csv.csv")

