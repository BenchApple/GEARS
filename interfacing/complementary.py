# Ben Chappell

import sys
import time
from MPU9250 import MPU9250
import imu_interface as imu
from math import atan2
from math import pi

# implements the complementary filter to calculate the yaw of our robot

# Accel data takes the most recent reading from the gyroscope
# gyro data takes the most recent reading from the gyro
# prev_yaw takes the previous positioning in degrees around the z axis (yaw)
# dt takes the time step between the previs reading and this reading.
def complementary_filter(accel_data, gyro_data, prev_yaw, dt):
    new_yaw = prev_yaw + (gyro_data * dt)

    force_magn_approx = abs(accel_data['x']) + abs(accel_data['y']) + abs(accel_data['z'])
    print(force_magn_approx)
    '''
    if force_magn_approx > 0.5 and force_magn_approx < 2:
        yaw_accel = atan2(accel_data['x'], accel_data['y']) * 180 / pi
        new_yaw = new_yaw * 0.98 + yaw_accel * 0.02
    '''

    return new_yaw

def use_kalman(state, filter, d1y):
    pass

def main():
    try: 
        cur_yaw = 0
        while True:
            dt = 0.01
            imu_obj = imu.init()
            accel_data = imu.getAccel(imu_obj) # This is a dictionary 
            gyro_z = imu.getZAngular(imu_obj) 
            cur_yaw = complementary_filter(accel_data, gyro_z, cur_yaw, dt);
            print(cur_yaw)
            time.sleep(dt)

    except KeyboardInterrupt:
        sys.exit()
    
if __name__ == "__main__":
    main()
    
