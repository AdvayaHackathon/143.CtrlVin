import tkinter as tk
from tkinter import ttk
import subprocess

# Simulated patient data from previous screen
patient_data = {
    "name": "Ravi Kumar",
    "phone": "9876543210",
    "location": "Bangalore",
    "age": "30",
    "language": "English"
}

def disease_selection_screen():
    root = tk.Tk()
    root.title("Disease Selection")
    root.geometry("600x400")
    root.configure(bg="lightgreen")

    selected_language = patient_data["language"]

    tk.Label(root, text="Select Your Disease", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=15)

    # Disease data
    disease_data = {
        "Headache": {
            "English": {"Doctor": "Dr. A. Kumar", "Room": "101", "Floor": "1st"},
            "Hindi": {"Doctor": "डॉ. ए. कुमार", "Room": "१०१", "Floor": "पहली मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಎ. ಕುಮಾರ್", "Room": "೧೦೧", "Floor": "ಮೊದಲ ಮಹಡಿ"},
        },
        "Fever": {
            "English": {"Doctor": "Dr. B. Sharma", "Room": "102", "Floor": "1st"},
            "Hindi": {"Doctor": "डॉ. बी. शर्मा", "Room": "१०२", "Floor": "पहली मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಬಿ. ಶರ್ಮಾ", "Room": "೧೦೨", "Floor": "ಮೊದಲ ಮಹಡಿ"},
        },
        "Toothache": {
            "English": {"Doctor": "Dr. D. Mehta", "Room": "202", "Floor": "2nd"},
            "Hindi": {"Doctor": "डॉ. डी. मेहता", "Room": "२०२", "Floor": "दूसरी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಡಿ. ಮೆಹತಾ", "Room": "೨೦೨", "Floor": "ಎರಡನೆ ಮಹಡಿ"},
        },
        "Chest Pain": {
            "English": {"Doctor": "Dr. E. Nair", "Room": "301", "Floor": "3rd"},
            "Hindi": {"Doctor": "डॉ. ई. नायर", "Room": "३०१", "Floor": "तीसरी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಈ. ನಾಯರ್", "Room": "೩೦೧", "Floor": "ಮೂರನೇ ಮಹಡಿ"},
        }
    }

    selected_disease = tk.StringVar()
    selected_disease.set("Select Disease")

    def on_disease_selected(*args):
        disease = selected_disease.get()
        if disease in disease_data:
            info = disease_data[disease][selected_language]
            doctor_label.config(text=f"Doctor: {info['Doctor']}")
            floor_label.config(text=f"Floor: {info['Floor']}")
            room_label.config(text=f"Room No: {info['Room']}")
            next_button.config(state="normal")
        else:
            doctor_label.config(text="")
            floor_label.config(text="")
            room_label.config(text="")
            next_button.config(state="disabled")

    disease_options = list(disease_data.keys())
    drop = ttk.Combobox(root, textvariable=selected_disease, values=disease_options, font=("Arial", 12))
    drop.pack(pady=10)
    drop.bind("<<ComboboxSelected>>", on_disease_selected)

    # Info display
    doctor_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="lightgreen")
    doctor_label.pack(pady=5)

    floor_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    floor_label.pack(pady=5)

    room_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    room_label.pack(pady=5)

    # Proceed to payment
    def go_to_payment():
        disease = selected_disease.get()
        info = disease_data[disease][selected_language]

        args = [
            "python", "payment_screen.py",
            patient_data["name"],
            patient_data["phone"],
            patient_data["location"],
            patient_data["age"],
            disease,
            info["Doctor"],
            info["Room"],
            info["Floor"],
            "₹300",  # Default fee, or make it disease specific if needed
            selected_language
        ]
        root.destroy()
        subprocess.Popen(args)

    next_button = tk.Button(root, text="Next", font=("Arial", 12, "bold"), bg="orange", fg="white", command=go_to_payment, state="disabled")
    next_button.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    disease_selection_screen()
