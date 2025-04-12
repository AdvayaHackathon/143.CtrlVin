import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import time
import sys

def send_sms(name, phone, disease, doctor, room, floor, fee, language):
    message = {
        "English": f"Dear {name}, your appointment for {disease} with {doctor} is confirmed. Room: {room}, Floor: {floor}. Fee: {fee}.",
        "Hindi": f"प्रिय {name}, आपकी {disease} के लिए {doctor} से अपॉइंटमेंट तय हो गई है। कक्ष: {room}, मंज़िल: {floor}, शुल्क: {fee}।",
        "Kannada": f"ಪ್ರಿಯ {name}, ನಿಮ್ಮ {disease}ಗಾಗಿ {doctor}ರೊಂದಿಗೆ ನೇಮಕಾತಿ ದೃಢವಾಗಿದೆ. ಕೋಣೆ: {room}, ಮಹಡಿ: {floor}, ಫೀಸ್: {fee}."
    }

    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = {
        "authorization": "YOUR_FAST2SMS_API_KEY",  # Replace with your API key
        "sender_id": "FSTSMS",
        "message": message[language],
        "language": "english",
        "route": "v3",
        "numbers": phone,
    }
    headers = {'cache-control': "no-cache"}
    response = requests.post(url, data=payload, headers=headers)
    print("SMS sent:", response.text)

def payment_screen():
    # For testing without command-line arguments
    if len(sys.argv) < 11:
        name = "Test Patient"
        phone = "9999999999"
        location = "Bangalore"
        age = "25"
        disease = "Fever"
        doctor = "Dr. Sharma"
        room = "101"
        floor = "1"
        fee = "₹300"
        language = "English"
    else:
        name = sys.argv[1]
        phone = sys.argv[2]
        location = sys.argv[3]
        age = sys.argv[4]
        disease = sys.argv[5]
        doctor = sys.argv[6]
        room = sys.argv[7]
        floor = sys.argv[8]
        fee = sys.argv[9]
        language = sys.argv[10]

    labels = {
        "English": {
            "title": "Payment Screen",
            "scan": "Scan QR to Pay",
            "upi": "Hospital UPI ID: adichunchanagiri@upi",
            "confirm": "Payment Done",
            "analyzing": "Analyzing Payment...",
            "done": "Payment Confirmed & SMS Sent!"
        },
        "Hindi": {
            "title": "भुगतान स्क्रीन",
            "scan": "QR को स्कैन करें",
            "upi": "अस्पताल UPI ID: adichunchanagiri@upi",
            "confirm": "भुगतान किया गया",
            "analyzing": "भुगतान का विश्लेषण हो रहा है...",
            "done": "भुगतान की पुष्टि और SMS भेजा गया!"
        },
        "Kannada": {
            "title": "ಪಾವತಿ ಪರದೆ",
            "scan": "QR ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ",
            "upi": "ಆಸ್ಪತ್ರೆಯ UPI ID: adichunchanagiri@upi",
            "confirm": "ಪಾವತಿ ಮಾಡಿಕೊಂಡೆ",
            "analyzing": "ಪಾವತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...",
            "done": "ಪಾವತಿ ದೃಢಪಡಿಸಲಾಗಿದೆ ಮತ್ತು SMS ಕಳುಹಿಸಲಾಗಿದೆ!"
        }
    }

    lang = labels[language]

    root = tk.Tk()
    root.title(lang["title"])
    root.geometry("500x600")
    root.configure(bg="white")

    tk.Label(root, text=lang["scan"], font=("Arial", 16, "bold"), bg="white").pack(pady=15)

    # Show QR Code
    try:
        img = Image.open("upi_qr.png")
        img = img.resize((250, 250))
        qr_img = ImageTk.PhotoImage(img)
        tk.Label(root, image=qr_img, bg="white").pack()
    except:
        tk.Label(root, text="(QR image not found)", font=("Arial", 12), bg="white", fg="red").pack()

    tk.Label(root, text=lang["upi"], font=("Arial", 14), bg="white", fg="green").pack(pady=15)

    def confirm_payment():
        # Simulate payment analysis
        processing = tk.Label(root, text=lang["analyzing"], font=("Arial", 12, "italic"), bg="white")
        processing.pack()
        root.update()
        time.sleep(2)  # simulate delay
        processing.destroy()

        send_sms(name, phone, disease, doctor, room, floor, fee, language)
        messagebox.showinfo("Success", lang["done"])
        root.destroy()

    tk.Button(root, text=lang["confirm"], font=("Arial", 14), bg="green", fg="white",
              command=confirm_payment).pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    payment_screen()
