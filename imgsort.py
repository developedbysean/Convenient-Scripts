import os
import datetime

path = r"C:\Users\user\Pictures"

img_extensions = ['.jpg','.JPG', '.png', '.gif', '.jpeg']

for files in os.listdir(path):
    for img_extension in img_extensions:
        if(files.endswith(img_extension)):

            file_path = path + "\\" + files

            create_date = os.stat(file_path).st_ctime
            create_year = datetime.datetime.fromtimestamp(create_date).strftime("%Y")
            create_month = datetime.date.fromtimestamp(create_date).strftime("%B")
            
            folder_year_path = os.path.join(path, create_year)
            folder_month_path = os.path.join(folder_year_path, create_month)
            
            if os.path.exists(folder_year_path):
                if os.path.exists(folder_month_path):
                    final_path = os.path.join(folder_month_path, files)
                    os.rename(file_path, final_path)
                else:
                    os.makedirs(folder_month_path)
            else:
                os.makedirs(folder_year_path)
              
       
