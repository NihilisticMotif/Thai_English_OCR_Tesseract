import os
import random
import pathlib
import subprocess

# https://github.com/astutejoe/tesseract_tutorial/blob/main/split_training_text.py
# https://youtu.be/KE4xEzFGSU8?si=NInF-dOBSbLCFz7V

########################################################################################
# Input
########################################################################################
DataSets=[
    'ChatGPT01.txt'
]
Select=DataSets[0]
Return='01'

########################################################################################
# Read Text File
########################################################################################

training_text_file = '/mnt/c/Users/Admin/Documents/GitHub/Thai_English_OCR_Tesseract/DataSet/'+Select
lines = []
count=0

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        if(count<5):
            if('III' in line):
                continue
            else:
                #print('##############'+str(count))
                #print(line.strip())
                #print(line)
                lines.append(line.strip())
                count+=1


########################################################################################
# Create Output Folder
########################################################################################
output_directory = '../Data_'+Return

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

########################################################################################
# Shuffle, Train Test Split
########################################################################################
'''
random.shuffle(lines)

count = 700
#print(len(lines))

Train = lines[:count]
Test = lines[count:]
#print(len(Train))
#print(len(Test))
'''

########################################################################################
# Create Data Set Files
########################################################################################


line_count = 0
for line in lines:
    # Origin file.txt
    # In this case, TxT
    ClassName = pathlib.Path(training_text_file).stem
    #print(ClassName)
    # TxT

    # Specify directory of the data file
    # ...
    # ../Data_/ChatGPT_974.gt.txt
    # ../Data_/ChatGPT_975.gt.txt
    # ../Data_/ChatGPT_976.gt.txt
    # ../Data_/ChatGPT_977.gt.txt
    # ../Data_/ChatGPT_978.gt.txt
    # ../Data_/ChatGPT_979.gt.txt
    # ...
    ThisName = os.path.join(output_directory, f'{ClassName}_{line_count}.gt.txt')
    #print(ThisName)

    # Create String Data file.txt
    with open(ThisName, 'w') as output_file:
        output_file.writelines([line])

    # Image File Name
    ThisImage = f'eng_{line_count}'
    #print(ThisImage)
    
    subprocess.run([
        'text2image',
        '--font=Apex',
        f'--text={ThisName}',
        f'--outputbase={output_directory}/{ThisImage}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=32',
        '--xsize=3600',
        '--ysize=480',
        '--char_spacing=1.0',
        '--exposure=0',
        '--unicharset_file=langdata/eng.unicharset'
    ])

    
    line_count += 1

'''
python3 CreateData.py
'''