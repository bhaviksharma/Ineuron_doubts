import os
import logging
os.mkdir("logfiles")

logging.basicConfig(filename="logfiles/base_info.log", level=logging.INFO, filemode='w', format="%(levelname)s %(name)s %(asctime)s %(message)s")

# file creation
file_name = "base_info.txt"
try:
    if os.path.isfile(file_name):
        with open(file_name, 'a') as f:
            f.writelines("\n")
            f.writelines("\n")
            f.writelines("\n")
        logging.warning("File already exists, writing in the same file")

    else:
        with open(file_name, 'w+') as f:
            pass
        logging.warning("File doesn't exist, creating and writing in new file.")

except Exception as e:
    logging.info("Something is not right about the file, most probably filename, please check. Here is the error:")
    logging.exception(e)

# I am unable to make above code work via below class by default (i.e, I don't want to create a method for that)
# I tried to put them into __init__ method, but still it didn't work. (__init__ method works by default everytime, so I thought it will work.)
# Please let me know how to do this! I just want 1 class in this file, is it possible??

class base_info:
    __year_founded = 2018
    __contact_mail = "contact@ineuron.ai"
    __contact_phone = "+91 87885-03778"

    def purpose(self):
        logging.info("Output: Purpose")
        with open(file_name, 'a') as f:
            f.writelines("Purpose: Ineuron provides affordable courses on latest software and AI technlogies. \n")
        print("Provides affordable courses on latest software and AI technlogies")


    def founder(self):
        logging.info("Output: founder")
        with open(file_name, 'a') as f:
            f.writelines("Founder: Sudhanshu Kumar \n")
        print("Sudhanshu Kumar")

    def HQ_address(self):
        logging.info("Output: HQ_address")
        hq = "17th floor Tower A, Brigade Signature Towers, Sannatammanahalli, Bengaluru, Karnataka 562129."
        with open(file_name, 'a') as f:
            f.writelines("HQ_address: " + hq + "\n")
        print(hq)

    def contact(self):
        logging.info("Output: contact")
        cout = "\n".join(
            ("Contact:",
             self.__contact_mail,
             self.__contact_phone)
        )
        with open(file_name, 'a') as f:
            f.writelines(cout + "\n")
        print(cout)

    def years_in_service(self, current_year: int):
        try:
            logging.info("Output: years_in_service")
            ans = (current_year - self.__year_founded)
            with open(file_name, 'a') as f:
                f.writelines("Year in service as of " + str(current_year) + " = " + str(ans) + "\n")
            #return ans
        except Exception as e:
            with open(file_name, 'a') as f:
                f.writelines("!! OOPS, something is wrong, please check the log file.")
            logging.error("Current year should be integer value, wrong datatype is entered")
            #logging.error(e)
            logging.exception(e)



    #logging.shutdown()
