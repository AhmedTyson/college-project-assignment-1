# B- Car Loan Calculator Application

# This program calculates monthly car loan payments based on:
# - User's job title
# - Car price
# - Down payment amount 
# - Loan term in years
# The calculator helps users understand their potential monthly payments
# before committing to an auto loan.
# Loan Amount = Car Price - Down Payment
# Interest Rate = 5.5% for 1 year, 6.2% for 3 years, 7.0% for 5 years, 7.5% for 7 years
# Total Interest = Interest Rate * Loan Amount * Loan Term
# Total Loan Amount = Loan Amount + Total Interest
# Monthly Payment = Total Loan Amount / (Loan Term * 12)    

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# main window
Car_Loan_App = tk.Tk()
Car_Loan_App.title(string="Car Loan Calculator")
Car_Loan_App.geometry("1080x720")
Car_Loan_App.configure(bg="#f0f0f0")

# main frame
main_frame = Frame(Car_Loan_App, bg="#f0f0f0")
main_frame.pack()

# logo frame
logo_frame = Frame(main_frame, bg="#f0f0f0")
logo_frame.pack()

# display logo
try:
    logo_image = Image.open("Car_logo.png")
    logo_image = logo_image.resize((80, 80))
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(logo_frame, image=logo_photo, bg="white")
    logo_label.image = logo_photo
except Exception:
    logo_label = Label(logo_frame, text="Car Logo", font=("Arial", 16, "bold"), bg="white", fg="gray")
logo_label.pack()

# Add title
title_label = Label(main_frame, text="Car Loan Calculator", font=("Arial", 20, "bold"), fg="blue")
title_label.pack()

# Define user_input function
def user_input():
    jobtitle = str(jobtitle_entry.get())
    car_price = car_price_entry.get()
    down_payment = down_payment_entry.get()
    loan_years = loan_years_entry.get()

    # job title
    if not jobtitle:
        messagebox.showerror("Error", "Please enter a job title!")
        return

    if jobtitle not in ["Doctor", "Engineer", "Teacher", "Student", "Other"]:
        messagebox.showerror("Error", "Invalid job type! Please enter: Doctor, Engineer, Teacher, Student, or Other")
        return

    # car price
    if not car_price:
        messagebox.showerror("Error", "Please enter car price!")
        return

    if not car_price.isdigit():
        messagebox.showerror("Error", "Car price must be a numeric value!")
        return

    # down payment
    if not down_payment:
        messagebox.showerror("Error", "Please enter down payment!")
        return

    if not down_payment.isdigit():
        messagebox.showerror("Error", "Down payment must be a numeric value!")
        return

    # loan years
    if not loan_years:
        messagebox.showerror("Error", "Please enter loan years!")
        return

    if not loan_years.isdigit():
        messagebox.showerror("Error", "Loan years must be a numeric value!")
        return

    loan_years = int(loan_years)
    if loan_years not in [1, 3, 5, 7]:
        messagebox.showerror("Error", "Loan years must be 1, 3, 5, or 7!")
        return

    # Convert inputs to float
    Car_Price = float(car_price)
    Down_Payment = float(down_payment)

    # Calculate loan amount
    Loan_Amount = Car_Price - Down_Payment
    if Loan_Amount <= 0:
        messagebox.showerror("Error", "Down payment cannot be greater than or equal to car price!")
        return

    # Prepare output message with steps
    output = "=== LOAN CALCULATION SUMMARY ===\n\n"
    output += f"Input Values:\n"
    output += f"• Job Title: {jobtitle}\n"
    output += f"• Car Price: ${round(Car_Price)}\n"
    output += f"• Down Payment: ${round(Down_Payment)}\n"
    output += f"• Loan Years: {loan_years}\n\n"

    # Calculate loan amount
    output += f"1. Loan Amount:\n"
    output += f"   ${round(Car_Price)} - ${round(Down_Payment)} = ${round(Loan_Amount)}\n\n"

    # Calculate yearly interest rate
    if loan_years == 1:
        yearly_interest_rate = 5.5
    elif loan_years == 3:
        yearly_interest_rate = 6.2
    elif loan_years == 5:
        yearly_interest_rate = 7.0
    else:  # 7 years
        yearly_interest_rate = 7.5

    output += f"2. Interest Rate: {yearly_interest_rate}% (for {loan_years} years)\n\n"

    # Calculate interest per year
    Interest_Per_Year = (yearly_interest_rate / 100) * Loan_Amount
    output += f"3. Interest Per Year:\n"
    output += f"   {yearly_interest_rate}% × ${round(Loan_Amount)} = ${round(Interest_Per_Year)}\n\n"

    # Calculate total interest
    Total_Interest = Interest_Per_Year * loan_years
    output += f"4. Total Interest:\n"
    output += f"   ${round(Interest_Per_Year)} × {loan_years} = ${round(Total_Interest)}\n\n"

    # Calculate total loan amount
    Total_Loan_Amount = Loan_Amount + Total_Interest
    output += f"5. Total Loan:\n"
    output += f"   ${round(Loan_Amount)} + ${round(Total_Interest)} = ${round(Total_Loan_Amount)}\n\n"

    # Calculate monthly payment
    Monthly_Payment = Total_Loan_Amount / (loan_years * 12)
    Monthly_Payment = round(Monthly_Payment)
    output += f"6. Pay/Month:\n"
    output += f"   ${round(Total_Loan_Amount)} ÷ ({loan_years} × 12) = ${Monthly_Payment}\n\n"

    # Display a congratulatory message if the monthly payment is affordable
    if Monthly_Payment < 15000:
        messagebox.showinfo("Congratulations", "Your monthly payment is affordable!")
    # Display a warning message if the monthly payment is high
    elif Monthly_Payment > 30000:
        messagebox.showwarning("Warning", "Your monthly payment is quite high!")
    # Display a congratulatory message for payments between 15000 and 30000
    else:
        messagebox.showinfo("Congratulations", "Your monthly payment is within a good range!")

    output_label.config(text=output)

# Function to clear all entries
def clear_entries():
    jobtitle_entry.delete(0, END)
    car_price_entry.delete(0, END)
    down_payment_entry.delete(0, END)
    loan_years_entry.delete(0, END)
    output_label.config(text="")

# Function to exit the application
def exit_app():
    Car_Loan_App.destroy()

# Create frames for different sections
input_frame = Frame(main_frame, bg="#f0f0f0")
input_frame.pack(side=LEFT, padx=10)

button_frame = Frame(main_frame, bg="#f0f0f0")
button_frame.pack(side=RIGHT, padx=10)

output_frame = Frame(main_frame, bg="#f0f0f0")
output_frame.pack(side=BOTTOM, pady=10)

# Job Title
job_frame = Frame(input_frame, bg="#f0f0f0")
job_frame.pack(pady=5)
Label(job_frame, text="Job Title (Doctor/Engineer/Teacher/Student/Other):", bg="#f0f0f0").pack()
jobtitle_entry = Entry(job_frame, width=40)
jobtitle_entry.pack()

# Car Price
price_frame = Frame(input_frame, bg="#f0f0f0")
price_frame.pack(pady=5)
Label(price_frame, text="Car Price ($):", bg="#f0f0f0").pack()
car_price_entry = Entry(price_frame, width=40)
car_price_entry.pack()

# Down Payment
down_frame = Frame(input_frame, bg="#f0f0f0")
down_frame.pack(pady=5)
Label(down_frame, text="Down Payment ($):", bg="#f0f0f0").pack()
down_payment_entry = Entry(down_frame, width=40)
down_payment_entry.pack()

# Loan Years
years_frame = Frame(input_frame, bg="#f0f0f0")
years_frame.pack()
Label(years_frame, text="Loan Years (1/3/5/7):", bg="#f0f0f0").pack()
loan_years_entry = Entry(years_frame, width=40)
loan_years_entry.pack()

# Buttons
calculate_button = Button(button_frame, text="Calculate", command=lambda: user_input(), bg="#4CAF50", fg="white", width=15, underline=0)
calculate_button.pack(side=LEFT, padx=5)

clear_button = Button(button_frame, text="Clear", command=lambda: clear_entries(), bg="#f44336", fg="white", width=15, underline=0)
clear_button.pack(side=LEFT, padx=5)

exit_button = Button(button_frame, text="Exit", command=lambda: exit_app(), bg="#2196F3", fg="white", width=15, underline=1)
exit_button.pack(side=LEFT, padx=5)

# Output Label
output_label = Label(output_frame, text="", bg="white", fg="black", width=70, height=30)
output_label.pack()

Car_Loan_App.mainloop()
