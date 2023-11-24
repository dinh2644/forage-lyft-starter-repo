from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self,wear_sensors):
        self.wear_sensors = wear_sensors
      
    def needs_service(self):
        sum = 0
        for i in range(0,len(self.wear_sensors)):
                sum = sum + self.wear_sensors[i]
            
        if(sum >= 0.9):
            return True
        else:
            return False
    