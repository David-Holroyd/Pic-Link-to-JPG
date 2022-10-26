import requests
import shutil
import pandas as pd
import cgi

folder = r'C:\Users\DavidHolroyd\PycharmProjects\Pic_Downloader\Excel Input\\'
file = input('Please enter file name to trap picture file in Excel Input folder: ')
filepath = folder + file
trap_df = pd.read_excel(filepath, usecols=['Tag #', 'Pic'])

traps = trap_df.values.tolist()  # This creates a list containing a list for each trap. This will be iterated over

pics_already_added = set()  # This set is to prevent pictures from being added twice - an error that prevents


for trap in traps:

    pic_list = []
    pic_list.append(trap[1])

    for pic in pic_list:
        picture_obj = requests.get(fr'{pic}', stream=True)
        picture_obj.raw.decode_content = True
        with open(f"{trap[0]}.jpg", 'wb') as f:  # Each picture is saved in the local directory with tag # as file name
            shutil.copyfileobj(picture_obj.raw, f)
        header = cgi.parse_header(picture_obj.headers['content-disposition'])[1]
        filename = header['filename']
        print(header)
        if filename in pics_already_added:
            print(filename)
            print(pics_already_added)
