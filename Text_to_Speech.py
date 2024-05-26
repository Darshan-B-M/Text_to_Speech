import os

print("-------Welcome to Darshan's text to speech Bot--------")
print("--->To Exit enter 'bye'")

while True:
        str=input("Enter the text")
        command =f"  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{str}');\""
        os.system(command)

        if str=="bye":
            break
print("Thank you")