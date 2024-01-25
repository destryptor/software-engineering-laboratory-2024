from tkinter import *
from tkinter import messagebox

academic_unit_members = []

class StyledFrame(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

class Person:
    def __init__(self, id, password, is_authenticated=None, is_active=None, valid_attempts=None):
        self.id = id
        self.password = password
        self.is_authenticated = is_authenticated if is_authenticated is not None else False
        self.is_active = is_active if is_active is not None else True
        self.valid_attempts = valid_attempts if valid_attempts is not None else 3
        academic_unit_members.append(self)

    def authenticate(self, entered_password):
        if entered_password == self.password:
            self.is_authenticated = True
            return True
        return False

class Teacher(Person):
    def __init__(self, user_id, password, name, subject, is_authenticated=None, is_active=None, valid_attempts=None):
        super().__init__(user_id, password, is_authenticated, is_active, valid_attempts)
        self.name = name
        self.subject = subject
        self.type = "Teacher"

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
            'subject': self.subject,
            'type': self.type
        })
        return base_dict

class Student(Person):
    def __init__(self, user_id, password, name, roll_no, birthday,  is_authenticated, is_active, valid_attempts):
        super().__init__(user_id, password, is_authenticated, is_active, valid_attempts)
        self.name = name
        self.roll_no = roll_no
        self.birthday = birthday

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
            'roll_no': self.roll_no,
            'birthday': self.birthday
        })
        return base_dict
    
class UG_student(Student):
    def __init__(self, user_id, password, name, roll_no, birthday, is_authenticated=None, is_active=None, valid_attempts=None):
        super().__init__(user_id, password, name, roll_no, birthday, is_authenticated, is_active, valid_attempts)
        self.type = "UG Student"

class PG_student(Student):
    def __init__(self, user_id, password, name, roll_no, birthday,is_authenticated=None, is_active=None, valid_attempts=None):
        super().__init__(user_id, password, name, roll_no, birthday, is_authenticated, is_active, valid_attempts)
        self.type = "PG Student"

def email_validator(email):
    if '@' not in email:
        return False
    if email.count('@') > 1:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True


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

def load_data_from_file():
    try:
        with open("academic_data.txt", "r") as file:
            data = file.read().split('\n\n')  # Split data into chunks based on extra line
            for chunk in data:
                if not chunk.strip():
                    continue  # Skip empty chunks

                user_data = chunk.strip().split('\n')
                user_type, *attributes = user_data

                if user_type.lower() == 'teacher':
                    new_user = Teacher(**parse_attributes(attributes), is_authenticated=False)
                elif user_type.lower() == 'ug student':
                    new_user = UG_student(**parse_attributes(attributes))
                elif user_type.lower() == 'pg student':
                    new_user = PG_student(**parse_attributes(attributes), is_authenticated=False)
                else:
                    print(f"Invalid user type: {user_type}")

    except FileNotFoundError:
        print("No data file found. Starting with an empty list.")

def parse_attributes(attributes):
    parsed_attributes = {}
    for attr in attributes:
        key_value = list(map(str.strip, attr.split(':')))
        key, value = key_value[0], key_value[1] if len(key_value) > 1 else ""
        parsed_attributes[key] = value

    return parsed_attributes

def save_data_to_file():
    with open('academic_data.txt', 'w') as file:
        for member in academic_unit_members:
            if isinstance(member, Teacher):
                user_type = 'Teacher'
            elif isinstance(member, UG_student):
                user_type = 'UG Student'
            elif isinstance(member, PG_student):
                user_type = 'PG Student'
            else:
                continue

            common_fields = [f'{user_type}', f'user_id:{member.id}', f'password:{member.password}', f'name:{member.name}']
            additional_fields = [f'{key}:{getattr(member, key)}' for key in member.__dict__.keys() if key not in ['type', 'id', 'password', 'name', 'is_authenticated']]

            user_data = '\n'.join(common_fields + additional_fields)
            file.write(user_data + '\n\n')

class UserRegistrationGUI(StyledFrame):
    def __init__(self, master, switch_gui):
        super().__init__(master)
        self.master = master
        self.master.title("User Registration")

        self.switch_gui = switch_gui

        self.label_user_id = Label(self, text="User ID (Must be your current active email):")
        self.label_password = Label(self, text="Password:")
        self.label_user_type = Label(self, text="User Type:")

        self.entry_user_id = Entry(self)
        self.entry_password = Entry(self, show="*")
        self.user_type_var = StringVar()
        self.user_type_var.set("")

        self.teacher_radio = Radiobutton(self, text="Teacher", variable=self.user_type_var, value="teacher")
        self.ug_radio = Radiobutton(self, text="UG Student", variable=self.user_type_var, value="ug")
        self.pg_radio = Radiobutton(self, text="PG Student", variable=self.user_type_var, value="pg")


        self.button_register = Button(self, text="Register", command=self.register_user)
        self.button_switch_to_sign_in = Button(self, text="Switch to Login", command=self.switch_to_sign_in)

        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.label_user_type.pack(pady=5)
        self.teacher_radio.pack(pady=2)
        self.ug_radio.pack(pady=2)
        self.pg_radio.pack(pady=2)
        self.button_register.pack(pady=10)
        self.button_switch_to_sign_in.pack(pady=5)

    def switch_to_sign_in(self):
        self.switch_gui(SignInGUI)

    def register_user(self):
        user_id = self.entry_user_id.get()
        password = self.entry_password.get()
        user_type = self.user_type_var.get()

        email_validation = email_validator(user_id)
        validation_result = password_validator(password)

        if email_validation is not True:
            messagebox.showerror("Error", "Username should be a valid email.")

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
            new_user = Teacher(user_id, password, "", "", False, True, 3)
        elif user_type.lower() == 'ug':
            new_user = UG_student(user_id, password, "", "", "", False, True, 3)
        elif user_type.lower() == 'pg':
            new_user = PG_student(user_id, password, "", "", "", False, True, 3)
        else:
            messagebox.showerror("Error", "Invalid user type.")
            return
        
        save_data_to_file()

        messagebox.showinfo("Registration", "User registered successfully!")
        if user_type.lower() == 'teacher':
            self.switch_gui(TeacherProfileEditGUI, new_user)
        elif user_type.lower() == 'ug':
            self.switch_gui(UGStudentProfileEditGUI, new_user)
        elif user_type.lower() == 'pg':
            self.switch_gui(PGStudentProfileEditGUI, new_user)


class SignInGUI(StyledFrame):
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

        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_sign_in.pack(pady=10)
        self.button_register.pack(pady=5)

    def switch_to_register(self):
        self.switch_gui(UserRegistrationGUI)

    def sign_in(self):
        user_id = self.entry_user_id.get()
        password = self.entry_password.get()

        for member in academic_unit_members:
            if member.id == user_id:
                if member.is_active:
                    if member.is_authenticated:
                        messagebox.showinfo("Sign In", "User is already authenticated.")
                    else:
                        if member.authenticate(password):
                            member.is_authenticated = True
                            messagebox.showinfo("Sign In", "Authentication successful!")
                            GUI_type = get_profile_edit_class(member)
                            if GUI_type == "Teacher":
                                self.switch_gui(TeacherProfileEditGUI, member)
                            elif GUI_type == "UGStudent":
                                self.switch_gui(UGStudentProfileEditGUI, member)
                            if GUI_type == "PGStudent":
                                self.switch_gui(PGStudentProfileEditGUI, member)
                        else:
                            member.valid_attempts -= 1
                            if member.valid_attempts > 1:
                                messagebox.showerror("Sign In", f"Invalid password. {member.valid_attempts} attempts remaining.")
                            elif member.valid_attempts == 1:
                                messagebox.showerror("Sign In", f"Invalid password. {member.valid_attempts} attempt remaining.")
                            else:
                                member.is_active = False
                                messagebox.showerror("Sign In", "User account deactivated due to too many incorrect password attempts.")
                    return
                else:
                    messagebox.showerror("Sign In", "User account deactivated due to too many incorrect password attempts.")
                    return
        messagebox.showerror("Sign In", "User not found.")

def get_profile_edit_class(user):
    if isinstance(user, Teacher):
        return "Teacher"
    elif isinstance(user, UG_student):
        return "UGStudent"
    elif isinstance(user, PG_student):
        return "PGStudent"

class TeacherProfileEditGUI(StyledFrame):
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
        self.button_deregister = Button(self, text="Deregister your account", command=self.deregister)

        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_subject.pack(pady=5)
        self.entry_subject.pack(pady=5)
        self.button_update.pack(pady=10)
        self.button_logout.pack(pady=5)
        self.button_deregister.pack(pady=5)

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
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, Teacher):
                member.is_authenticated = False
                break
        self.switch_gui(WelcomeGUI)

    def deregister(self):
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, Teacher):
                academic_unit_members.remove(member)
                messagebox.showinfo("Deregister", "Account deregistered successfully.")
                self.switch_gui(SignInGUI)

class UGStudentProfileEditGUI(StyledFrame):
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
        self.button_deregister = Button(self, text="Deregister your account", command=self.deregister)

        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_roll_no.pack(pady=5)
        self.entry_roll_no.pack(pady=5)
        self.label_birthday.pack(pady=5)
        self.entry_birthday.pack(pady=5)
        self.button_update.pack(pady=10)
        self.button_logout.pack(pady=5)
        self.button_deregister.pack(pady=5)

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
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, UG_student):
                member.is_authenticated = False
                break
        self.switch_gui(WelcomeGUI)

    def deregister(self):
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, UG_student):
                academic_unit_members.remove(member)
                messagebox.showinfo("Deregister", "Account deregistered successfully.")
                self.switch_gui(SignInGUI)

class PGStudentProfileEditGUI(StyledFrame):
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
        self.button_deregister = Button(self, text="Deregister your account", command=self.deregister)

        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_roll_no.pack(pady=5)
        self.entry_roll_no.pack(pady=5)
        self.label_birthday.pack(pady=5)
        self.entry_birthday.pack(pady=5)
        self.button_update.pack(pady=10)
        self.button_logout.pack(pady=5)
        self.button_deregister.pack(pady=5)

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
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, PG_student):
                member.is_authenticated = False
                break
        self.switch_gui(WelcomeGUI)

    def deregister(self):
        for member in academic_unit_members:
            if member.id == self.entry_user_id.get() and isinstance(member, PG_student):
                academic_unit_members.remove(member)
                messagebox.showinfo("Deregister", "Account deregistered successfully.")
                self.switch_gui(SignInGUI)

class WelcomeGUI(StyledFrame):
    def __init__(self, master, switch_gui):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome to the Academic Unit")

        self.switch_gui = switch_gui

        self.label_welcome = Label(self, text="Welcome to the Academic Section.")
        self.label_select = Label(self, text="Select any of the following to proceed:")
        self.button_login = Button(self, text="Login", command=self.login)
        self.button_register = Button(self, text="Register", command=self.register)

        self.label_welcome.pack(pady=10)
        self.label_select.pack(pady=5)
        self.button_login.pack(pady=5)
        self.button_register.pack(pady=5)

    def login(self):
        self.switch_gui(SignInGUI)

    def register(self):
        self.switch_gui(UserRegistrationGUI)

def on_exit():
    save_data_to_file()
    app.destroy()

class MainApplication(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Academic Unit System")

        self.protocol("WM_DELETE_WINDOW", on_exit)

        load_data_from_file()

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
