import serial

class DataRx:
    def __init__(self):
        # open the serial port at the appropriate baud rate and settings
        self.ser = serial.Serial('COM7', baudrate = 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0.001)

    def PutData(self, DataList):
        prev_value_first_3bits = None
        prev_value = None
        circuit_data = ''
        while True:
            # Read 10 bytes from serial port
            data = self.ser.read(10) 
            if data:
                # Convert data to binary string
                binary_data = ' '.join(format(x, '08b') for x in data)

                # First 8 bits of the binary_data
                binary_data = binary_data[:8]

                # First 3 bits of the binary_data
                first_3bits = binary_data[:3]

                # Last 5 bits of the binary_data
                last_5bits = binary_data[3:]

                # If first_3bits is not equal to prev_value_first_3bits, do the following
                if first_3bits != prev_value_first_3bits:
                    # Circuit data is the last 5 bits of the binary_data concatanate for 4 steps starting from first_3bits = 000 to first_3bits = 011
                    if first_3bits == '000':
                        circuit_data = last_5bits
                    elif first_3bits == '001':
                        circuit_data = last_5bits + circuit_data
                    elif first_3bits == '010':
                        circuit_data = last_5bits + circuit_data
                    elif first_3bits == '011':
                        circuit_data = last_5bits + circuit_data
                        

                # If circuit_data is not equal to prev_value and circuit_data is 20 bits long, print circuit_data and write to file
                if circuit_data != prev_value and len(circuit_data) == 20:
                    print(circuit_data) # Print binary string 
                    DataList.append(circuit_data)
                    prev_value = circuit_data # Set prev_value to circuit_data
                # if len(circuit_data) == 20:
                #     print(circuit_data) # Print binary string 
                #     f.flush()  # flush write buffer to force data to be written to file

                prev_value_first_3bits = first_3bits # Set prev_value to first_3bits