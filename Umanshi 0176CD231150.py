#Name: Umanshi Gupta
#Enrollment: 0176CD231150
#Batch: 2027
import random

record = {}
with open('userdata.txt', 'r') as file:
    for line in file:
            parts = line.strip().split('|')
            if len(parts) == 8:
                username = parts[0]
                record[username] = {'username': parts[0], 'password': parts[1], 'name': parts[2], 'email': parts[3], 'contact': parts[4], 'course': parts[5], 'college': parts[6], 'city': parts[7]}

logged_user = ''
logged = False

def register():
    print("__REGISTRATION PAGE__")
    global record
    username=input("Enter your username: ").lower()
    if username in record:
        print("Username already exists")
    else:
        password = input("Enter password: ")
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        contact= int(input("Enter you contact number: "))
        course=input("Enter you course name: ")
        college= input("Enter the name of your college: ")
        city= input("Enter your city: ")
        record[username] = {'username': username, 'password': password, 'name': name, 'email': email, 'contact': contact, 'course': course, 'college': college, 'city': city }
        print("Registration successful!")
        with open('userdata.txt', 'a') as file:
            file.write(f"{username}|{password}|{name}|{email}|{contact}|{course}|{college}|{city}\n")
        record[username] = {'username': username, 'password': password, 'name': name, 'email': email, 'contact': contact, 'course': course, 'college': college, 'city': city }
    login()

def login():
    global logged_user
    global logged
    if logged== True:
        print("You're already logged in")
    print("__LOGIN PAGE__")
    user=input("Enter your username:").lower()
    if user in record:
        pas=input("Enter your password: ")
        if pas==record[user]['password']:
            logged_user= user
            logged= True
            mains()
        else:
            print("Invalid password")
            login()
    else:
        print("Username doesn't exist, please check or register!")
        main()

def show_profile():
    if logged== False:
        print("Please login/register first")
        main()
    else:
        user =record[logged_user]
        print("__STUDENT PROFILE__")
        print(f"Username: {user['username']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Contact: {user['contact']}")
        print(f"Course: {user['course']}")
        print(f"College: {user['college']}")
        print(f"City: {user['city']}")
        mains()
        
def update_profile():
    if logged== False:
        print("Please login/register first")
        main()
    else:
        print("__STUDENT PROFILE__")
        user =record[logged_user]
        res=input("Enter what to update: ").lower()
        if res=='username':
            '''new=input("Enter your username: ").lower()
            if new in record:'''
            print("Username can't be changed")
            user=new
        elif res=='name':
            user['name'] = input("Enter new name: ")
        elif res=='email':
            user['email'] = input("Enter new email: ")
        elif res=='contact':
            user['contact'] = int(input("Enter new contact number: "))
        elif res=='course':
            user['course'] = input("Enter new course: ")
        elif res=='college':
            user['college'] = input("Enter new college: ")
        elif res=='city':
            user['city'] = input("Enter new city: ")
        else:
            print("Invalid input")
        print("Profile updated successfully!")
        with open('userdata.txt', 'r') as f:
            lines = f.readlines()
        with open('userdata.txt', 'w') as f:
            for line in lines:
                if line.startswith(logged_user + '|'):
                    u = record[logged_user]
                    line = f"{u['username']}|{u['password']}|{u['name']}|{u['email']}|{u['contact']}|{u['course']}|{u['college']}|{u['city']}\n"
                f.write(line)
        
        show_profile()
            
def logout():
    global logged
    global logged_user
    conf=input("Are you sure you want to logout (Yes/No): ").lower()
    if conf=='yes':
        logged= False
        logged_user= ''
        print("_LOGGED OUT_")
        main()
    else:
        mains()
    
def terminate():
    exit()

def quiz():
    score=0
    questions=[]
    print("__QUIZ SECTION__")
    subject = input("Enter subject (DSA/DBMS/OOPM): ").upper()
    print("Answer the following questions")
    with open("quiz.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        parts = line.strip().split('|')
        if subject== parts[0]:
            questions.append(parts)
    random.shuffle(questions)
    ask = questions[:5]
    for q in ask:
        print(f"Q: {q[1]}")
        print(f"1. {q[2]}")
        print(f"2. {q[3]}")
        print(f"3. {q[4]}")
        print(f"4. {q[5]}")
        ans = int(input("Enter your answer (1/2/3/4): "))
        if ans in [1,2,3,4]:
            if q[ans+1]==q[6]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q[6]}")
        else:
            print("Invalid choice! Skipping this question.")
    print(f" You scored {score}/5")

def mains():
    print("__STUDENT DASHBOARD__")
    response = input('''
        Choose option:
        1. Attempt Quiz
        2. Show profile
        3. Update profile
        4. Logout
        5. Main Menu
        6. Exit

            select option 1/2/3/4/5/6: ''')
    if response == '1':
        quiz()
    elif response == '2':
        show_profile()
    elif response == '3':
        update_profile()
    elif response == '4':
        if logged==True:
            logout()
        main()
    elif response == '5':
        main()
    elif response == '6':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        mains()

def main():
    print("__STUDENT REGISTRATION SYSTEM__")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Main Menu
        4. Exit

            select option 1/2/3/4: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        main()
    elif response == '4':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()
main()


        
    
    
