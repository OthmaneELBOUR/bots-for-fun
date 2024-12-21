import smtplib
from email.message import EmailMessage
import time
import csv

#Generate mail with a specific paragraphe for each receiver and send it using smtp protocol
def generate_mail(entreprise):
    email_body = f"""Madame, monsieur,
Bonjour,
Paragrpahe 1

{paragraphes[entreprise]}

Paragraphe 2

Paragraphe 3
"""
    return email_body


def send_emails(sender, password, recipient, attach, body, smtp_server, smtp_port):
    
    msg = EmailMessage()
    msg["Subject"] = "Demande de stage PFA en hydrogéologie"
    msg["From"] = sender
    msg.set_content(body)

    try:
        with open(attach, "rb") as file:
            file_data = file.read()
            file_name = attach.split("/")[-1] 
            msg.add_attachment(
                file_data, maintype="application", subtype="pdf", filename=file_name
            )
    except FileNotFoundError:
        print(f"File {attach} not found!")
        return

    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, password)

            
            msg["To"] = recipient
            server.send_message(msg)
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

    
    time.sleep(1)

def readCSV(file_path1, file_path2):
    expected_fields1 = ["Email", "Entreprise"]
    expected_fields2 = ["Entreprise", "Paragraphe"]
    
    
    with open(file_path1, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        
        if set(expected_fields1).issubset(reader.fieldnames):
            print("The file contains all expected fields.")
        else:
            missing_fields = set(expected_fields1) - set(reader.fieldnames)
            print(f"Missing fields: {missing_fields}")

        
        for row in reader:
            data.append(row)
    
    with open(file_path2, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        if set(expected_fields2).issubset(reader.fieldnames):
            print("The file contains all expected fields.")
        else:
            missing_fields = set(expected_fields1) - set(reader.fieldnames)
            print(f"Missing fields: {missing_fields}")

        for row in reader:
            paragraphes[row["Entreprise"]] = row["Paragraphe"]   
        
#Needs you mail, the app password, the files to attach, the database to get the data from
sender_email = input("Entrez votre email : ")    
sender_password = input("Entrez votre mot de passe : ")
sender_cv = input("Le nom de votre CV (sans le .pdf) : ")
sender_cv += ".pdf"
csv_file_name = input("Le nom de votre base de donnees (sans le .csv) : ")
csv_file_name += ".csv"
csv_file_paragraphes = input("Le nom de la bases de données avec les paragraphes (sans le .csv): ")
csv_file_paragraphes += ".csv"

smtp_server = "smtp.gmail.com"
smtp_port = 587

data =[]
paragraphes = {}

readCSV(csv_file_name, csv_file_paragraphes)


#main ----------------------------------------------------------------------------------------
for p in data:
    email = generate_mail(p["Entreprise"])
    print(email)
    print("\n--------------------------------------------------------------------------------------\n")
    send_emails(sender_email, sender_password,p["Email"], sender_cv,email, smtp_server, smtp_port)


