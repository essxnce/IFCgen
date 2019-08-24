"""

Changing a scale of a wall information as industry foundation class (IFC) data
Author : Jinhyeok Yang
last modified : 2019/08/09

"""


def wallScale(walltype, width, length, height):
    file_input = open("wall.ifc", "r")  # Read existing data
    file_output = open("wall_edited.ifc", "w") # Write and save only coorninate data

    dataline = file_input.readlines()
    
    string = " "

    halfWidth = repr(int(width) / 2)
    newArea = repr(int(length)*int(height))
    newVolume = repr(300*int(newArea))

    for i in range(0, len(dataline)):
        ##### Wall material (But width is not changed) #####
 
        #47
        if "IFCWALLSTANDARDCASE" in dataline[i]:
            file_output.write(dataline[i].replace("135mm Partition (2-hr)", walltype))
        #48
        elif "IFCWALLTYPE" in dataline[i]:
            file_output.write(dataline[i].replace("135mm Partition (2-hr)", walltype))
        #49
        elif "IFCMATERIALLAYERSET" in dataline[i]:
            file_output.write(dataline[i].replace("135mm Partition (2-hr)", walltype))
        

        ##### Wall dimension (width, length and height) #####
        #65 width
        elif "IFCMATERIALLAYERSETUSAGE" in dataline[i]:
            file_output.write(dataline[i].replace("67.5", halfWidth))
        #70 length
        elif ("IFCQUANTITYLENGTH" in dataline[i]) and ('NominalLength' in dataline[i]):
            file_output.write(dataline[i].replace("1000", length))
        #73 height
        elif ("IFCQUANTITYLENGTH" in dataline[i]) and ('NominalHeight' in dataline[i]):
            file_output.write(dataline[i].replace("2700", height))
        #74 length and height
        elif ("IFCQUANTITYAREA" in dataline[i]):
            file_output.write(dataline[i].replace("2700000", newArea))
        #75 width, length and height
        elif ("IFCQUANTITYVOLUME" in dataline[i]):
            file_output.write(dataline[i].replace("364500000", newVolume))
        #80, #84 - #88 width, height
        elif ("IFCCARTESIANPOINT" in dataline[i]) and (("1000" in dataline[i]) or ("67.5" in dataline[i])):
            string = dataline[i].replace("1000", length)
            string = string.replace("67.5", halfWidth)
            file_output.write(string)
        #89 height
        elif ("IFCEXTRUDEDAREASOLID" in dataline[i]) and ("2700" in dataline[i]):
            file_output.write(dataline[i].replace("2700", height))


        ##### Rest of lines #####
        else:
            file_output.write(dataline[i])


    file_input.close() # close input reading data
    file_output.close() # close output writing data

    print("Data is edited")
    
def main():
    wallScale("Generic 300mm", "300", "3000", "5000")

main()
