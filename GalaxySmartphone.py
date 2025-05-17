
class GalaxySmartphone:
    # attributes of GalaxySmartphone
    def __init__(self, model, storage, ram,battery, camera, hard_drive):
        self.model = model
        self.storage = storage
        self.ram = ram
        self.battery = battery
        self.camera = camera
        self.hard_drive = hard_drive
        self.apps = []
        self.locked = True
        self.connected_wifi = None
        
      #Methods of GalaxySmartphone   
         
    def display_specifications(self):
        print(f"Galaxy{self.model} specification:")
        print(f"storage:{self.storage} GB")
        print("ram:{self.ram} GB")
        print("battery:{self.battery} mAh")
        print("camera:{self.camera} MP")
        print("hard_drive:{self.hard_drive} GB")
        
    def make_call(self, number):
        if not self.locked:
           print(f"calling {+2347047504914} from Galaxy {self.model}...")
        else:
            print("unlock your smartphone to phone first.")
            
        if self.call_unreachable:
            
           return f"'{self.model}Call unreachable'."    
    
    def take_photograph(self, camera):
        if not self.locked:
           print(f"photo taken with{self.camera}MP camera on Galaxy {self.model}.")
        else:
            print("Unlock your smartphone to use the camera.")
            
    def get_details(self):
        return f"'{self.ram} MP {self.battery} GB {self.hard_drive} GB on Galaxy{self.model}'."
    
    class GalaxySmartphone:
     def __init__(self, model, storage, ram, battery, camera):
        self.model = model
        self.storage = storage 
        self.ram = ram  
        self.battery = battery 
        self.camera = camera  
        self.apps = []  
        self.locked = True  
        self.connected_wifi = None

    def display_specs(self):
        print(f"\nGalaxy {self.model} Specifications:")
        print(f"Storage: {self.storage}GB")
        print(f"RAM: {self.ram}GB")
        print(f"Battery: {self.battery}mAh")
        print(f"Camera: {self.camera}MP")

    def make_call(self, number):
        if not self.locked:
            print(f"Calling {number} from Galaxy {self.model}...")
        else:
            print("Unlock your phone first.")

    def take_photo(self):
        if not self.locked:
            print(f"Photo taken with {self.camera}MP camera on Galaxy {self.model}.")
        else:
            print("Unlock your phone to use the camera.")

    def install_app(self, Facebook):
        if Facebook not in self.apps:
            self.apps.append(Facebook)
            print(f"{Facebook} installed.")
        else:
            print(f"{Facebook} is already installed.")

    def uninstall_app(self, Zoom):
        if Zoom in self.apps:
            self.apps.remove(Zoom)
            print(f"{Zoom} uninstalled.")
        else:
            print(f"{Zoom} is not installed.")

    def unlock_with_fingerprint(self):
        self.locked = False
        print("Phone unlocked using fingerprint.")

    def lock_phone(self):
        self.locked = True
        print("Phone locked.")

    def connect_wifi(self, MTN_unlimited):
        self.connected_wifi = MTN_unlimited
        print(f"Connected to Wi-Fi network: {MTN_unlimited}")


galaxy = GalaxySmartphone("S25 Ultra", 512, 16, 4000, 200, "1TB")

galaxy.display_specs()
galaxy.unlock_with_fingerprint()
galaxy.install_app("Facebook")
galaxy.install_app("Zoom")
galaxy.make_call("+2347047504914")
galaxy.take_photo()
galaxy.connect_wifi("MTN_unlimited")
galaxy.lock_phone()
galaxy.make_call("07000000000")  
