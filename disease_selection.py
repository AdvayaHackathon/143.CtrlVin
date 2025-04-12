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
    root.geometry("600x600")
    root.configure(bg="lightgreen")

    selected_language = patient_data["language"]

    tk.Label(root, text="Select Your Disease", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=15)

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
        },
        "Cardiologist (Heart Disease)": {
            "English": {"Doctor": "Dr. Manish Reddy", "Room": "401", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. मनीष रेड्डी", "Room": "४०१", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಮಣಿಷ್ ರೆಡ್ಡಿ", "Room": "೪೦೧", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Neurologist (Brain Disorders)": {
            "English": {"Doctor": "Dr. Preeti Shetty", "Room": "402", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. प्रीति शेट्टी", "Room": "४०२", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಪ್ರೀತೀ ಶೆಟ್ಟಿ", "Room": "೪೦೨", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Pulmonologist (Asthma)": {
            "English": {"Doctor": "Dr. K. Ramesh", "Room": "403", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. के. रमेश", "Room": "४०३", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಕೆ. ರಮೇಶ್", "Room": "೪೦೩", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Hematologist (Blood Cancer)": {
            "English": {"Doctor": "Dr. Neha Gupta", "Room": "404", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. नेहा गुप्ता", "Room": "४०४", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ನೆಹಾ ಗುಪ್ತಾ", "Room": "೪೦೪", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Endocrinologist (Diabetes)": {
            "English": {"Doctor": "Dr. Ajay Joshi", "Room": "405", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. अजय जोशी", "Room": "४०५", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಅಜಯ್ ಜೋಷಿ", "Room": "೪೦೫", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Dermatologist (Skin)": {
            "English": {"Doctor": "Dr. Sheetal Rao", "Room": "406", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. शीतल राव", "Room": "४०६", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಶೀತಲ್ ರಾವ್", "Room": "೪೦೬", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Rheumatologist (Arthritis)": {
            "English": {"Doctor": "Dr. Gopal Menon", "Room": "407", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. गोपाल मेनन", "Room": "४०७", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಗೋಪಾಲ್ ಮೆನನ್", "Room": "೪೦೭", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Ophthalmologist (Eyes)": {
            "English": {"Doctor": "Dr. Kavya Patel", "Room": "408", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. काव्या पटेल", "Room": "४०८", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಕಾವ್ಯಾ ಪಟೇಲ್", "Room": "೪೦೮", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Psychiatrist (Mental Health)": {
            "English": {"Doctor": "Dr. Harshitha Rao", "Room": "409", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. हर्षिता राव", "Room": "४०९", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಹರ್ಷಿತಾ ರಾವ್", "Room": "೪೦೯", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        },
        "Gynecologist (Women’s Health)": {
            "English": {"Doctor": "Dr. Swathi Desai", "Room": "410", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. स्वाति देसाई", "Room": "४१०", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಸ್ವಾತಿ ದೇಸಾಯಿ", "Room": "೪೧೦", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
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
    drop = ttk.Combobox(root, textvariable=selected_disease, values=disease_options, font=("Arial", 12), state="readonly", width=50)
    drop.pack(pady=10)
    drop.bind("<<ComboboxSelected>>", on_disease_selected)

    doctor_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="lightgreen")
    doctor_label.pack(pady=5)

    floor_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    floor_label.pack(pady=5)

    room_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    room_label.pack(pady=5)

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
            "₹300",
            selected_language
        ]
        root.destroy()
        subprocess.Popen(args)

    next_button = tk.Button(root, text="Next", font=("Arial", 12, "bold"), bg="orange", fg="white", command=go_to_payment, state="disabled")
    next_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    disease_selection_screen()
