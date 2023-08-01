import os,shutil
path=r"C:/Users/hp/OneDrive/Desktop/vs/Phyton/projects/samples for file sorter/"
#path to reach the file in os

files=os.listdir(path)
#files is the that will loops all the files in the folder

folder_names=["images","zip","videos","docx","pdfs","csv"]

#creating new folder according to the files if not avaiable
for name in range (0,6) :
    if not os.path.exists(path + folder_names[name]):
        #print(path+folder_names[name])
        #can be used to see which folder are being created
        os.makedirs(path + folder_names[name])

#moving the files
for file in files:
    if(".csv") in file and not os.path.exists(path+"csv/"+file):
        shutil.move(path+file,path+"csv/"+file)
    
    if(".jpg") in file and not os.path.exists(path+"images/"+file):
        shutil.move(path+file,path+"images/"+file)
        
    if(".mp4") in file and not os.path.exists(path+"videos/"+file):
        shutil.move(path+file,path+"videos/"+file)
    
    if(".docx") in file and not os.path.exists(path+"docx/"+file):
        shutil.move(path+file,path+"docx/"+file)
    
    if(".pdf") in file and not os.path.exists(path+"pdfs/"+file):
        shutil.move(path+file,path+"pdfs/"+file)
                
    if(".zip") in file and not os.path.exists(path+"zip/"+file):
        shutil.move(path+file,path+"zip/"+file)
    
    if(".word") in file and not os.path.exists(path+"docx/"+file):
        shutil.move(path+file,path+"docx/"+file)
    
    else:
        (print(file+"not have seperate folder"))
    
                