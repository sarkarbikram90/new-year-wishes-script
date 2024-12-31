import pywhatkit as kit
import time

# List of phone numbers
contacts = [
    
    
    # type contact numbers followed by comma (,)
    
]

# Message to send
message = "🎉 Happy New Year! 🎊 May this year bring you happiness, success, and good health. 🥳"

# Schedule and send messages
for number in contacts:
    try:
        # Schedule the message for 1 minute from now
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min + 1
        
        # Send message using pywhatkit
        kit.sendwhatmsg(number, message, hour, minute)
        
        print(f"Message sent to {number}")
        time.sleep(60)  # Wait to ensure the message is sent before sending the next one
    except Exception as e:
        print(f"Failed to send message to {number}. Error: {e}")
