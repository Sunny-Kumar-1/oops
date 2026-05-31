class chater:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = "false"
        self.menu()

    def menu(self):
        user_input = input("""welcome to chater how you want to proceed?
                            1.press 1 to sign up
                            2. press 2 to sign in 
                            3. press 3 to post
                            4. press 4 to send message
                            5. press 5 to exit""")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.my_msg()
        else:
            exit()
        
    def signup(self):
        email=input("enter email")
        password = input("enter password")
        self.username = email
        self.password = password
        print("singhed up successfully!!!")
        print("\n")
        self.menu()
    
    def signin(self): 
        if self.username=="" and self.password=="":
            print("signup first")
        else:
            email=input("enter email")
            password = input("enter password")
            if self.username == email and self.password == password:
                print("sign in successfully ")
                self.loggedin=True
            else:
                print("enter right credentials")
        self.menu()

    def my_msg(self):
        if self.loggedin == True:
            receiver= input("whom u wnat to msg")
            my_msg = input("emnter msg")
            print(f"msg sent to {receiver}")
        else:
            print("log in first")
        self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            post= input("what u wnat to post")
            print(f"posted sucessfully {post}")
        else:
            print("log in first")
        self.menu()

    @staticmethod
    def set_no(self):
        exit()


obj = chater()