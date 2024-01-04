import tkinter 
from tkinter import messagebox 
import mysql.connector 
 
def create_table(): 
    db_connection = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="", 
        database="student_registration" 
    ) 
 
    cursor = db_connection.cursor() 
 
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS student_info ( 
            Name CHAR(30), 
            Email CHAR(30), 
            Age INT(2), 
            IC_Number INT(12), 
            Password INT(8), 
            Total_fee INT (3)
        ) 
    ''') 
    cursor.close() 
    db_connection.close() 
 
 
# collect data 
def collect_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        name = name_entry.get()
        icnumber = ic_number_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        total_fee = total_fee_entry.get()

        if name and icnumber and email and password:
            age = age_spinbox.get()

            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="student_registration"
            )

            cursor = db_connection.cursor()

            # Check if the selected package is Package C
            if package_var.get() == "Package 3":  # Update based on your actual package names
                # Apply a discount of 10% to the total fee
                total_fee = 60 * 0.9
            else:
                total_fee = 30

            sql = "INSERT INTO student_info (Name, Email, Age, IC_Number, Password, Total_Fee) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (name, email, age, icnumber, password, total_fee)

            try:
                cursor.execute(sql, val)
                db_connection.commit()
                messagebox.showinfo("Success", "Registration successful!")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                cursor.close()
                db_connection.close()

                # Display the total fee with or without the discount 
            total_fee_label.config(text=f"Total Fee: RM {total_fee}") 

        else:
            messagebox.showwarning(title="Error", message="Insert your first and last name, please.")
    else:
            messagebox.showwarning(title="Error", message="You have not accepted the terms")
 
root = tkinter.Tk() 
root.title("Tution Student Registration") 
root.geometry("600x800") 
 
frame = tkinter.Frame(root) 
frame.grid() 
 
# student information 
stud_info_frame = tkinter.LabelFrame(frame, text="Student Information") 
stud_info_frame.grid(row=0, column=0, padx=20, pady=10) 
 
name_label = tkinter.Label(stud_info_frame, text="Name") 
name_label.grid(row=0, column=0) 
name_entry = tkinter.Entry(stud_info_frame) 
name_entry.grid(row=1, column=0) 
 
email_label = tkinter.Label(stud_info_frame, text="Email") 
email_label.grid(row=2, column=1) 
email_entry = tkinter.Entry(stud_info_frame) 
email_entry.grid(row=3, column=1) 
 
age_label = tkinter.Label(stud_info_frame, text="Age") 
age_spinbox = tkinter.Spinbox(stud_info_frame, from_=13, to=17) 
age_label.grid(row=0, column=1) 
age_spinbox.grid(row=1, column=1) 
 
ic_number_label = tkinter.Label(stud_info_frame, text="IC Number") 
ic_number_label.grid(row=2, column=0) 
ic_number_entry = tkinter.Entry(stud_info_frame) 
ic_number_entry.grid(row=3, column=0) 
 
password_label = tkinter.Label(stud_info_frame, text="Password") 
password_label.grid(row=4, column=0) 
password_entry = tkinter.Entry(stud_info_frame) 
password_entry.grid(row=5, column=0) 
 
for widget in stud_info_frame.winfo_children(): 
    widget.grid_configure(padx=10, pady=5) 
 
label = tkinter.Label(root, text='Calculate your Subject Package', font=("Times New Romans",14, "bold")) 
label.grid(ipadx=10, ipady=10) 
 
subject_text = tkinter.Text(root, height=11, width=73) 
subject_text.grid(pady=20) 
 
subject_text.insert(tkinter.END, "Subject Package Prices:\n\n") 
subject_text.insert(tkinter.END, "Package 1: Bahasa Melayu + English \nPrice: RM30\n\n") 
subject_text.insert(tkinter.END, "Package 2: Mathematic + Science \nPrice: RM30\n\n") 
subject_text.insert(tkinter.END, "Package 3: Core Subject (Bahasa Melayu + English + Mathematic + Science) \nPrice: RM60\n\n") 
subject_text.configure(state='disabled') 
subject_text.grid(padx = 30, pady = 30)
 
packs_label = tkinter.Label(root, text="Choose Your Package") 
packs_label.grid() 
 
package_var = tkinter.StringVar(root) 
package_var.set("Select Your Favourite Package")  # Default value before your selection 
trip_dropdown = tkinter.OptionMenu(root, package_var, "Package 1", "Package 2", "Package 3") 
trip_dropdown.grid(pady=20) 
 
#terms & conditions 
terms_frame = tkinter.LabelFrame(root, text="Terms & Conditions") 
terms_frame.grid(sticky="news", padx= 20, pady= 10) 
 
accept_var = tkinter.StringVar(value="Not Accepted") 
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.", 
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted") 
terms_check.grid(sticky="news", padx=20, pady=10) 
 
#button 
button = tkinter.Button(root, text="Register & Calculate Package", command= collect_data) 
button.grid(sticky="news", padx=21, pady=11) 
 
total_fee_label = tkinter.Label(root, text="Total Fee: RM") 
total_fee_label.grid(row=24, column=0, sticky="news") 
total_fee_entry = tkinter.Entry(root)
 
root.mainloop()