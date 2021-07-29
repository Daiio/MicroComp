# Created by Daphne Fauber, Kyle Sander, Will Sharpless, & Adam Arkin
# Last Updated July 26, 2021

# Made using Python 3.8.8 

# MicroComp is a program designed to compare the compatibility between target microbes and the three distinct
#   zones of the rhizopshere---the endorhizosphere, exorhizopshere, and rhizoplane---to inform the creation
#   of more successful plant root system microbiomes

# The inputs of the model are described in more detail in the READ ME, however, briefly the inputs are
#   currently designed to be a variable number of csv files---one that contains the maximum and minimum of
#   parameter values that the target microbes can survive at and the rest of the files representing an
#   environment per file that contains data for each parameter as time passes in the given environment

# The output of the model is currently a text output that utilizes the inputs to compute for which days the
#   microbes would be able to survive under the given conditions and condition limits as well as which 
#   microbes would also overlap in compatibility
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Load csv library for working with comma separated value files in Python
import csv

# Initilaize global variables
file_names = ["testData1.csv", "testData2.csv", "testData3.csv"]
comp_data_dict = {}
microbe_range_data = []
microbe_one = [[], [], []]
microbe_two = [[], [], []]
microbe_three = [[], [], []]
microbe_four = [[], [], []]
microbe_five = [[], [], []]
microbe_list = [microbe_one, microbe_two, microbe_three, microbe_four, microbe_five]
dictionary_keys = []

# Function that accepts an argument that is an array that contains the file names of the environment
#   data files to be processed and populates the data into a dictionary where each environment has its
#   own dictionary entry with all the parameter values by time values
def format_data(data_name_array):

    # Variable that keeps track of which number file is being accessed and uses it as a
    #   naming convention in the dictionary key
    env_i = 1

    # For loop that iterates through the files saved in the array
    for file in data_name_array:

        # The data_name_array argument is used as input into a file path to open the file with target
        #   data as a comma separated value (csv) file using the csv library
        with open(file, newline = '') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skips the first line---the column labels---in the data files
            next(csv_reader)

            # Array that stores data by day so it can compiled and then saved as a single dictionary
            #   entry
            day_data = []

            # For loop that iterates through all the lines in the file and saves each row of data to
            #   the array day_data excluding the column that contains the time
            for row in csv_reader:
                day_data.append(row[1:])

        # Creates an entry in the comp_data_dict dictionary where the key is "environment_i" and the 
        #   value pair is the corresponding day_data array for that environment
        comp_data_dict["environment_" + str(env_i)] = day_data
        dictionary_keys.append("environment_" + str(env_i))

        env_i += 1

# Function that takes user input to determine how many files to process and save their names into an
#   array for processing using the format_data function
def populate_files():
    
    # # Accepts an integer user input for how many environment files should be analyzed
    # num_answer = int(input("How many microclimate files would you like analyzed? "))

    # # For loop that repeats a number of times equal to the num_answer input and appends input file
    # #   names to the file_name array
    # for i in range(int(num_answer)):
    #     file_name_answer = str(input("What file would you like to add? "))
    #     file_names.append(file_name_answer)

    # # Accepts a string user input that is the file name for the file containing the microbe data
    # microbe_data = str(input("What is the name of the file that contains the microbe data? "))

    # The data_name_array argument is used as input into a file path to open the file with target
    #   data as a comma separated value (csv) file using the csv library
    with open("microbeData.csv", newline = '') as csv_file:
            csv_reader = csv.reader(csv_file)

            # For loop that iterates through all the lines in the file and saves each row of data
            #   to the microbe_range_data array ignoring the column that contains the time
            for row in csv_reader:
                microbe_range_data.append(row)

    # Calls the format_data function using the file_names array built during this function as
    #   input
    format_data(file_names)

# Function that accepts a dictionary of environmental data and an array of microbe survival ranges
#   for each parameter as arguments, saving the days in which there was compatibility across all
#   parameters in a given environment to the corresponding array housed within the microbe array
#   and then prints out the compatibility analysis based on the contents of the arrays
def compare_datasets(enviro_data_dictionary, micro_data_array):

    # Variable that keeps track of which microbe is being accessed
    microbe_num = 1

    # For loop that iterates through each microbe in an array of the microbes
    for microbe in micro_data_array:

        # Variable that keeps track of which of the three environments within a specific microbe
        #   array is being accessed
        env_i = 0

        # For loop that iterates through the lists representing the environments for a given microbe
        for environment in microbe:

            # Variable that represents the accessing of the dictionary that contains the enviornmental data
            #   by calling the previously defined dictionary_keys array and iterating through it
            dict_array = enviro_data_dictionary.get(dictionary_keys[env_i])

            # For loop that repeats once for each day
            for day_i in range(15):
               
                # Variable that keeps track of where in the microbe_range_data the comparison is happening
                data_count = 1

                # Array that is populated with True or False by parameter to determine compatibility between
                #   all parameters on a given day for a given microbe
                check_day = []

                # For loop that iterates through all the values in the dictionary entry for the given 
                #   environment by day
                for value in dict_array[day_i]:

                    # If statement that checks if value is between the minimum or maximum compatibility values
                    #   and appends True for every parameter that fits and False for every parameter that does
                    #   not
                    if ((float(value) <= float(microbe_range_data[microbe_num][data_count])) and
                     (float(value) >= float(microbe_range_data[microbe_num][data_count + 1]))):
                        check_day.append(True)
                        data_count += 2
                    else: 
                        check_day.append(False)
                        data_count += 2

                # If statement that adds the number of the day to the microbe-environment array if there were
                #   no Falses in the check_day array
                if check_day.count(False) < 1:
                    micro_data_array[microbe_num - 1][env_i].append(day_i + 1)

            env_i += 1
        microbe_num += 1

    # Variable that keeps track of which microbe is being accessed in compatibiliy analysis
    mic_count = 1

    # For loop that iterates through each microbe in an array of microbes
    for microbe in micro_data_array:

        # Formatting for the printout that prints a header for which microbe is being analyzed
        print()
        print("MICROBE " + str(mic_count) + " COMPATIBILITY ASSESSMENT:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # Variable that keeps track of which of the three environments within a specific microbe
        #   array is being accessed
        enviro_count = 1

        # For loop that iterates through the lists representing the environments for a given microbe
        for environment in microbe:
            
            # Formatting for the printout that prints for each environment, which days the microbe and environment
            #   were compatible
            print("In Environment " + str(enviro_count) + " there was envrionmental compatibility on the following days: ")
            print(micro_data_array[mic_count-1][enviro_count-1])

            # Variable that keeps track of which microbe is being compared to the orginal microbe
            compare_microbe_count = 1

            # For loop that iterates through the microbes in the microbe array to be compared to the orginal microbe
            for compare_microbe in micro_data_array:        
                
                # Formatting for the printout that prints which microbe is being compared to the orginal microbe and
                #   for which environment
                print("For Microbe " + str(compare_microbe_count) + " the following days were compatible with Microbe "
                 + str(mic_count) + " in Environment " + str(enviro_count) + ": ")

                compare_microbe_count += 1

                # For loop that iterates through the lists representing the environments for the comparison microbe
                for compare_environment in compare_microbe:

                    # For loop that iterates through the compatible days stored in the array
                    for compare_days in compare_environment:

                        # If loop that checks if the mcirobes were compatible on a given day and if so prints the day
                        if environment.count(compare_days) > 0:
                            print(compare_days, end = " ")
                
                print()

            enviro_count += 1

        mic_count += 1

# Function that intializes the main functionality of the program by calling the functions
#   populate_files and compare_datasets    
def main():
    populate_files()
    compare_datasets(comp_data_dict, microbe_list)

# Executing body of the program
main()
