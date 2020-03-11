"""
The Divide.py
'Economic Immobility' Wicked problem
"""
#<METADATA>
SOLUZION_VERSION = "3.0"
PROBLEM_NAME = "The Divide"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['A. Chu, D. Hu, E. Kuniyoshi & O. Shaikh Omar']
PROBLEM_CREATION_DATE = "12-SEP-2019"

PROBLEM_MISC =\
"""
The game The Divide requires the player to solve the wicked 
problem of Economic Immobility, The setting is a fictional 
city that contains allsocial classes from working to upper 
class. Gameplay, which revolves around the lives of four 
people in a family, is influenced by the social class the 
player has selected at the start of the game. For example, 
someone who selects being rich would have access to a large 
sum of cash, allowing them to pursue the best healthcare, 
education, and other opportunities for success in the game. 
The player will be presented with a screen that displays 
public service facilities and other buildings found in a 
typical city. The family in the game can move to these 
various locations to increase their income, education etc.
"""
#</METADATA>
#<COMMON_DATA>

from random import randint

#</COMMON_DATA>

#</COMMON_CODE>

"""Inc: is the individuals income per month
Hlth & hap: represent the health and happiness of each individual
Edu: max-15"""

#(sm, [inc0, inc1, inc2, inc3], [hlth0, hlth1, hlth2, hlth]3, [hap0, hap1, hap2, hap3], [edu0, edu1, edu2, edu3])
income_class = 0 #income class array index
sm = 1 #starting balance array index
inc = 2 #income array index
hlth = 3 #health array index
hap = 4 #happiness array index
edu = 5 #education array index
occ = 6 #occupation array index
gender = 7 #gender array index
age = 8 #age array index
diploma = 9 #diploma
housing = 10 #housing
ins = 11 #insurance level
turn = 12 #turn array index

father = 0 # array index to access father's status
mother = 1 # array index to access mother's status
brother = 2 # array index to access brother's status 
sister = 3 # array index to access sister's status

global actions
actions = 0

global housing_list
housing_list = {'expense':0, 'hlth_change':0}

global job_list
job_list = [{'hlth_cost': 0, 'hap_cost': 0}, {'hlth_cost': 0, 'hap_cost': 0}, {'hlth_cost': 0, 'hap_cost': 0}, {'hlth_cost': 0, 'hap_cost':0}]

global choose_fam
choose_fam = father

global print_fam
print_fam = 'Father'
#income class depends on what the user picks
lower_class = {"balance": 5000, "income": [10000,0,0,0], "starting_job": ['Garbage Collector', 'None', 'None', 'None'], "health": [60, 65, 85, 80], "happiness": [50, 45, 60, 70], "education": [5,3,0,0], "diploma": ['High-School Diploma', 'None', 'None', 'None'], "housing": 'Trailer Park'}
middle_class = {"balance": 30000, "income": [50000, 40000, 0, 0], "starting_job": ['Office Worker', 'Teacher', 'None', 'None'], "health": [65, 70, 90, 90], "happiness": [60, 65, 80, 75], "education": [11, 6, 1, 1], "diploma": ['College Diploma', 'High-School Diploma', 'None', 'None'], "housing": 'Apartment'}
upper_class = {"balance": 100000, "income": [150000, 35000, 0, 0], "starting_job": ['Doctor', 'Secretary', 'None', 'None'], "health": [80, 85, 95, 95], "happiness": [80, 85, 90, 85], "education": [15, 11, 1, 1], "diploma": ['Vocational Degree', 'College Diploma', 'None', 'None'], "housing": 'Mansion'}

#max_actions
#all occupations (Dictionary: education requirements, pay, former job)
construction_worker = {"salary": 30000, "education":4, "age": 18, "gender": 'M', "name": 'Construction Worker', "hap_cost": -3, "hlth_cost": -5}
office_worker = {"salary": 50000, "education":6,  "age": 21, "gender": 'M', "name": 'Office Worker', "hap_cost": -4, "hlth_cost": -3}
doctor = {"salary": 150000, "education":15, "age": 30, "gender" : 'M/F', "name": 'Doctor', "hap_cost": -3, "hlth_cost": -4}
care_taker = {"salary": 15000, "education":3, "age": 18, "gender" : 'F', "name": 'Care Taker', "hap_cost": -1, "hlth_cost": -3}
secretary = {"salary": 35000, "education":7, "age": 30, "gender" : 'F', "name": 'Secretary', "hap_cost": -3, "hlth_cost": -3}
nurse  = {"salary": 70000, "education":10, "age": 30 , "gender" : 'F', "name": 'Nurse', "hap_cost": -2, "hlth_cost": -5}
real_estate = {"salary": 100000 , "education":11, "age": 30 , "gender" : 'M', "name": 'Real Estate Agent', "hap_cost": -2, "hlth_cost": -3}
garbage_collector = {"salary": 10000, "education":4 , "age": 20, "gender" : 'M/F', "name": 'Garbage Collector', "hap_cost": -5, "hlth_cost": -6}
teacher = {"salary": 40000, "education": 9, "age": 30, "gender" : 'M/F', "name": 'Teacher', "hap_cost": -2, "hlth_cost": -3}
truck_driver = {"salary": 35000, "education": 5 , "age": 20 , "gender": 'M/F', "name": 'Truck Driver', "hap_cost": -4, "hlth_cost": -2}
volunteer= {"salary": 0, "edu_gain": 1, "edu_chance": 20, "education": 0, "age": 10, "gender" : 'M/F', "name": 'Volunteer', "hap_cost": 5, "hlth_cost": 2}

#all education (pricing, education chance, happiness cost, health cost)
#middle_school/high_school
private_school = {"expense": 5000, "max_age": 30, "edu_chance":90, "edu_points": 1}
public_school = {"expense": 500, "max_age": 30, "edu_chance": 40, "edu_points": 1}
home_school = {"expense": 100, "max_age": 30, "edu_chance": 20, "edu_points": 1}
vocational = {"expense": 20000, "max_age": 50, "edu_chance": 80, "edu_points": 3}

#college
community_college = {"expense": 10000, "max_age": 40, "edu_chance": 75, "edu_points": 2, "diploma": 'college'}
public_university = {"expense": 2000, "max_age": 40, "edu_chance": 85, "edu_points": 2, "diploma":'college'}
private_university = {"expense": 2000, "max_age": 40, "edu_chance": 90, "edu_points": 2, "diploma": 'college'}

#all housing (pricing, expense, health rise, risk chance)
tent_city ={"expense": 0, "hlth_change": -8, "name": "Tent City"}
trailer_park = {"expense": 1000, "hlth_change": -2, "name": "Tent City"}
apartment  = {"expense": 7500, "hlth_change": 3, "name": "Tent City"}
duplex = {"expense": 15000, "hlth_change": 5, "name": "Tent City"}
mansion = {"expense": 30000, "hlth_change": 10, "name": "Tent City"}

#all consumables/groceries(pricing, health rise)
canned_goods = {"expense": 250, "hlth_change": 3}
microwavable_meals = {"expense": 300, "hlth_change":4}
fresh_produce = {"expense": 500, "hlth_change":8}
vitamin = {"expense": 600, "hlth_change":10}
medicine = {"expense": 1300, "hlth_change": 19}

take_out = {"expense": 700, "hlth_change":11 }
restaurant = {"expense": 1600, "hlth_change": 22}
local_diner = {"expense": 1400, "hlth_change": 20}
fine_dinning = {"expense": 2500, "hlth_change": 25}

#all entertainment (pricing, happiness rise)
park = {"expense": 0, "hap_change": 2}
circus = {"expense": 200, "hap_change": 5}
movies = {"expense": 500, "hap_change": 7}
amusement_park = {"expense":800, "hap_change": 9}
vacation = {"expense":2000, "hap_change": 15}

#all insurance (pricing, risk protection level)
level1_insurance = {"expense": 1000, "level": 1}
level2_insurance = {"expense": 4000, "level": 2}
level3_insurance = {"expense": 10000, "level": 3}

class State:

    #Initial State
    def __init__(self, d=None):
    
        if d==None:
            # [income class, sm, inc, hlth, hap, edu, occ, age, gender, turn]
            d = {'profile': ['', 0, [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ['None','None','None','None'], ['M','F','M','F'], [34,32,14,13], ['None','None','None','None'], '', 0, 0]}
            p = d['profile']
            #print tutorial here  IMPORTANT
            #p[0] = input("Select a starting income class: lower, middle, upper")
            #self.bracket()
                
        self.d = d
        

    def __str__(self):
        p = self.d['profile']
        global print_fam
        if choose_fam == 0:
            print_fam = 'Father'
        elif choose_fam == 1:
            print_fam = 'Mother'
        elif choose_fam == 2:
            print_fam = 'Brother'
        elif choose_fam == 3:
            print_fam = 'Sister'
            
        return  '\n' + "=========================================================================" + '\n' +\
                "\n Individual Information: " + '\n' +\
                "\n Father's Profile- Income: " + str(p[inc][father]) + ", Health: " + str(p[hlth][father]) + ", Happiness: " + str(p[hap][father]) + ", Education: " + str(p[edu][father]) + ", \n" + " Occupation: " + str(p[occ][father]) + ", Age: " + str(p[age][father]) + " Gender: " + str(p[gender][father]) + ", Diploma: " + str(p[diploma][father]) + "\n" + "\n" +\
                " Mother's Profile- Income: " + str(p[inc][mother]) + ", Health: " + str(p[hlth][mother]) + ", Happiness: " + str(p[hap][mother]) + ", Education: " + str(p[edu][mother]) + ", \n" + " Occupation: " + str(p[occ][mother]) + ", Age: " +  str(p[age][mother]) + " Gender: " + str(p[gender][mother]) + ", Diploma: " + str(p[diploma][mother]) + "\n" + "\n" +\
                " Brother's Profile- Income: " + str(p[inc][brother]) + ", Health: " + str(p[hlth][brother]) + ", Happiness: " + str(p[hap][brother]) + ", Education: " + str(p[edu][brother]) + ", \n" + " Occupation: " + str(p[occ][brother]) + ", Age: " +  str(p[age][brother]) + " Gender: " + str(p[gender][brother]) + ", Diploma: " + str(p[diploma][brother]) + "\n" + "\n" +\
                " Sister's Profile- Income: " + str(p[inc][sister]) + ", Health: " + str(p[hlth][sister])+ ", Happiness: " + str(p[hap][sister]) + ", Education: " + str(p[edu][sister]) + ", \n" + " Occupation: " + str(p[occ][sister]) + ", Age: " + str(p[age][sister]) + " Gender: " + str(p[gender][sister]) + ", Diploma: " + str(p[diploma][sister]) + "\n" + "\n" +\
                " Financial Information: " + "\n" + \
                " Income Class: " + str(p[income_class]) + "\n" + \
                " Housing: " + str(p[housing]) + "\n" + \
                " Family Balance: " + str(p[sm]) + "\n" + \
                " Turn: "+ str(p[turn]) + "\n" +\
                " Actions: "+ str(actions) + "\n" +\
                " Playing as: " + print_fam + "\n" +\
                '\n' + "=========================================================================" + '\n'
        

    def __hash__(self):
        return (self.__str__()).__hash__()
    
    def copy(self):
        news = State(d=self.d)
        return news
   
    def bracket(self, bracket):
        news = self.copy()
        p = news.d['profile']
        if  bracket == 'lower':
                p[income_class] = 'lower'
                p[sm] = lower_class.get('balance')
                p[inc] = lower_class.get('income')
                p[hlth] = lower_class.get('health')
                p[hap] = lower_class.get('happiness')
                p[edu] = lower_class.get('education')
                p[diploma] = lower_class.get('diploma')
                p[occ] = lower_class.get('starting_job')
                p[housing] = lower_class.get('housing')

        elif bracket == 'middle':
                p[income_class] = 'middle'
                p[sm] = middle_class.get('balance')
                p[inc] = middle_class.get('income')
                p[hlth] = middle_class.get('health')
                p[hap] = middle_class.get('happiness')
                p[edu] = middle_class.get('education')
                p[diploma] = middle_class.get('diploma')
                p[occ] = middle_class.get('starting_job')
                p[housing] = middle_class.get('housing')

        elif bracket == 'upper':
                p[income_class] = 'upper'
                p[sm] = upper_class.get('balance')
                p[inc] = upper_class.get('income')
                p[hlth] = upper_class.get('health')
                p[hap] = upper_class.get('happiness')
                p[edu] = upper_class.get('education')
                p[diploma] = upper_class.get('diploma')
                p[occ] = upper_class.get('starting_job')
                p[housing] = upper_class.get('housing')
                
        news.d['profile'] = p
        return news
        

    def max_actions(self):
        if actions == 10:
            return False
        
        else:
            return True
        
    def education(self, family, choice):
        global actions
        news = State(d=self.d)
        p = news.d['profile'][:]
        chance = randint(0,100)
        p[sm] -= choice.get('expense')
        actions += 1
        
        if (chance <= choice.get('edu_chance')):
                p[edu][family] += choice.get('edu_points')

        for i in range(len(p[edu])):
            if p[edu][i] >= 5 and p[edu][i] < 11:
            #high-school diploma
                p[diploma][i] = 'High-School Diploma'
                
            elif p[edu][i] >= 11 and p[edu][i] <=15:
            #college-diploma
                p[diploma][i] = 'College Diploma'
                
            #vocational diploma
            elif p[edu][i] == 15:
                p[diploma][i] = 'Vocational Degree'       
        news.d['profile'] = p
        return news           
    
    def job(self, family, job):
        global actions
        global job_list
        news = self.copy()
        p = news.d['profile']
        if job == volunteer:
            p[occ][family] = job.get("name")
            p[inc][family] = job.get("salary")
            job_list['jobs'].insert(family, job)
            actions += 1
        
        else:
            actions += 1
            p[occ][family] = job.get("name")
            p[inc][family] = job.get("salary")
            job_list['jobs'].insert(family, job)
            news.d['profile'] = p
        return news
        
    # costs happiness and health
    
    #def entertainment, housing, groceries, insurance all need money
    def entertainment(self, entertainment):
        global actions
        news = State(d=self.d)
        p = news.d['profile'][:]
        chance = randint(0,100)
        p[sm] -= entertainment.get('expense')
        actions += 1
        for i in range(len(p[hap])):
            p[hap][i] += entertainment.get('hap_change')
            if p[hap][i] > 100:
                p[hap][i] = 100
        news.d['profile'] = p
        return news
    
    def insurance(self,level):
        news = State(d=self.d)
        p = news.d['profile']
        global insurance_info
        insurance_info['expense'] = level['expense']
        insurance_info['level'] = level['level']
        p[ins] = level['level']
        news.d['profile'] = p
        return news

    def grocery(self, grocery):
        global actions
        news = State(d=self.d)
        p = news.d['profile'][:]
        p[sm] -= grocery.get('expense')
        actions += 1
        for i in range(len(p[hlth])):
            p[hlth][i] += grocery.get('hlth_change')
            if p[hlth][i] > 100:
                p[hlth][i] = 100
        news.d['profile'] = p
        return news
    
    def housing(self, choice):
        global actions
        news = State(d=self.d)
        p = news.d['profile']
        p[sm] -= choice.get('expense')
        p[housing] = choice.get('name')
        news = self.copy()
        p = news.d['profile']
        actions += 1
        for i in range(len(p[hlth])):
            if p[hlth][i] > 100:
                p[hlth][i] = 100
        news.d['profile'] = p
        return news

    def choose_family(self, family):
        news = self.copy()
        global choose_fam 
        choose_fam = family
        return news

    def value_change(self):
        global job_list
        global housing_list
        news = State(d=self.d)
        p = news.d['profile']
        p[sm] = p[sm] + p[inc][father] + p[inc][mother] + p[inc][brother] + p[inc][sister] - insurance_info['expense'] - housing_list['expense']
        for i in range(len(p[hlth])):
            p[hlth][i] += job_list['jobs'][i].get("hlth_cost")
            p[hlth][i] += housing_list['housing'][i].get("hlth_change")
        for i in range(len(p[hap])):
            p[hap][i] += job_list['jobs'][i].get("hap_cost")

    def turn(self):
        global actions
        news = self.copy()
        p = news.d['profile']
        p[turn] += 1
        actions = 0
        self.value_change()
        if turn % 2 == 0:
            for i in range(len(p[age])):
                p[age][i] += 1
        #happiness and health decreases a bit based on decay
        return news
    
    #can_methods
    def can_pay(self, choice):
        p = self.d['profile']
        if self.max_actions():
            if p[sm] >= choice.get('expense'):
                return True
        else:
            return False

    #no dup function
    def can_pay_housing(self, choice):
        global housing_list
        p = self.d['profile']
        if self.max_actions():
            if housing_list['expense'] != choice['expense']:
                if p[sm] >= choice.get('expense'):
                    return True
        else:
                    return False
                
    def can_choose(self):
        news = self.copy()
        p = news.d['profile']
        return True
    
    def can_job(self, family, job):
        global job_list
        news = self.copy()
        p = news.d['profile']
        if self.max_actions():
            if job_list[family]['hlth_cost'] != job['hlth_cost'] and job_list[family]['hap_cost'] != job['hap_cost']:
                if p[age][family] >= job.get('age') and p[gender][family] == job.get('gender') and p[edu][family] >= job.get('education'):
                            return True
                elif p[age][family] >= job.get('age') and job.get('gender') == 'M/F' and p[edu][family] >= job.get('education'):
                            return True
        else:
                return False
        
    def can_bracket(self):
        news = self.copy()
        p = news.d['profile']
        if p[0] == '':
            return True
        
    def can_edu(self, family, education):
        news = self.copy()
        p = news.d['profile']
        if self.max_actions():
            if education['edu_points'] == 1:
                if self.can_pay(education) and p[age][family] <= education.get('max_age'):
                        return True
                else:
                        return False
            elif education['edu_points'] == 2:
                    if p[family][diploma] == 'High-School Diploma' and self.can_pay(education) and p[age][family] <= education.get('max_age'):
                        return True
                    else:
                        return False
            elif education['edu_points']==3:
                    if p[family][diploma] == 'College Diploma' and self.can_pay(education) and p[age][family] <= education.get('max_age'):
                        return True
                    else:
                        return False
        else:
            return False

    def can_college(self, family, education):
        news = self.copy()
        p = news.d['profile']
        if self.max_actions():
            if self.can_pay(education) and p[age][family] <= education.get('max_age'):
                for i in range(len(p[diploma])):
                            if p[diploma][i] == 'High-School Diploma':
                                return True
                            else:
                                return False
        else:
            return False

    def can_vocational(self, family, education):
        news = self.copy()
        p = news.d['profile']
        if self.max_actions():
            if self.can_pay(education) and p[age][family] <= education.get('max_age'):
                for i in range(len(p[diploma])):
                            if p[diploma][i] == 'College Diploma':
                                return True
                            else:
                                return False
        else:
            return False

    def can_turn(self):
        news = self.copy()
        return True
    
    def isGoal(self):
        p = self.d['profile']
        return (p[turn] == 20 or p[hlth][father] == 0 and p[hlth][mother] == 0 and p[hlth][brother] == 0 and p[hlth][sister] == 0 and p[turn] > 1 or p[sm] <= 0 and p[turn] > 1)
 
    
    def goal_message(self):
        p = self.d['profile']

        #if health is none, family dies message
        if (p[sm] < 30000):
           return "Your family is still affected by economic immobility and the future doesn't look bright for them."

        elif (p[sm] > 30000):
           return "Your family is doing decently for itself, the future looks promising."

        elif (p[sm] > 100000):
            return "Your family is able to thrive and move up and the future for your family looks bright."  

    
class Operator:
    
        def __init__(self, name, precond, state_transf):
            
            global print_fam
            if choose_fam == 0:
                print_fam = 'Father'
            elif choose_fam == 1:
                print_fam = 'Mother'
            elif choose_fam == 2:
                print_fam = 'Brother'
            elif choose_fam == 3:
                print_fam = 'Sister'
                
            self.name = name
            self.precond = precond
            self.state_transf = state_transf
            
        def is_applicable(self,s):
            return self.precond(s)

        def apply(self,s):
            return self.state_transf(s)
        
#</COMMON_CODE>
        
#<OPERATOR>

#income bracket
#shrink down to categories
            
intialstate_lower0 = Operator("Pick the low-income bracket",
    lambda s: s.can_bracket(),
    lambda s: s.bracket('lower'))
intialstate_middle1 = Operator("Pick the middle-income bracket",
    lambda s: s.can_bracket(),
    lambda s: s.bracket('middle'))
intialstate_upper2 = Operator("Pick the upper-income bracket",
    lambda s: s.can_bracket(),
    lambda s: s.bracket('upper'))

pick_father1 = Operator("Pick Father",
    lambda s: s.can_choose(),
    lambda s: s.choose_family(father))
pick_mother2 = Operator("Pick Mother",
    lambda s: s.can_choose(),
    lambda s: s.choose_family(mother))
pick_sister3 = Operator("Pick Sister",
    lambda s: s.can_choose(),
    lambda s: s.choose_family(sister))
pick_brother4 = Operator("Pick Brother",
    lambda s: s.can_choose(),
    lambda s: s.choose_family(brother))

#send family member to school (add constraint, parents, plus education levels/options)
#Family member choice
publicschool1 = Operator("Send " + print_fam + " to public school",
    lambda s: s.can_edu(choose_fam, public_school),                         
    lambda s: s.education(choose_fam, public_school))
privateschool2 = Operator("Send " + print_fam + " to private school",
    lambda s: s.can_edu(choose_fam, private_school),
    lambda s: s.education(choose_fam, private_school))
homeschool3 = Operator("Send " + print_fam + " to home school",
    lambda s: s.can_edu(choose_fam, home_school),
    lambda s: s.education(choose_fam, home_school))
community_college4 = Operator("Send" + print_fam + " to community school",
    lambda s: s.can_college(choose_fam, community_college),
    lambda s: s.education(choose_fam, community_college))
public_university5 = Operator("Send" + print_fam + " to public school",
    lambda s: s.can_college(choose_fam, public_university),
    lambda s: s.education(choose_fam, public_university))
private_university6 = Operator("Send" + print_fam + " to private school",
    lambda s: s.can_college(choose_fam, private_university),
    lambda s: s.education(choose_fam, private_university))
vocationalschool7 = Operator("Send " + print_fam + " to vocational school",
    lambda s: s.can_vocational(choose_fam, vocational),
    lambda s: s.education(choose_fam, vocational))

#college add CHANGE
#find job position (add constraint, children, plus education requirements/more job options)
#SHOW SALARY CHANGE
volunteer1 = Operator(print_fam + " applies for job: volunteer",
    lambda s: s.can_job(choose_fam, volunteer),
    lambda s: s.job(choose_fam, volunteer))
garbagecollector2 = Operator(print_fam + " applies for job: garbage collector",
    lambda s: s.can_job(choose_fam, garbage_collector),
    lambda s: s.job(choose_fam, doctor))
truck_driver3 = Operator(print_fam + " applies for job: truck driver",
    lambda s: s.can_job(choose_fam, truck_driver),
    lambda s: s.job(choose_fam, truck_driver))
constructionworker4 = Operator(print_fam + " applies for job: construction worker",
    lambda s: s.can_job(choose_fam, construction_worker),
    lambda s: s.job(choose_fam,construction_worker))
officeworker5 = Operator(print_fam + " applies for job: officer worker",
    lambda s: s.can_job(choose_fam, office_worker),
    lambda s: s.job(choose_fam,office_worker))
real_estate6 = Operator(print_fam + " applies for job: real estate agent",
    lambda s: s.can_job(choose_fam, real_estate),
    lambda s: s.job(choose_fam,real_estate))
doctor7 = Operator(print_fam + " applies for job: doctor",
    lambda s: s.can_job(choose_fam, doctor),
    lambda s: s.job(choose_fam, doctor))
caretaker8 = Operator(print_fam + " applies for job: care_taker",
    lambda s: s.can_job(choose_fam, care_taker),
    lambda s: s.job(choose_fam, care_taker))
teacher9 = Operator(print_fam + " applies for job: teacher",
    lambda s: s.can_job(choose_fam, teacher),
    lambda s: s.job(choose_fam, teacher))
nurse10 = Operator(print_fam + " applies for job: nurse",
    lambda s: s.can_job(choose_fam, nurse),
    lambda s: s.job(choose_fam, nurse))
secretary11 = Operator(print_fam + " applies for job: secretary",
    lambda s: s.can_job(choose_fam, secretary),
    lambda s: s.job(choose_fam, secretary))
#check contraints age and edu

#select entertainment 
family_park1 = Operator("Bring family to park",
    lambda s: s.can_pay(park),
    lambda s: s.entertainment(park))
family_circus2 = Operator("Bring family to circus",
    lambda s: s.can_pay(circus),
    lambda s: s.entertainment(cricus))
family_movie3 = Operator("Bring family to movies",
    lambda s: s.can_pay(movies),
    lambda s: s.entertainment(movies))
family_amusement4 = Operator("Bring family to amusement park",
    lambda s: s.can_pay(amusement_park),
    lambda s: s.entertainment(amusement_park))
family_vacation5 = Operator("Bring family to vacation abroad",
    lambda s: s.can_pay(vacation),
    lambda s: s.entertainment(vacation))

#select groceries
canned_goods1 = Operator("Buy canned goods for family to eat",
    lambda s: s.can_pay(canned_goods),
    lambda s: s.grocery(canned_goods))
microwavable_meals2 = Operator("Buy microwavable meals for family to eat",
    lambda s: s.can_pay(microwavable_meals),
    lambda s: s.grocery(microwavable_meals))
fresh_produce3 = Operator("Buy fresh produce for family to eat",
    lambda s: s.can_pay(fresh_produce),
    lambda s: s.grocery(fresh_produce))
take_out4 = Operator("Buy take out for family to eat",
    lambda s: s.can_pay(take_out),
    lambda s: s.grocery(take_out))
local_diner5 = Operator("Go to local diner with family",
    lambda s: s.can_pay(local_diner),
    lambda s: s.grocery(local_diner))
restaurant6 = Operator("Go to restaurant with family",
    lambda s: s.can_pay(restaurant),
    lambda s: s.grocery(restaurant))
fine_dinning7 = Operator("Go to fine dinning establishment with family",
    lambda s: s.can_pay(fine_dinning),
    lambda s: s.grocery(fine_dinning))
vitamins8 = Operator("Buy vitamins for family",
    lambda s: s.can_pay(vitamin),
    lambda s: s.grocery(vitamin))
medicine9 = Operator("Buy medicine for family",
    lambda s: s.can_pay(canned_goods),
    lambda s: s.grocery(canned_goods))

tent_city1 = Operator("Move to a tent city",
    lambda s: s.can_pay_housing(tent_city),
    lambda s: s.housing(tent_city))
trailer_park2 = Operator("Move to a trailer park",
    lambda s: s.can_pay_housing(trailer_park),
    lambda s: s.housing(trailer_park))
apartment3 = Operator("Move to a apartment",
    lambda s: s.can_pay_housing(apartment),
    lambda s: s.grocery(apartment))
duplex4 = Operator("Move to a duplex",
    lambda s: s.can_pay_housing(duplex),
    lambda s: s.grocery(duplex))
mansion5 = Operator("Move to a mansion",
    lambda s: s.can_pay_housing(mansion),
    lambda s: s.grocery(mansion))

level1_insurance1 = Operator("Buy level 1 insurance",
    lambda s: s.can_pay(level1_insurance),
    lambda s: s.insurance(level1_insurance))
level2_insurance2 = Operator("Buy level 2 insurance",
    lambda s: s.can_pay(level2_insurance),
    lambda s: s.insurance(level2_insurance))
level3_insurance3 = Operator("Buy level 3 insurance",
    lambda s: s.can_pay(level3_insurance),
    lambda s: s.insurance(level3_insurance))

#Next turn
next_turn = Operator("Next Turn (6 Months Pass)",
    lambda s: s.can_turn(),
    lambda s: s.turn())


OPERATORS = [intialstate_lower0, intialstate_middle1 , intialstate_upper2 , pick_father1 ,pick_mother2 ,pick_sister3 ,pick_brother4 ,publicschool1 ,privateschool2 ,homeschool3 , community_college4, public_university5, private_university6,vocationalschool7,garbagecollector2 ,truck_driver3 ,constructionworker4 ,officeworker5 ,real_estate6 ,doctor7 ,teacher9 ,nurse10 ,secretary11 ,family_park1 , family_circus2, family_movie3, family_amusement4, family_vacation5, canned_goods1, 
microwavable_meals2, fresh_produce3,take_out4, local_diner5, restaurant6, fine_dinning7,vitamins8,medicine9, tent_city1 ,trailer_park2,apartment3,duplex4,mansion5
, level1_insurance1, level2_insurance2, level3_insurance3, next_turn]
#</OPERATOR>
