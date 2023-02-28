class Student:
    def __init__(self, nom, prenom, numero_etudiants):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiants = numero_etudiants
        self.__nb_credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__nb_credits += int(credits)
            self.__level = self.__studentEval()
        return f'Le nombre de credit de {self.__prenom} {self.__nom} est de {self.__nb_credits}'
    
    def __studentEval(self):
        if self.__nb_credits <= 59:
            return "insuffisant"
        elif self.__nb_credits >= 60 and self.__nb_credits <=69:
            return "Passable"
        elif self.__nb_credits >= 70 and self.__nb_credits <= 79:
            return "Bien"
        elif self.__nb_credits >= 80 and self.__nb_credits <= 89:
            return "Tres bien"
        elif self.__nb_credits >= 90:
            return "Excellent"
        
    def studentInfo(self):
        return f'Nom = {self.__nom}\nPrénom = {self.__prenom}\nid = {self.__numero_etudiants}\nNiveau = {self.__level}'

    

s = Student("Doe", "Jhon", 145)
for i in range(3):
    s.add_credits(25)
print(s.studentInfo())
