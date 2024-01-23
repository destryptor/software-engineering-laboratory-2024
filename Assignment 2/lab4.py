from tkinter import *
from tkinter import messagebox

academic_unit_members = []


class Person:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.is_authenticated = False
        academic_unit_members.append(self)

    def authenticate(self, entered_password):
        if entered_password == self.password:
            self.is_authenticated = True
            return True
        return False

class Teacher(Person):
    def __init__(self, user_id, password, name, subject):
        super().__init__(user_id, password)
        self.name = name
        self.subject = subject

class Student(Person):
    def __init__(self, user_id, password, name, roll_no, birthday):
        super().__init__(user_id, password)
        self.name = name
        self.roll_no = roll_no
        self.birthday = birthday

class UG_student(Student):
    def __init__(self, user_id, password, name, roll_no, birthday):
        super().__init__(user_id, password, name, roll_no, birthday)
        self.type = "UG"

class PG_student(Student):
    def __init__(self, user_id, password, name, roll_no, birthday):
        super().__init__(user_id, password, name, roll_no, birthday)
        self.type = "PG"

def password_validator(password):
    if not (8 <= len(password) <= 12):
        return 501

    has_upper = False
    has_digit = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        return 502

    special_characters = set("!@#$%&*")
    if not any(char in special_characters for char in password):
        return 503

    if ' ' in password:
        return 504

    return True

class UserRegistrationGUI(Frame):
    def __init__(self, master, switch_gui):
        super().__init__(master)
        self.master = master
        self.master.title("User Registration")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID:")
        self.label_password = Label(self, text="Password:")
        self.label_user_type = Label(self, text="User Type:")

        self.entry_user_id = Entry(self)
        self.entry_password = Entry(self, show="*")
        self.entry_user_type = Entry(self)

        self.button_register = Button(self, text="Register", command=self.register_user)
        self.button_switch_to_sign_in = Button(self, text="Switch to Login", command=self.switch_to_sign_in)

        self.label_user_id.pack()
        self.entry_user_id.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.label_user_type.pack()
        self.entry_user_type.pack()
        self.button_register.pack()
        self.button_switch_to_sign_in.pack()

    def switch_to_sign_in(self):
        self.switch_gui(SignInGUI)

    def register_user(self):
        user_id = self.entry_user_id.get()
        password = self.entry_password.get()
        user_type = self.entry_user_type.get()

        validation_result = password_validator(password)

        if validation_result is not True:
            if validation_result == 501:
                messagebox.showerror("Error", "Password should be within 8-12 characters long.")
                return
            if validation_result == 502:
                messagebox.showerror("Error", "Password should contain at least one upper case, one digit, and one lower case.")
                return
            if validation_result == 503:
                messagebox.showerror("Error", "Password should contain one or more special character(s) from [! @ # $ % & *].")
                return
            if validation_result == 504:
                messagebox.showerror("Error", "Password should not contain blank spaces.")
                return

        if user_type.lower() == 'teacher':
            new_user = Teacher(user_id, password, "", "")
        elif user_type.lower() == 'ug':
            new_user = UG_student(user_id, password, "", "", "")
        elif user_type.lower() == 'pg':
            new_user = PG_student(user_id, password, "", "", "")
        else:
            messagebox.showerror("Error", "Invalid user type.")
            return

        messagebox.showinfo("Registration", "User registered successfully!")
        if user_type.lower() == 'teacher':
            self.switch_gui(TeacherProfileEditGUI, new_user)
        elif user_type.lower() == 'ug':
            self.switch_gui(UGStudentProfileEditGUI, new_user)
        elif user_type.lower() == 'pg':
            self.switch_gui(PGStudentProfileEditGUI, new_user)


class SignInGUI(Frame):
    def __init__(self, master, switch_gui):
        super().__init__(master)
        self.master = master
        self.master.title("Sign In")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID:")
        self.label_password = Label(self, text="Password:")

        self.entry_user_id = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.button_sign_in = Button(self, text="Sign In", command=self.sign_in)

        self.button_register = Button(self, text="Register", command=self.switch_to_register)

        self.label_user_id.pack()
        self.entry_user_id.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_sign_in.pack()
        self.button_register.pack()

    def switch_to_register(self):
        self.switch_gui(UserRegistrationGUI)

    def sign_in(self):
        user_id = self.entry_user_id.get()
        password = self.entry_password.get()

        for member in academic_unit_members:
            if member.id == user_id:
                if member.is_authenticated:
                    messagebox.showinfo("Sign In", "User is already authenticated.")
                else:
                    if member.authenticate(password):
                        messagebox.showinfo("Sign In", "Authentication successful!")
                        GUI_type = get_profile_edit_class(member)
                        if GUI_type == "Teacher":
                            self.switch_gui(TeacherProfileEditGUI, member)
                        elif GUI_type == "UGStudent":
                            self.switch_gui(UGStudentProfileEditGUI, member)
                        if GUI_type == "PGStudent":
                            self.switch_gui(PGStudentProfileEditGUI, member)
                    else:
                        messagebox.showerror("Sign In", "Authentication failed. Invalid password.")
                return

        messagebox.showerror("Sign In", "User not found.")

def get_profile_edit_class(user):
    if isinstance(user, Teacher):
        return "Teacher"
    elif isinstance(user, UG_student):
        return "UGStudent"
    elif isinstance(user, PG_student):
        return "PGStudent"

class TeacherProfileEditGUI(Frame):
    def __init__(self, master, switch_gui, teacher):
        super().__init__(master)
        self.master = master
        self.master.title("Teacher Profile Edit")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID:")
        self.label_name = Label(self, text="Name:")
        self.label_subject = Label(self, text="Subject:")

        self.entry_user_id = Entry(self)
        self.entry_name = Entry(self)
        self.entry_subject = Entry(self)

        self.button_update = Button(self, text="Update", command=self.update_profile)
        self.button_logout = Button(self, text="Log Out", command=self.logout)

        self.label_user_id.pack()
        self.entry_user_id.pack()
        self.label_name.pack()
        self.entry_name.pack()
        self.label_subject.pack()
        self.entry_subject.pack()
        self.button_update.pack()
        self.button_logout.pack()

        # Initialize fields with user data
        self.entry_user_id.insert(0, teacher.id)
        self.entry_name.insert(0, teacher.name)
        self.entry_subject.insert(0, teacher.subject)

    def update_profile(self):
        user_id = self.entry_user_id.get()
        name = self.entry_name.get()
        subject = self.entry_subject.get()

        for member in academic_unit_members:
            if member.id == user_id and isinstance(member, Teacher):
                member.name = name
                member.subject = subject

                messagebox.showinfo("Profile Update", "Profile updated successfully.")
                return

        messagebox.showerror("Profile Update", "User not found or not a teacher.")

    def logout(self):
        self.switch_gui(WelcomeGUI)


class UGStudentProfileEditGUI(Frame):
    def __init__(self, master, switch_gui, ug_student):
        super().__init__(master)
        self.master = master
        self.master.title("UG Student Profile Edit")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID:")
        self.label_name = Label(self, text="Name:")
        self.label_roll_no = Label(self, text="Roll No:")
        self.label_birthday = Label(self, text="Birthday:")

        self.entry_user_id = Entry(self)
        self.entry_name = Entry(self)
        self.entry_roll_no = Entry(self)
        self.entry_birthday = Entry(self)

        self.button_update = Button(self, text="Update", command=self.update_profile)

        self.button_logout = Button(self, text="Log Out", command=self.logout)

        self.label_user_id.pack()
        self.entry_user_id.pack()
        self.label_name.pack()
        self.entry_name.pack()
        self.label_roll_no.pack()
        self.entry_roll_no.pack()
        self.label_birthday.pack()
        self.entry_birthday.pack()
        self.button_update.pack()
        self.button_logout.pack()

        self.entry_user_id.insert(0, ug_student.id)
        self.entry_name.insert(0, ug_student.name)
        self.entry_roll_no.insert(0, ug_student.roll_no)
        self.entry_birthday.insert(0, ug_student.birthday)

    def update_profile(self):
        user_id = self.entry_user_id.get()
        name = self.entry_name.get()
        roll_no = self.entry_roll_no.get()
        birthday = self.entry_birthday.get()

        for member in academic_unit_members:
            if member.id == user_id and isinstance(member, UG_student):
                member.name = name
                member.roll_no = roll_no
                member.birthday = birthday

                messagebox.showinfo("Profile Update", "Profile updated successfully.")
                return

        messagebox.showerror("Profile Update", "User not found or not an UG student.")

    def logout(self):
        self.switch_gui(WelcomeGUI)

class PGStudentProfileEditGUI(Frame):
    def __init__(self, master, switch_gui, pg_student):
        super().__init__(master)
        self.master = master
        self.master.title("PG Student Profile Edit")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID:")
        self.label_name = Label(self, text="Name:")
        self.label_roll_no = Label(self, text="Roll No:")
        self.label_birthday = Label(self, text="Birthday:")

        self.entry_user_id = Entry(self)
        self.entry_name = Entry(self)
        self.entry_roll_no = Entry(self)
        self.entry_birthday = Entry(self)

        self.button_update = Button(self, text="Update", command=self.update_profile)

        self.button_logout = Button(self, text="Log out", command=self.logout)

        self.label_user_id.pack()
        self.entry_user_id.pack()
        self.label_name.pack()
        self.entry_name.pack()
        self.label_roll_no.pack()
        self.entry_roll_no.pack()
        self.label_birthday.pack()
        self.entry_birthday.pack()
        self.button_update.pack()
        self.button_logout.pack()

        self.entry_user_id.insert(0, pg_student.id)
        self.entry_name.insert(0, pg_student.name)
        self.entry_roll_no.insert(0, pg_student.roll_no)
        self.entry_birthday.insert(0, pg_student.birthday)

    def update_profile(self):
        user_id = self.entry_user_id.get()
        name = self.entry_name.get()
        roll_no = self.entry_roll_no.get()
        birthday = self.entry_birthday.get()

        for member in academic_unit_members:
            if member.id == user_id and isinstance(member, PG_student):
                member.name = name
                member.roll_no = roll_no
                member.birthday = birthday

                messagebox.showinfo("Profile Update", "Profile updated successfully.")
                return

        messagebox.showerror("Profile Update", "User not found or not a PG student.")

    def logout(self):
        self.switch_gui(WelcomeGUI)

class WelcomeGUI(Frame):
    def __init__(self, master, switch_gui):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome to the Academic Unit")

        self.switch_gui = switch_gui

        self.label_welcome = Label(self, text="Welcome to the Academic Section.")
        self.label_select = Label(self, text="Select any of the following to proceed:")
        self.button_login = Button(self, text="Login", command=self.login)
        self.button_register = Button(self, text="Register", command=self.register)

        self.label_welcome.pack()
        self.label_select.pack()
        self.button_login.pack()
        self.button_register.pack()

    def login(self):
        self.switch_gui(SignInGUI)

    def register(self):
        self.switch_gui(UserRegistrationGUI)

class MainApplication(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Academic Unit System")

        self.current_frame = None

        self.show_frame(WelcomeGUI)

    def show_frame(self, frame_class, *args):
        new_frame = frame_class(self, self.switch_frame, *args)
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = new_frame
        self.current_frame.pack()

    def switch_frame(self, frame_class, *args):
        self.show_frame(frame_class, *args)


if __name__ == "__main__":
    app = MainApplication()
    app.geometry("400x300")
    app.mainloop()
