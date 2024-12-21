import pywhatkit
import time
dico = {
    "+212612345678" : "Random Name" ,
    }

# Was used to send whatsapp messages to a large number of people to let them know they got accepted
for key in dico:
    pywhatkit.sendwhatmsg_instantly(key, "Hello {}, sending you a message using a bot".format(dico[key].title()))
    time.sleep(25)


