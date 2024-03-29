from adafruit_servokit import ServoKit
from time import sleep
import threading

class Legs():
    coxa_pin = 0
    femur_pin = 0
    tibia_pin = 0

    coxa_init_angle = 90.0
    femur_init_angle = 90.0
    tibia_init_angle = 90.0

    coxa_offset_angle = 0.0
    femur_offset_angle = 0.0
    tibia_offset_angle = 0.0

Leg = []
for x in range(6):
    Leg.append(Legs())

leftlegs = ServoKit(channels=16, address=0x40, frequency=120)
rightlegs = ServoKit(channels=16, address=0x41, frequency=120)
movement_delay = 0.010 #100ms
movement_offset = 15 #10 degrees

class Commands():

  
    def hello(self):
        print("hello")

    def waiting():
        print("waiting")

    M_thread = threading.Thread(target=waiting)
    M_thread.start()
    total_moved = 0

    run = 0

    
    def idle(self):
        if(self.run ==1):
            rightlegs.servo[Leg[0].coxa_pin].angle = Leg[0].coxa_init_angle
            rightlegs.servo[Leg[0].femur_pin].angle = Leg[0].femur_init_angle
            rightlegs.servo[Leg[0].tibia_pin].angle = Leg[0].tibia_init_angle

            rightlegs.servo[Leg[1].coxa_pin].angle = Leg[1].coxa_init_angle
            rightlegs.servo[Leg[1].femur_pin].angle = Leg[1].femur_init_angle
            rightlegs.servo[Leg[1].tibia_pin].angle = Leg[1].tibia_init_angle

            rightlegs.servo[Leg[2].coxa_pin].angle = Leg[2].coxa_init_angle
            rightlegs.servo[Leg[2].femur_pin].angle = Leg[2].femur_init_angle
            rightlegs.servo[Leg[2].tibia_pin].angle = Leg[2].tibia_init_angle

            leftlegs.servo[Leg[3].coxa_pin].angle = Leg[3].coxa_init_angle
            leftlegs.servo[Leg[3].femur_pin].angle = Leg[3].femur_init_angle
            leftlegs.servo[Leg[3].tibia_pin].angle = Leg[3].tibia_init_angle

            leftlegs.servo[Leg[4].coxa_pin].angle = Leg[4].coxa_init_angle
            leftlegs.servo[Leg[4].femur_pin].angle = Leg[4].femur_init_angle
            leftlegs.servo[Leg[4].tibia_pin].angle = Leg[4].tibia_init_angle

            leftlegs.servo[Leg[5].coxa_pin].angle = Leg[5].coxa_init_angle
            leftlegs.servo[Leg[5].femur_pin].angle = Leg[5].femur_init_angle
            leftlegs.servo[Leg[5].tibia_pin].angle = Leg[5].tibia_init_angle

    def leg_movement(self,number):

        if number == 0:
            moved_1 = True
            #up and then forward
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].femur_pin].angle = Leg[0].femur_init_angle - i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].tibia_pin].angle = Leg[0].tibia_init_angle - i
                sleep(movement_delay)
                
            for i in range(movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].coxa_pin].angle = Leg[0].coxa_init_angle - i
                sleep(movement_delay)

            #down and then backward
            for i in range(movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].tibia_pin].angle = Leg[0].tibia_init_angle - movement_offset + i
                sleep(movement_delay)
                
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].femur_pin].angle = Leg[0].femur_init_angle - (movement_offset + movement_offset) + i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_1 = False
                    break
                rightlegs.servo[Leg[0].coxa_pin].angle = Leg[0].coxa_init_angle - movement_offset + i
                sleep(movement_delay)

            if moved_1:
                self.total_moved+=1

        elif number == 1:
            moved_2 = True
            #up and then forward
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].femur_pin].angle = Leg[1].femur_init_angle - i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].tibia_pin].angle = Leg[1].tibia_init_angle - i
                sleep(movement_delay)
                
            for i in range(movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].coxa_pin].angle = Leg[1].coxa_init_angle - i
                sleep(movement_delay)

            #down and then backward
            for i in range(movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].tibia_pin].angle = Leg[1].tibia_init_angle - movement_offset + i
                sleep(movement_delay)
                
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].femur_pin].angle = Leg[1].femur_init_angle - (movement_offset + movement_offset) + i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_2 = False
                    break
                rightlegs.servo[Leg[1].coxa_pin].angle = Leg[1].coxa_init_angle - movement_offset + i
                sleep(movement_delay)
                
            if moved_2:
                self.total_moved+=1

        elif number == 2:
            moved_3 = True
            #up and then forward
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].femur_pin].angle = Leg[2].femur_init_angle - i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].tibia_pin].angle = Leg[2].tibia_init_angle - i
                sleep(movement_delay)
                
            for i in range(movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].coxa_pin].angle = Leg[2].coxa_init_angle - i
                sleep(movement_delay)

            #down and then backward
            for i in range(movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].tibia_pin].angle = Leg[2].tibia_init_angle - movement_offset + i
                sleep(movement_delay)
                
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].femur_pin].angle = Leg[2].femur_init_angle - (movement_offset + movement_offset) + i
                sleep(movement_delay)

            for i in range(movement_offset):
                if self.run == 0:
                    moved_3 = False
                    break
                rightlegs.servo[Leg[2].coxa_pin].angle = Leg[2].coxa_init_angle - movement_offset + i
                sleep(movement_delay)
                
            if moved_3:
                self.total_moved+=1

        elif number == 3:
            moved_4 = True
            #up and then forward
            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_4 = False
                    break
                leftlegs.servo[Leg[3].femur_pin].angle = Leg[3].femur_init_angle - i
                sleep(movement_delay)

            for i in range(movement_offset + movement_offset):
                if self.run == 0:
                    moved_4 = False
                    break
                leftlegs.servo[Leg[3].femur_pin].angle = Leg[3].femur_init_angle - i
                sleep(movement_delay)

            
        

    def frwrd(self):
        if self.run == 1:

            self.leg_movement(3)
            # self.leg_movement(1)
            # self.leg_movement(2)
            print("total moved: ",self.total_moved)
        
    def backwrd(self):
        while(self.run == 1):
            pass

    def start_commands(self):

        command = input("enter command: ")
        while(command != "exit"):
            if command == "idle":

                self.run = 0
                self.M_thread.join()
                print(self.M_thread.is_alive())
                self.run = 1
                self.M_thread = threading.Thread(target = self.idle)
                self.M_thread.start()

                
            elif command == "frwrd":
                
                self.run = 0
                self.M_thread.join()
                print(self.M_thread.is_alive())
                self.run = 1
                self.M_thread = threading.Thread(target = self.frwrd)
                self.M_thread.start()
                
            elif command == "backward":
                self.run = 0
                self.M_thread.join()
                print(self.M_thread.is_alive())
                self.run = 1
                self.M_thread = threading.Thread(target = self.backwrd)
                self.M_thread.start()
            

            print(command)
            print("Thread's count: ", threading.active_count())
            command = input("enter command: ")



def init():
    
    #leg 0 configurations
    Leg[0].coxa_pin = 13
    Leg[0].femur_pin = 14
    Leg[0].tibia_pin = 15

    Leg[0].coxa_offset_angle = 10 #0.0
    Leg[0].femur_offset_angle = -45 #-22.0
    Leg[0].tibia_offset_angle = 10 #40.0
    
    Leg[0].coxa_init_angle = 90 + Leg[0].coxa_offset_angle
    Leg[0].femur_init_angle = 90 + Leg[0].femur_offset_angle
    Leg[0].tibia_init_angle = 90 + Leg[0].tibia_offset_angle

    rightlegs.servo[Leg[0].coxa_pin].angle = Leg[0].coxa_init_angle
    rightlegs.servo[Leg[0].femur_pin].angle = Leg[0].femur_init_angle
    rightlegs.servo[Leg[0].tibia_pin].angle = Leg[0].tibia_init_angle


    #leg 1 configurations
    Leg[1].coxa_pin = 9
    Leg[1].femur_pin = 5
    Leg[1].tibia_pin = 6

    Leg[1].coxa_offset_angle = 0 #0.0
    Leg[1].femur_offset_angle = 0 #25.0
    Leg[1].tibia_offset_angle = 20 #40.0
    
    Leg[1].coxa_init_angle = 90 + Leg[1].coxa_offset_angle
    Leg[1].femur_init_angle = 90 + Leg[1].femur_offset_angle
    Leg[1].tibia_init_angle = 90 + Leg[1].tibia_offset_angle

    rightlegs.servo[Leg[1].coxa_pin].angle = Leg[1].coxa_init_angle
    rightlegs.servo[Leg[1].femur_pin].angle = Leg[1].femur_init_angle
    rightlegs.servo[Leg[1].tibia_pin].angle = Leg[1].tibia_init_angle


    #leg 2 configurations
    Leg[2].coxa_pin = 3
    Leg[2].femur_pin = 0
    Leg[2].tibia_pin = 1

    Leg[2].coxa_offset_angle = 0 #0.0
    Leg[2].femur_offset_angle = 15 #35.0
    Leg[2].tibia_offset_angle = 20 #50.0
    
    Leg[2].coxa_init_angle = 90 + Leg[2].coxa_offset_angle
    Leg[2].femur_init_angle = 90 + Leg[2].femur_offset_angle
    Leg[2].tibia_init_angle = 90 + Leg[2].tibia_offset_angle

    rightlegs.servo[Leg[2].coxa_pin].angle = Leg[2].coxa_init_angle
    rightlegs.servo[Leg[2].femur_pin].angle = Leg[2].femur_init_angle
    rightlegs.servo[Leg[2].tibia_pin].angle = Leg[2].tibia_init_angle

    #leg 3 configurations
    Leg[3].coxa_pin = 13
    Leg[3].femur_pin = 15
    Leg[3].tibia_pin = 14

    Leg[3].coxa_offset_angle = 0 #0.0
    Leg[3].femur_offset_angle = -38 #-34.0
    Leg[3].tibia_offset_angle = 20 #65.0
    
    Leg[3].coxa_init_angle = 90 + Leg[3].coxa_offset_angle
    Leg[3].femur_init_angle = 90 + Leg[3].femur_offset_angle
    Leg[3].tibia_init_angle = 90 + Leg[3].tibia_offset_angle

    leftlegs.servo[Leg[3].coxa_pin].angle = Leg[3].coxa_init_angle
    leftlegs.servo[Leg[3].femur_pin].angle = Leg[3].femur_init_angle
    leftlegs.servo[Leg[3].tibia_pin].angle = Leg[3].tibia_init_angle


    #leg 4 configurations
    Leg[4].coxa_pin = 9
    Leg[4].femur_pin = 6
    Leg[4].tibia_pin = 5

    Leg[4].coxa_offset_angle = -10 #-10.0
    Leg[4].femur_offset_angle = -35 #-28.0
    Leg[4].tibia_offset_angle = 10 #50.0
    
    Leg[4].coxa_init_angle = 90 + Leg[4].coxa_offset_angle
    Leg[4].femur_init_angle = 90 + Leg[4].femur_offset_angle
    Leg[4].tibia_init_angle = 90 + Leg[4].tibia_offset_angle

    leftlegs.servo[Leg[4].coxa_pin].angle = Leg[4].coxa_init_angle
    leftlegs.servo[Leg[4].femur_pin].angle = Leg[4].femur_init_angle
    leftlegs.servo[Leg[4].tibia_pin].angle = Leg[4].tibia_init_angle

    #leg 5 configurations
    Leg[5].coxa_pin = 3
    Leg[5].femur_pin = 1
    Leg[5].tibia_pin = 0

    Leg[5].coxa_offset_angle = 0 #0.0
    Leg[5].femur_offset_angle = -30 #-25.0
    Leg[5].tibia_offset_angle = 10 #55.0
    
    Leg[5].coxa_init_angle = 90 + Leg[5].coxa_offset_angle
    Leg[5].femur_init_angle = 90 + Leg[5].femur_offset_angle
    Leg[5].tibia_init_angle = 90 + Leg[5].tibia_offset_angle

    leftlegs.servo[Leg[5].coxa_pin].angle = Leg[5].coxa_init_angle
    leftlegs.servo[Leg[5].femur_pin].angle = Leg[5].femur_init_angle
    leftlegs.servo[Leg[5].tibia_pin].angle = Leg[5].tibia_init_angle

    print("initialized")

command = Commands()



def main():
    init()
    command.start_commands()

if __name__ == '__main__':
    
    main()