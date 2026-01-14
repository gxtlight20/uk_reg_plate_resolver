import csv
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "letter_codes.csv")

def number_plate_finder():
  print()
  print("Number Plate Finder UK Selected")
  print("The number plate must be in the format [XX00 XXX]")
  num_plate = input("Enter Number Plate: ")
  place_location = num_plate[0:2]
  year_location = num_plate[2:4]
  year_location = int(year_location)
  
  if year_location >= 51:
    year_of = year_location - 50
    if year_of < 10:
      year_of = "0" + str(year_of)
    year_of = str(year_of)
    final_year_of = "20" + year_of
  else:
    year_of = year_location
    year_of = str(year_of)
    final_year_of = "20" + year_of
  
  with open(file_path, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 3:
                    continue  # Skip rows with insufficient data

                area_code = row[0].strip()
                location = row[1].strip()
                letters = row[2].strip().split()

                if num_plate[0] == area_code and num_plate[1] in letters:
                    location_vehicle = location
                else:
                    "Location not found for the given number plate."

  if location_vehicle:
    print("The vehicle year is:", final_year_of)
    if location_vehicle != "Reserved for select issue":
        print("The vehicle is registered to the", location_vehicle, "DVLA office.")
    else:
        print("The vehicle has a location identifier of reserved for select issue, the location of the vehicle registration could not be found.")
  else:
    print("The vehicle year is:", final_year_of)
    print("The registration plate locator characters do not match governmental records")

  print("You will now be return to the main menu.")
  main_menu()

def main_menu():
    number_plate_finder()
main_menu()
