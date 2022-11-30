import random


class Pipette:

    def __init__(self, location):
        self.serial = input("Enter pipette serial number: ")
        self.location = location
        try:
            x = open("cal_date_12-2022_cal_due_03-2023.txt", 'r')
            if (self.serial in x):
                print("* Check output file *")
            else:
                print("* Serial not yet in file *")
        except:
            pass
        self.channel = input("Single or multichannel: ")
        self.min_volume = float(input("Minimum volume (ul): "))
        self.max_volume = float(input("Maximum volume (ul): "))

    def out(self):
        # our current scale is not accurate under 1ul
        if (self.min_volume <= 1.0):
            self.temp1 = round(random.uniform(0.95, 1.05), 2)
            self.temp2 = round(random.uniform(0.95, 1.05), 2)
            self.temp3 = round(random.uniform(0.95, 1.05), 2)
            self.average = round((self.temp1 + self.temp2 + self.temp3) / 3, 2)
        else:
            top = 0.05 * self.min_volume + self.min_volume
            bottom = self.min_volume - 0.05 * self.min_volume
            self.temp1 = round(random.uniform(bottom, top), 2)
            self.temp2 = round(random.uniform(bottom, top), 2)
            self.temp3 = round(random.uniform(bottom, top), 2)
            self.average = round((self.temp1 + self.temp2 + self.temp3) / 3, 2)
        # one txt file per calibration month
        f = open("cal_date_12-2022_cal_due_03-2023.txt", 'a')
        f.write("Location: " + self.location + "\n")
        f.write("Pipette Serial Number: " + self.serial + "\n")
        f.write("Channel: " + self.channel + "\n")
        if (self.min_volume < 1.0):
            f.write("Volume Range: " + str(self.min_volume) + " - " + str(int(self.max_volume)) + "ul\n")
        else:
            f.write("Volume Range: " + str(int(self.min_volume)) + " - " + str(int(self.max_volume)) + "ul\n")
        f.write("Example volumes assuming 5% error (ul):    " + str(self.temp1) + "    " + str(self.temp2) + "    " + str(self.temp3) + "\n")
        f.write("Example Average: " + str(self.average) + "ul\n\n")
        self.choice = input("\nPress 1 to enter another pipette in " + self.location + "\n" \
            "Press 2 for a new location\nPress enter to quit\n")
        print()
        if (self.choice == '1'):
            same = Pipette(self.location)
            same.out()
        elif (self.choice == '2'):
            new = Pipette(input("Enter location of pipette: "))
            new.out()
                

p = Pipette(input("Enter location of pipette: "))
p.out()
