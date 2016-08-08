import re

FilePath = "D:\\2016_2017_OVTI\\_20160808_Demis-Hassibis\\"
# FileName = "Demis Hassabis, CEO, DeepMind Technologies - The Theory of Everything.srt"
FileName = "Demis Hassabis - Artificial Intelligence.srt"
InFile = FilePath + FileName
OutFile = FilePath + "_" + FileName

input_file = open(InFile, 'r')
output_file = open(OutFile, 'w')

OutString = ""
for OneLine in input_file:
    if OneLine is not None:
        if re.search('[a-zA-Z]', OneLine):
            # OneLine = OneLine.replace("\n", " ")
            OneLine = OneLine.replace(".", ".\n")
            OneLine = OneLine.replace("  ", " ")
            OutString += OneLine

            # if re.search('[I]', OneLine):
            #     print OneLine
            #     print OneLine
    else:
         break;

output_file.writelines(OutString)
