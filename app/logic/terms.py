from app.logic.database_manager import getSemesters
semesters = []

def handle_semesters(option):
    global currentSemester, semesters
    if option == "init": #Initialize semesters[]
        for i in range(len(getSemesters())):
            semesters.append(f"Semester {getSemesters()[i][0]}")
        semesters.append("Add Semester")
        currentSemester = int(semesters[0].split()[-1])
    elif option == "Add Semester":
        latestSem = int(semesters[-2].split()[-1])
        semesters.insert(-1, f"Semester {latestSem + 1}")
    else:
        currentSemester = int(option.split()[-1])

def get_current_semester():
    return currentSemester