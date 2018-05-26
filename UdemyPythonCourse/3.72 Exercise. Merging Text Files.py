import glob2
from datetime import datetime

filenames_to_read = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file_for_merging:
    for filename in filenames_to_read:
        with open(filename, "r") as f:
            file_for_merging.write(f.read() + "\n")




#import glob2
#from datetime import datetime
 
#filenames = glob2.glob("*.txt")
#with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
#    for filename in filenames:       
#        with open(filename, "r") as f:
#            file.write(f.read() + "\n")



# filenames = ["file1.txt", "file2.txt", "file3.txt"]
# #def merger(filename, filepath):
#    with open(filepath, 'w') as merged_text_file:

#        for names in filenames:
           
#                merged_text_file.write(str(f) + "\n")
#merger(filenames, "merged.txt")

    
