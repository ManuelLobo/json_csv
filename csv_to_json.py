import csv
import json

def csv_input(csvfile, jsonfile):
	with open(csvfile) as csv_file:
		rows = []
		read_csv = csv.DictReader(csv_file)
		fields = read_csv.fieldnames # fields
		for row in read_csv:
			rows.append({field:row[field] for field in fields})

		with open(jsonfile, "w") as json_file:
			json_file.write(json.dumps(rows, sort_keys=False, indent=4, separators=(',', ': '),
									    ensure_ascii=False)) #encoding="utf-8",

	return rows

csv_input("sample2.csv", "output.json")


# f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
