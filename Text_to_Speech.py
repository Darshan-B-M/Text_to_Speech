import os

print("------------------------------welcome to Darshan's text to speech--------------------------------")
print("---> Enter 'bye' to exit")

while True:
    str=input("Enter the Text to Speech")

    command = (f"  PowerShell -Command \"Add-Type –AssemblyName System.Speech; "
               f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{str}');\"")  # ms speech command line from stack overflow

    os.system(command)

    if str=="bye":
        break
print("Thank You")
