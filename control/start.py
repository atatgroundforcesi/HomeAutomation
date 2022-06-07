from asyncio.windows_events import NULL
from platform import system
from re import search, match
from random import choice

class Setup:

        def menue():
            #Statements
            statements_enter = ["Enter Input: ", "Howdy, please instruct me what i should do: "]
            statements_exit = ["exit"]

            men_input = input(str(f"***Home Automation***\n{statements_enter[0]} "))

            while len(men_input) > 0:

                #Help
                if search(men_input,"help"):
                    print("\nOptions\n +start: Start Building Image or VM\n +exit: exit HomeAutomation\n +reload: Go Back to main Menue to start again :")
                    men_input = input(choice(statements_enter))
            
                #Start
                if search(men_input,"-s|start"):

                    if search(men_input, "-s vm| or start vm"):
                        Setup.create_vm()
                        break

                    if match(men_input, "start -vm"):
                        #TODO Menue for Start Building VM
                        print("Menue Building VM")
                        break

                if match(men_input, "start image"):
                    #TODO Menue for Building Image
                    print("Menue Building Image")
                    break

                else:
                    men_input = input(str("Please Enter valid Option or type quit: "))

                    if match(men_input, "quit"):
                        print("abort Homeautomation\n Bye!")
                        exit(0)


        def create_vm():
            supported_os = ["Windows"]
            supported_hypervisor = ["Hypver-V"]

            if system() != supported_os[0]:
                print("Only Windows Supported")
                print(f"Following Hypervisor are Supported: {supported_hypervisor} ")
                exit(1)

            else:
                os = system()
                print(f"Supported os {os} found")

Setup.menue()