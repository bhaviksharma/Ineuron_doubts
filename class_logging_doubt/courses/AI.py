import os
import logging
logging.basicConfig(filename="logfiles/AI_course.log", level=logging.INFO, filemode='w', format="%(levelname)s %(name)s %(asctime)s %(message)s")
file_name = "AI_course.txt"

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

class AI:

    def course_features(self) -> None:
        '''
        AI course features
        :return: str -- and writes in AI_course.txt file.
        '''
        logging.info("AI course features")
        cout = "\n".join((
            "********** AI COURSE FEATURES **********",
            "AI: On demand recorded videos",
            "AI: Assignments",
            "AI: Quizzes",
            "AI: Course completion certificate"
        ))
        with open(file_name, 'a') as f:
            f.writelines("\n")
            f.writelines("\n")
            f.writelines("********** AI COURSE FEATURES ********** \n")
            f.writelines("AI: On demand recorded videos \n")
            f.writelines("AI: Assignments\n")
            f.writelines("AI: Quizzes\n")
            f.writelines("AI: Course completion certificate \n")


        print(cout)


    def requirements(self) -> None:
        '''
        AI course requirements
        :return: str -- and writes in AI_course.txt file.
        '''
        logging.info("AI course requirements")

        cout = "\n".join((
            "********** AI COURSE REQUIREMENTS **********",
            "AI: System with Internet Connection",
            "AI: Interest to learn",
            "AI: Dedication"
        ))

        with open(file_name, 'a') as f:
            f.writelines("\n")
            f.writelines("\n")
            f.writelines("********** AI COURSE REQUIREMENTS ********** \n")
            f.writelines("AI: System with Internet Connection\n")
            f.writelines("AI: Interest to learn \n")
            f.writelines("AI: Dedication \n")

        print(cout)

    def curriculum(self) -> None:
        '''
        AI course curriculum
        :return: str -- and writes in AI_course.txt file
        '''
        logging.info("AI course curriculum")

        cout = "\n".join((
            "********** AI COURSE CURRICULUM **********",
            "AI: Topic 1",
            "AI: Topic 2",
            "AI: Topic 3"
        ))

        with open(file_name, 'a') as f:
            f.writelines("\n")
            f.writelines("\n")
            f.writelines("********** AI COURSE CURRICULUM ********** \n")
            f.writelines("AI: Topic 1 \n")
            f.writelines("AI: Topic 2 \n")
            f.writelines("AI: Topic 3 \n")

        print(cout)



    def instructors(self) -> None:
        '''
        AI Course Instructors
        :return: str -- and writes in AI_course.txt file
        '''

        logging.info("AI course instructors")

        cout = "\n".join((
            "********** AI COURSE INSTRUCTORS **********",
            "AI: Sudhanshu Kumar",
            "AI: Krish Naik"
        ))

        with open(file_name, 'a') as f:
            f.writelines("\n")
            f.writelines("\n")
            f.writelines("********** AI COURSE INSTRUCTORS ********** \n")
            f.writelines("AI: Sudhanshu Kumar \n")
            f.writelines("AI: Krish Naik \n")

        print(cout)






