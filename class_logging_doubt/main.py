import ineuron
from courses import AI
def main():
    i = ineuron.base_info()
    i.purpose()
    i.founder()
    i.HQ_address()
    i.contact()
    i.years_in_service(2022)
    i.years_in_service('2022')

def main_AI():
    ai = AI.AI()
    ai.course_features()
    ai.requirements()
    ai.curriculum()
    ai.instructors()

if __name__ == '__main__':
    main()
    main_AI() # I don't get log file which is strange.

