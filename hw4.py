import sys
import build_data
from hw3 import *
import data


def read_ops(fileName : str) -> list[list[str]]:
    f = open(fileName, 'r')
    contents = f.read()
    f.close()
    ops = []
    for line in contents.split('\n'):
        arr = line.split(':')
        ops.append(arr)
    return ops

def do_ops(d : list[data.CountyDemographics], ops : list[list[str]]):
    s = []
    for command in ops:
        try:
            if command[0] == "filter-state":
                s = filter_by_state(d, command[1])
                print("Filter: state ==", command[1], "(", len(s), "entries)")
            elif command[0] == "population-total":
                x = population_total(d)
                print("2014 population:", x)
            elif command[0] == "percent":
                key = command[1].split('.')
                if key[0] == "Education":
                    print("2014", command[1], percent_by_education(d, key[1]))
                elif key[0] == "Ethnicities":
                    print("2014", command[1], percent_by_ethnicity(d, key[1]))
                elif key[0] == "Income":
                    print("2014", command[1], percent_below_poverty_level(d, key[1]))
            elif command[0] == "population":
                key = command[1].split('.')
                if key[0] == "Education":
                    print("2014", command[1], population_by_education(d, key[1]))
                elif key[0] == "Ethnicities":
                    print("2014", command[1], population_by_ethnicity(d, key[1]))
                elif key[0] == "Income":
                    print("2014", command[1], population_below_poverty_level(d, key[1]))
            elif command[0] == "filter-gt":
                key = command[1].split('.')
                if key[0] == "Education":
                    d = education_greater_than(d, key[1], float(command[2]))
                elif key[0] == "Ethnicities":
                    d = ethnicity_greater_than(d, key[1], float(command[2]))
                elif key[0] == "Income":
                    d = below_poverty_level_greater_than(d, float(command[2]))
            elif command[0] == "display":
                for row in d:
                    print(row)
            elif command[0] == "filter-lt":
                key = command[1].split('.')
                if key[0] == "Education":
                    d = education_less_than(d, key[1], float(command[2]))
                elif key[0] == "Ethnicities":
                    d = ethnicity_less_than(d, key[1], float(command[2]))
                elif key[0] == "Income":
                    d = below_poverty_level_less_than(d, float(command[2]))
            elif command[0] == "":
                pass
            else:
                print("Unrecognized command: ", command[0])
        except:
            print("ValueError: error in formatting")





if __name__ == "__main__":
    ops = read_ops(sys.argv[1])
    d = build_data.get_data()
    print(len(d), "records loaded")
    do_ops(d, ops)

