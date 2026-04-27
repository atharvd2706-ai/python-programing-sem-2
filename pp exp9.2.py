from datetime import datetime

today = datetime.today()
formatted_date = today.strftime("%d %B %Y")  

print("Appointment Date:", formatted_date)