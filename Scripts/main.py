import csv
import os
import pandas as pd


def readCsv_2(name):  # returns an array with the elements of the csv file as rows, columns
    lines = []
    file = open(name, mode='r')
    for element in file:
        column = element.replace('"', '').rstrip().split(",")
        lines.append(column)
    file.close()
    return lines


def readCsv(name):
    lines = []
    file = pd.read_csv(name, encoding = 'utf8')
    head_f = file.columns.values.tolist()
    lines = [head_f] + file.values.astype(str).tolist()
    return lines


def readTxt(name):
    parse = dict()
    file = open(name, 'r')
    lines = file.read().split("\n")
    for line in lines:
        temp = line.split("\t")
        parse[(temp[1].rstrip().lstrip().upper(), temp[2].rstrip().lstrip())] = temp[0].rstrip().lstrip()
    file.close()
    return parse


def get_incident(data):
    parsed = []
    if data[0][0] == "DATA_YEAR":
        parsed = get_incident_v1(data)
    else:
        parsed = get_incident_v2(data)
    return parsed


def get_incident_v1(data):  # takes data in an array format and returns an array with the data ordered
    parsed = []
    for columns in data[1:]:
        # incident_id, agency_id, data_year, incident_date, incident_h
        parsed.append([columns[2], columns[1], columns[0], columns[6], columns[8]])
    return parsed


def get_incident_v2(data):
    parsed = []
    for columns in data[1:]:
        # incident_id, agency_id, data_year, incident_date, incident_h
        parsed.append([columns[1], columns[0], columns[6][:4], columns[6][:10], columns[8]])
    return parsed


def get_offender(data):
    parsed = dict()
    if data[0][0] == "DATA_YEAR":
        parsed = get_offender_v1(data)
    else:
        parsed = get_offender_v2(data)
    return parsed


def get_offender_v1(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, offender_id, age_num, sex_num, sex_code, race_id, ethnicity_id
        parsed[columns[2]] = [columns[1], columns[5], columns[6], columns[7], columns[8]]
    return parsed


def get_offender_v2(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, offender_id, age_num, sex_num, sex_code, race_id, ethnicity_id
        parsed[columns[1]] = [columns[0], columns[4], columns[5], columns[6], columns[7]]
    return parsed


def get_victim(data):
    parsed = dict()
    if data[0][0] == "DATA_YEAR":
        parsed = get_victim_v1(data)
    else:
        parsed = get_victim_v2(data)
    return parsed


def get_victim_v1(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, victim_id, age_num, sex_code, race_id, ethnicity_id
        parsed[columns[2]] = [columns[1], columns[9], (columns[10] if (columns[10] != '') else "U"), columns[11],
                              columns[12]]
    return parsed


def get_victim_v2(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, victim_id, age_num, sex_code, race_id, ethnicity_id
        parsed[columns[1]] = [columns[0], columns[8], (columns[9] if (columns[9] != '') else "U"), columns[10],
                              columns[11]]
    return parsed


def get_victim_offender_rel(data):
    parsed = dict()
    if data[0][0] == "DATA_YEAR":
        parsed = get_victim_offender_rel_v1(data)
    else:
        parsed = get_victim_offender_rel_v2(data)
    return parsed


def get_victim_offender_rel_v1(data):
    parsed = dict()
    for columns in data[1:]:
        # offender_id, relationship_id
        parsed[columns[2]] = columns[3]
    return parsed


def get_victim_offender_rel_v2(data):
    parsed = dict()
    for columns in data[1:]:
        # offender_id, relationship_id
        parsed[columns[1]] = columns[2]
    return parsed


def get_agency(data):
    parsed = dict()
    for columns in data[1:]:
        # agency_id, county_name, state_name
        parsed[columns[1]] = [columns[54], columns[17]]
    return parsed


def get_cde_agency(data):
    parsed = dict()
    for columns in data[1:]:
        # agency_id, county_name, state_name
        parsed[columns[0]] = [columns[14], columns[20]]
    return parsed


def get_offense(data):
    parsed = dict()
    if data[0][0] == "DATA_YEAR":
        parsed = get_offense_v1(data)
    else:
        parsed = get_offense_v2(data)
    return parsed


def get_offense_v1(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, offense_type_id
        parsed[columns[2]] = columns[3]
    return parsed


def get_offense_v2(data):
    parsed = dict()
    for columns in data[1:]:
        # incident_id, offense_type_id
        parsed[columns[1]] = columns[2]
    return parsed


def parse_offender(array, data):
    for row in array:
        if row[0] in data:
            row.append(data[row[0]][0])
            row.append(data[row[0]][1])
            row.append(data[row[0]][2])
            row.append(data[row[0]][3])
            row.append(data[row[0]][4])
        else:
            row.append("")
            row.append("")
            row.append("")
            row.append("")
            row.append("")


def parse_victim(array, data):
    for row in array:
        if row[0] in data:
            row.append(data[row[0]][0])
            row.append(data[row[0]][1])
            row.append(data[row[0]][2])
            row.append(data[row[0]][3])
            row.append(data[row[0]][4])
        else:
            row.append("")
            row.append("")
            row.append("")
            row.append("")
            row.append("")


def parse_victim_offender_rel(array, data):
    for row in array:
        if row[5] in data:
            row.append(data[row[5]])
        else:
            row.append("")


def parse_agency(array, data):
    for row in array:
        if row[1] in data:
            row.append(data[row[1]][0])
            row.append(data[row[1]][1])
        else:
            row.append("")
            row.append("")


def parse_offense(array, data):
    for row in array:
        if row[0] in data:
            row.append(data[row[0]])
        else:
            row.append("")


def filterData(data):
    parsed = []
    for row in data:
        if row[15] == "3" or row[15] == "12" or row[15] == "21" or row[15] == "26":
            parsed.append(row)
    return parsed


def get_Fips(array, fips):  # to append the fips number
    for row in array:
        current_county = row[16]
        current_state = row[17].upper()
        # If multiple counties for the state have to try every option
        if ";" in current_county:
            counties = current_county.split(";")
            current_county = counties[0]
        elif "/" in current_county:
            counties = current_county.split("/")
            current_county = counties[0]
        elif "-" in current_county:
            counties = current_county.split("-")
            current_county = counties[0]
        current_county = current_county.upper().rstrip().lstrip()
        # If single county
        if (current_county, current_state) in fips:
            row.append(fips[(current_county, current_state)])
        else:
            row.append("")


def makeCsv(name, data, header):
    output = open(f'{name}.csv', 'w', encoding='UTF8', newline='')
    w_output = csv.writer(output)

    w_output.writerow(header)

    w_output.writerows(data)


def create_file(name, path, fips, header):
    out = []  # the final array to be added to

    states = os.listdir(path)

    for state in states:
        new_path = os.path.join(path, state)

        if len(os.listdir(new_path)) == 1:
            new_path = os.path.join(new_path, os.listdir(new_path)[0])

        # Open Incident File

        output_file = readCsv(os.path.join(new_path, "NIBRS_INCIDENT.csv"))
        output_file = get_incident(output_file)

        # Append Offender File

        temp = readCsv(os.path.join(new_path, "NIBRS_OFFENDER.csv"))
        temp = get_offender(temp)
        parse_offender(output_file, temp)

        # Append Victim file

        temp = readCsv(os.path.join(new_path, "NIBRS_VICTIM.csv"))
        temp = get_victim(temp)
        parse_victim(output_file, temp)

        # Append Victim-Offender relationship

        temp = readCsv(os.path.join(new_path, "NIBRS_VICTIM_OFFENDER_REL.csv"))
        temp = get_victim_offender_rel(temp)
        parse_victim_offender_rel(output_file, temp)

        # Append Agency

        if "agencies.csv" in os.listdir(new_path) or "agencies.CSV" in os.listdir(new_path):
            temp = readCsv(os.path.join(new_path, "agencies.csv"))
            temp = get_agency(temp)
        else:
            temp = readCsv(os.path.join(new_path, "cde_agencies.csv"))
            temp = get_cde_agency(temp)
        parse_agency(output_file, temp)

        # Append Offense

        temp = readCsv(os.path.join(new_path, "NIBRS_OFFENSE.csv"))
        temp = get_offense(temp)
        parse_offense(output_file, temp)

        # Add file to final array

        out += output_file

    # add fips

    get_Fips(out, fips)

    # Filter

    filter_data = filterData(out)

    # Convert to CSV file

    makeCsv(name, filter_data, header)


def main():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # path = os.path.join(dir_path, "states")

    path = r"D:\V\states"

    fips = readTxt("FIPS.txt")

    header = ["Incident_ID", "Agency_ID", "Data_Year", "Incident_Date", "Incident_Hour", "Offender_ID", "O_Age_NUM",
              "O_Sex_CODE", "O_Race_ID", "O_Ethnicity_ID", "Victim_ID", "V_Age_NUM", "V_Sex_CODE", "V_Race_ID",
              "V_Ethnicity_ID", "Relationship_ID", "County_Name", "State", "Offense_Type_ID", "FIPS"]

    years = os.listdir(path)

    for year in years:
        new_path = os.path.join(path, year)
        create_file(year, new_path, fips, header)


if __name__ == '__main__':
    main()
