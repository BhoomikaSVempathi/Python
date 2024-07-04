from tkinter import *

# Create the main window
window = Tk()

# Set the geometry of the window
window.geometry("800x500")
window.configure(background='light blue')

# Set the title of the window
window.title("Besant Technology")

# Function to handle the submission and print details
def getDetails():
    first_name = fName.get()
    last_name = lName.get()
    date = date_entry.get()
    mobile_number = mobile_no.get()
    alternative_number = alt_no.get()
    email_text = email.get()
    address_text = address.get()
    course_text = course.get()
    batch_text = batch.get()
    about_text = about.get()
    exp_text = exp.get()
    contact_text = contact.get()
    counselor_text = counselor.get()
    fee_text = fee.get()
    comment_text = comment.get()
    register = varR.get()
    enquire = varE.get()
    
    # Print the values to the console (or perform any action you need)
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Date: {date}")
    print(f"Mobile No: {mobile_number}")
    print(f"Alternative No: {alternative_number}")
    print(f"Email_ID: {email_text}")
    print(f"Address: {address_text}")
    print(f"Course Interested: {course_text}")
    print(f"Batch Preferred: {batch_text}")
    print(f"How You came To Know Us: {about_text}")
    print(f"Are you Experience Or Fresher: {exp_text}")
    print(f"Contact Person From Besant Technology: {contact_text}")
    print(f"Counselor: {counselor_text}")
    print(f"Fees: {fee_text}")
    print(f"Comment: {comment_text}")
    print(f"Register: {register}")
    print(f"Enquire: {enquire}")

# Create and place the labels and entry widgets
Label(window, text="Besant Technology Enquiry Form", font='arial 15 bold', background='light blue').grid(row=0, column=1, pady=10)
Label(window, text="First Name", font='arial 10', background='light blue').grid(row=1, column=0, sticky=W)
Label(window, text="Last Name", font='arial 10', background='light blue').grid(row=2, column=0, sticky=W)
Label(window, text="Date", font='arial 10', background='light blue').grid(row=3, column=0, sticky=W)
Label(window, text="Mobile No", font='arial 10', background='light blue').grid(row=4, column=0, sticky=W)
Label(window, text="Alternative No", font='arial 10', background='light blue').grid(row=5, column=0, sticky=W)
Label(window, text="Email_ID", font='arial 10', background='light blue').grid(row=6, column=0, sticky=W)
Label(window, text="Address", font='arial 10', background='light blue').grid(row=7, column=0, sticky=W)
Label(window, text="Course Interested", font='arial 10', background='light blue').grid(row=8, column=0, sticky=W)
Label(window, text="Batch Preferred", font='arial 10', background='light blue').grid(row=9, column=0, sticky=W)
Label(window, text="How You came To Know Us", font='arial 10', background='light blue').grid(row=10, column=0, sticky=W)
Label(window, text="Are you Experience Or Fresher", font='arial 10', background='light blue').grid(row=11, column=0, sticky=W)
Label(window, text="Contact Person From Besant Technology", font='arial 10', background='light blue').grid(row=12, column=0, sticky=W)
Label(window, text="Counselor", font='arial 10', background='light blue').grid(row=13, column=0, sticky=W)
Label(window, text="Fees", font='arial 10', background='light blue').grid(row=14, column=0, sticky=W)
Label(window, text="Comment", font='arial 10', background='light blue').grid(row=15, column=0, sticky=W)

fName = Entry(window)
fName.grid(row=1, column=1, padx=10, pady=2)

lName = Entry(window)
lName.grid(row=2, column=1, padx=10, pady=2)

date_entry = Entry(window)
date_entry.grid(row=3, column=1, padx=10, pady=2)

mobile_no = Entry(window)
mobile_no.grid(row=4, column=1, padx=10, pady=2)

alt_no = Entry(window)
alt_no.grid(row=5, column=1, padx=10, pady=2)

email = Entry(window)
email.grid(row=6, column=1, padx=10, pady=2)

address = Entry(window)
address.grid(row=7, column=1, padx=10, pady=2)

course = Entry(window)
course.grid(row=8, column=1, padx=10, pady=2)

batch = Entry(window)
batch.grid(row=9, column=1, padx=10, pady=2)

about = Entry(window)
about.grid(row=10, column=1, padx=10, pady=2)

exp = Entry(window)
exp.grid(row=11, column=1, padx=10, pady=2)

contact = Entry(window)
contact.grid(row=12, column=1, padx=10, pady=2)

counselor = Entry(window)
counselor.grid(row=13, column=1, padx=10, pady=2)

fee = Entry(window)
fee.grid(row=14, column=1, padx=10, pady=2)

comment = Entry(window)
comment.grid(row=15, column=1, padx=10, pady=2)

# Initialize IntVar variables for checkbuttons
varR = IntVar()
varE = IntVar()

# Create and place the checkbuttons
checkM = Checkbutton(window, text="Register", variable=varR, background='light blue')
checkM.grid(row=16, column=1)

checkF = Checkbutton(window, text="Enquiry", variable=varE, background='light blue')
checkF.grid(row=17, column=1)

# Create and place the submit button
Button(window, text="Submit", bg="Green", command=getDetails).grid(row=20, column=1, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
