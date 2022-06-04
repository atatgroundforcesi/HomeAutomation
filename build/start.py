from platform import system

class Setup:
        def create_vm():
            supported_os = ["Windows"]
            supported_hypervisor = ["Hypver-V"]

            if system() != supported_os[0]:
                print(system())
                print("Only Windows Supported")
                print(f"Following Hypervisor are Supported: {supported_hypervisor} ")

            else:
                print("Supported os found")

        def create_boot_media():
            supported_iso = ["Ubuntu Server", "Windows Server"]

Setup.create_vm()