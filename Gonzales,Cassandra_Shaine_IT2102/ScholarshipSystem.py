import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import webbrowser, datetime
import mysql.connector

admin_username = "useradmin" 
admin_password = "adminpass"

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Scholar_DB"
    )

def ask_account():
    response = messagebox.askyesno("Account", "Do you have an account?")
    if response:
        re_enter_label.place_forget()
        re_enter.place_forget()
        signup_button.place_forget()
        login_button.place(relx=1.0, x=-115, y=300, anchor="e")
    else:
        re_enter_label.place(relx=1.0, x=-70, y=300, anchor="e")
        re_enter.place(relx=1.0, x=-45, y=330, width=200, anchor="e")
        signup_button.place(relx=1.0, x=-115, y=400, anchor="e")

def validate_login():
    if not entry_user.get() or not entry_pass.get():  
        messagebox.showerror("Error", "Please fill out both username and password.")
    else: 
        if entry_user.get() == admin_username and entry_pass.get() == admin_password: 
            new_admin_window()
        else:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT userid FROM accounts WHERE username=%s AND password=%s", (entry_user.get(), entry_pass.get()))  
            result = cursor.fetchone()
            conn.close()
            if result:
                userid = result[0]  
                open_new_window(userid)
            else:
                messagebox.showerror("Error", "Invalid credentials")


def signup_confirmation():
    if not entry_user.get() or not entry_pass.get() or not re_enter.get():
        messagebox.showerror("Error", "Please fill out all fields.")
    elif entry_pass.get() == re_enter.get():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username=%s", (entry_user.get(),))
        result = cursor.fetchone()
        if result:
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        else:
            cursor.execute("INSERT INTO accounts (username, password) VALUES (%s, %s)", (entry_user.get(), entry_pass.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sign Up", "Account created!")
            re_enter.place_forget()
            re_enter_label.place_forget()
            signup_button.place_forget()
            login_button.place(relx=1.0, x=-115, y=300, anchor="e")
    else:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")

def open_new_window(userid):
    new_window = tk.Toplevel(root)
    new_window.geometry("1000x600")
    new_window.title("Welcome")
    new_window.configure(bg="#cddafd")
    
        
    tk.Label(new_window, text="What do you want to do today?", font=("Helvetica", 30), fg="#001F3F",bg="#cddafd").pack(pady=20)

    application_button = tk.Button(new_window, text="Application", command=lambda: check_application(userid), bg="#001F3F", fg="white", font=("Helvetica", 30, "bold"))
    application_button.place(relx=0.5, y=200, anchor="center")

    status_button = tk.Button(new_window, text="Check Status", command=lambda: status_window(userid), bg="#3A6D8C", fg="white", font=("Helvetica", 30, "bold"))
    status_button.place(relx=0.5, y=300, anchor="center")

    check_schedule_button = tk.Button(new_window, text="Check Schedule", command=lambda: sched_confirmation(userid), bg="#6A9AB0", fg="white", font=("Helvetica", 30, "bold"))
    check_schedule_button.place(relx=0.5, y=400, anchor="center")

    tk.Label(new_window, text="DREAMS TO DEGREES: Iskolar ng Batangas", font=("Helvetica", 20), fg="#001F3F",bg="#cddafd").place(relx=0.5, y=550, anchor="center")

def existing_application(userid):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM application WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def check_application(userid):
    if existing_application(userid):
        messagebox.showinfo("Application Status", "Application already submitted.")
    else:
        application_window(userid)

def application_window(userid):
    app_window = tk.Toplevel(root)
    app_window.geometry("1000x600")
    app_window.title("For Application")
    app_window.configure(bg="white")

    frame_right = tk.Frame(app_window, bg="#001F3F", width=500)
    frame_right.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    tk.Label(app_window, text="Fill out the needed fields", font=("Helvetica", 30),bg="white").place(x=40, y=35)

    tk.Label(app_window, text="(Surname, First Name, Middle Initial)", font=("Helvetica", 12),bg="white").place(x=120, y=120)
    tk.Label(app_window, text="Full Name", font=("Helvetica", 16),bg="white").place(x=10, y=140)
    name_application = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=30)
    name_application.place(x=110, y=145)

    tk.Label(app_window, text="YYYY-MM-DD", font=("Helvetica", 12),bg="white").place(x=125, y=173)
    tk.Label(app_window, text="Birthday", font=("Helvetica", 16),bg="white").place(x=10, y=190)
    birthday_application = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=20)
    birthday_application.place(x=115, y=195)

    tk.Label(app_window, text="Address", font=("Helvetica", 16),bg="white").place(x=10, y=240)
    address_application = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=30)
    address_application.place(x=110, y=245)

    tk.Label(app_window, text="Email", font=("Helvetica", 16),bg="white").place(x=10, y=295)
    email_application = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=30)
    email_application.place(x=110, y=300)

    tk.Label(app_window, text="School", font=("Helvetica", 16),bg="white").place(x=10, y=345)
    school_application = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=30)
    school_application.place(x=110, y=350)

    level_label = tk.Label(app_window, text="Level", font=("Helvetica", 16),bg="white")
    level_label.place(x=10, y=380)
    level = tk.StringVar(app_window)
    level.set("Select Level")
    level_menu = tk.OptionMenu(app_window, level, "High School", "College")
    level_menu.place(x=10, y=410)

    grade_level_label = tk.Label(app_window, text="Year/Grade Level", font=("Helvetica", 16),bg="white")
    grade_level_label.place(x=140, y=380)
    grade_level = tk.StringVar(app_window)
    grade_level.set("Select Year/Grade Level")
    grade_level_menu = tk.OptionMenu(app_window, grade_level, "1st Year", "2nd Year", "3rd Year", "4th Year", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12")
    grade_level_menu.place(x=140, y=410)

    tk.Label(app_window, text="(If in High School write N/A)", font=("Helvetica", 12),bg="white").place(x=125, y=460)
    tk.Label(app_window, text="Program", font=("Helvetica", 16),bg="white").place(x=10, y=480)
    program = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=30)
    program.place(x=110, y=485)

    tk.Label(app_window, text="G.W.A.", font=("Helvetica", 16),bg="white").place(x=10, y=520)
    gwa_grades = tk.Entry(app_window, bg="#e0e0e0", font=("Helvetica", 16), width=10)
    gwa_grades.place(x=110, y=525)

    tk.Label(app_window, text="INSTRUCTIONS:", font=("Helvetica", 16), bg="#001F3F", fg="white").place(relx=0.75, y=60, anchor="center")
    tk.Label(app_window, text="Compile all the needed Requirements and\nsave it in one pdf file.", font=("Helvetica", 16), bg="#001F3F", fg="white").place(relx=0.75, y=150, anchor="center")
    tk.Label(app_window, text="- Last Semester's Grade\n- Enrollment Form\n- Copy of Latest School ID", font=("Helvetica", 16), bg="#001F3F", fg="white").place(relx=0.75, y=250, anchor="center")
    requirements = tk.Entry(app_window, bg="#001F3F", font=("Helvetica", 16), width=30)
    requirements.place(relx=0.75, y=350, anchor="center")

    def upload_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            requirements.delete(0, tk.END)
            requirements.insert(0, file_path)

    def view_pdf():
        file_path = requirements.get()
        if file_path:
            webbrowser.open(file_path)

    tk.Button(app_window, text="Upload PDF", command=upload_pdf, bg="#3A6D8C", fg="white", font=("Helvetica", 12)).place(relx=0.75, y=400, anchor="center")
    tk.Button(app_window, text="View", command=view_pdf, bg="#3A6D8C", fg="white", font=("Helvetica", 12)).place(relx=0.75, y=440, anchor="center")

    def save_application(userid):
        conn = connect_db()
        cursor = conn.cursor()
        current_date = datetime.date.today()

        if not messagebox.askyesno("Confirmation", "I hereby certify that all the information provided is true and accurate"):
            return

        cursor.execute(
            "INSERT INTO Students (full_name, birthday, address, email) VALUES (%s, %s, %s, %s)",
            (name_application.get(), birthday_application.get(), address_application.get(), email_application.get())
        )
        studentid = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Application (userid, studentid, full_name, birthday, address, email, school, level, grade_level, program, gwa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (userid, studentid, name_application.get(), birthday_application.get(), address_application.get(), email_application.get(), school_application.get(), level.get(), grade_level.get(), program.get(), gwa_grades.get())
        )
        application_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Payout (ApplicationID, userid ,full_name, Application_Date, Approval_Date, Status, Payout_Date) VALUES (%s,%s, %s, %s, %s, %s, %s)",
            (application_id, userid, name_application.get(), current_date, None, 'Pending', None)
        )

        conn.commit()
        conn.close()
        messagebox.showinfo("Info", "Application Submitted!")

    tk.Button(app_window, text="Submit", font=("Helvetica", 12), command=lambda: save_application(userid), bg="green", fg="white").place(relx=0.75, y=500, anchor="center")

def status_window(userid):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM payout WHERE UserID = %s", (userid,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            app_window = tk.Toplevel(root)
            app_window.geometry("350x200")
            app_window.title("Application Status")
            app_window.configure(bg="#cddafd")

            status = result[0]
            if status == "Accepted":
                tk.Label(app_window, text="Congratulations! \nYour application has been \napproved.", 
                         font=("Helvetica", 16), fg="green", bg="#cddafd").pack(pady=10)
                tk.Label(app_window, text="You may now check the \nschedule of your payout", 
                         font=("Helvetica", 12), fg="black", bg="#cddafd").pack(pady=10)
            elif status == "Rejected":
                tk.Label(app_window, text="We regret to inform you \nthat your application\n has been rejected.", 
                         font=("Helvetica", 16), fg="red", bg="#cddafd").pack(pady=10)
            else:
                tk.Label(app_window, text="Your application is still \npending. Please check back later.", 
                         font=("Helvetica", 16), fg="orange", bg="#cddafd").pack(pady=10)
                tk.Label(app_window, text="Make sure to check your \nemail to see if there are revisions needed", 
                         font=("Helvetica", 12), fg="black", bg="#cddafd").pack(pady=10)
        else:
            messagebox.showerror("Error", "No application found for this user.")
    
    except mysql.connector.Error as db_error:
        messagebox.showerror("Database Error", f"An error occurred while accessing the database:\n{db_error}")
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{ex}")


def sched_confirmation(userid):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM payout WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    conn.close()

    if result:
        status = result[0]
        if status == "Accepted":
            check_sched(userid)
        elif status == "Rejected":
            messagebox.showerror("Error", "Your application has been rejected.")
        elif status == "Pending":
            messagebox.showerror("Error", "Your application is still pending. Please check back later.")
        else:
            messagebox.showerror("Error", "Unknown application status.")
    else:
        messagebox.showerror("Error", "No application found for this user.")

def check_sched(userid):
    app_window = tk.Toplevel(root)
    app_window.geometry("400x150")
    app_window.title("Schedule")
    app_window.config(bg="#cddafd")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT approval_date FROM payout WHERE userid = %s", (userid,))
    result = cursor.fetchone()
    conn.close()

    if result:
        approval_date = result[0]
        payout_date = approval_date + datetime.timedelta(days=3) 

        schedule_label = tk.Label(app_window, text=f"Payout Date: {payout_date}", font=("Helvetica", 14), bg="#cddafd")
        schedule_label.pack(pady=20)

        schedule_label = tk.Label(app_window, text=f"You may now claim your scholarship grant\n from this date onwards", font=("Helvetica", 14, ), bg="#cddafd")
        schedule_label.pack(pady=20)
        
    else:
        schedule_label = tk.Label(app_window, text="No schedule found for this user.", font=("Helvetica", 14), bg="#cddafd")
        schedule_label.pack(pady=20)

def new_admin_window():
    admin_window = tk.Toplevel(root)
    admin_window.geometry("1000x500")
    admin_window.title("Admin Panel")
    admin_window.config(bg="#669bbc")


    frame = tk.Frame(admin_window, bg="#669bbc")
    frame.place(x=20, y=0, width=960, height=400)

    tree = ttk.Treeview(frame, columns=("full_name", "birthday", "address", "email", "school", "level", "grade_level", "gwa"), show="headings")
    tree.place(x=0, y=0, width=900, height=400)

    tree.column("full_name", width=160, anchor=tk.W)
    tree.column("birthday",  width=60, anchor=tk.CENTER)
    tree.column("address",  width=80, anchor=tk.W)
    tree.column("email",  width=130, anchor=tk.W)
    tree.column("school",  width=130, anchor=tk.W)
    tree.column("level",  width=60, anchor=tk.CENTER)
    tree.column("grade_level",  width=60, anchor=tk.CENTER)
    tree.column("gwa",  width=50, anchor=tk.CENTER)

    tree.heading("full_name", text="Full Name", anchor=tk.CENTER)
    tree.heading("birthday", text="Birthday", anchor=tk.CENTER)
    tree.heading("address", text="Address", anchor=tk.CENTER)
    tree.heading("email", text="Email", anchor=tk.CENTER)
    tree.heading("school", text="School", anchor=tk.CENTER)
    tree.heading("level", text="Level", anchor=tk.CENTER)
    tree.heading("grade_level", text="Grade Level", anchor=tk.CENTER)
    tree.heading("gwa", text="GWA", anchor=tk.CENTER)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT applicationid, full_name, birthday, address, email, school, level, grade_level, gwa FROM application")

    rows = cursor.fetchall()
    conn.close()

    button_refs = {}

    for i, row in enumerate(rows):
        applicationid = row[0]  
        tree.insert("", tk.END, iid=applicationid, values=row[1:])  

        button_frame = tk.Frame(frame, bg="#669bbc")
        button_frame.place(x=905, y=23 + i * 20, width=60, height=20)

        approve_btn = tk.Button(button_frame, text="/", command=lambda id=applicationid: confirm_approval(applicationid), fg="green")
        reject_btn = tk.Button(button_frame, text="X", command=lambda id=applicationid: confirm_rejection(applicationid), fg="red")
        approve_btn.pack(side=tk.LEFT)
        reject_btn.pack(side=tk.RIGHT)
        button_refs[applicationid] = (approve_btn, reject_btn)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    exit_button = tk.Button(admin_window, text="exit", command=admin_window.destroy, font=("Helvetica", 12), bg="#0077b6", fg="white", width=20)
    exit_button.place(relx=0.5, y=450, anchor=tk.CENTER)

def confirm_rejection(applicationid):
    try:
        result = messagebox.askyesno("Confirm Rejection", "Are you sure you want to reject this application?")
        if result:
            reject_application(applicationid)
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{ex}")

def confirm_approval(applicationid):
    try:
        result = messagebox.askyesno("Confirm Approval", "Are you sure you want to approve this application?")
        if result:
            approve_application(applicationid)
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{ex}")

def approve_application(applicationid):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        approved_date = datetime.date.today()
        payout_date = approved_date + datetime.timedelta(days=3)

        cursor.execute(
            "UPDATE payout SET status = 'Accepted', approval_date = %s, payout_date = %s WHERE applicationid = %s",
            (approved_date, payout_date, applicationid)
        )
        conn.commit()

        cursor.execute("SELECT status, approval_date, payout_date FROM payout WHERE applicationid = %s", (applicationid,))
        result = cursor.fetchone()
        conn.close()

        if result and result[0] == "Accepted":
            messagebox.showinfo("Success", f"Application {applicationid} approved successfully!\nPayout Date: {result[2]}")
        else:
            messagebox.showwarning("Warning", f"Failed to update the status for application {applicationid}.")
    except mysql.connector.Error as db_error:
        messagebox.showerror("Database Error", f"An error occurred while accessing the database:\n{db_error}")
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{ex}")

import mysql.connector
from tkinter import messagebox

def reject_application(applicationid):
    if not applicationid:
        messagebox.showwarning("Warning", "Application ID cannot be empty!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE payout SET status = 'Rejected' WHERE applicationid = %s",
            (applicationid,)
        )
        conn.commit()

        cursor.execute(
            "SELECT status, payout_date FROM payout WHERE applicationid = %s",
            (applicationid,)
        )
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result and result[0] == "Rejected":
            messagebox.showinfo("Success", f"Application {applicationid} rejected successfully!\nPayout Date: {result[1]}")
        else:
            messagebox.showwarning("Warning", f"Failed to update the status for application {applicationid}.")
    except mysql.connector.Error as db_error:
        messagebox.showerror("Database Error", f"An error occurred while accessing the database:\n{db_error}")
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{ex}")


root = tk.Tk()
root.geometry("1000x600")
root.title("Login / Sign Up")
root.config(bg="white")

font_style = ("Helvetica", 12)

frame_left = tk.Frame(root, bg="#001F3F", width=200)
frame_left.place(relwidth=0.7, relheight=1)

image = Image.open("dreams.png")
image = image.resize((600, 600))
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(frame_left, image=image_tk, bg="#001F3F")
image_label.place(relwidth=1.0, relheight=1.0)

tk.Label(root, text="Username", bg="white", font=font_style).place(relx=1.0, x=-105, y=160, anchor="e")
entry_user = tk.Entry(root, bg="#e0e0e0", font=font_style)
entry_user.place(relx=1.0, x=-45, y=190, width=200, anchor="e")

tk.Label(root, text="Password", bg="white", font=font_style).place(relx=1.0, x=-105, y=230, anchor="e")
entry_pass = tk.Entry(root, show="*", bg="#e0e0e0", font=font_style)
entry_pass.place(relx=1.0, x=-45, y=260, width=200, anchor="e")

re_enter_label = tk.Label(root, text="Re-Enter Password", bg="white", font=font_style)
re_enter_label.place_forget()
re_enter = tk.Entry(root, show="*", bg="#e0e0e0", font=font_style)
re_enter.place_forget()

signup_button = tk.Button(root, text="Sign Up", command=signup_confirmation, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
signup_button.place_forget()
login_button = tk.Button(root, text="Login", command=validate_login, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
login_button.place_forget()

root.after(100, ask_account)
root.mainloop()
