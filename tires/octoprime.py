from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self,wear_sensors):
        self.wear_sensors = wear_sensors
      
    def needs_service(self):
        sum = 0
        for i in range(0,len(self.wear_sensors)):
            sum = sum + self.wear_sensors[i]
        
        if(sum >= 3):
            return True
        else:
            return False
    