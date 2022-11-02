import csv
import os


def file_to_detail(folderPath):
  # Convert the folder to a list
    dataSet = os.listdir(folderPath)
    
  # mapping inside the list 
    for fileName in dataSet:
      #Select just files with "t" in the name
        if fileName[9] == 't':
          #splice the user id from name of file 
            userId=fileName[:3]
            userIds=[]
            userIds.append(userId)
            
            #Find the High-Way Number from name of file 
            Hw_Number= fileName[11:13]
            Hw_Num=[]
            Hw_Num.append(Hw_Number)

            #Find Situation from name of file 
            st_first=fileName[14]
            st_second=fileName[18]
            status=[]
            if st_first =="a":
                if st_second=="b":
                    status.append("a-baseline")
                else:
                    status.append("a")
            else:
                if st_second=="b":
                    status.append("m-baseline")
                else:
                    status.append("m")

            # Create the file path by joining the folder and file name  
            file_path=f"{ os.path.join(folderPath,fileName)}"
            print("File path  ==>>>",file_path)
            # open the file to use the data inside
            file_reader=open(file_path)
            csv_reader = csv.reader(file_reader, delimiter=",")
            next(csv_reader)
            
            
            final=[]
            
#             index=[1]
            
  # Mappingin the CSV file and use each row 
              for (i,row) in enumerate( csv_reader, start=-1):
                #index.append(i)
                #final.append(userIds+Hw_Num+status+[row[:][0]]+[row[:][3]]+[i])
                final.append(userIds+Hw_Num+status+[row[:][0]]+[row[:][3]])
          # eliminate two first row - header
            final_list=final[2:]
            print(final_list)
            file_reader.close()
            #Create new file and print new list inside
            with open(f'./{fileName}', 'w') as f:
                header = ["col1","col2",'col3',"col4",'col5','col6']
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write multiple rows
                writer.writerows(final_list)
        
file_to_detail("The File Path Should be there .....")
