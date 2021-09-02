"""
Read the REPL to receive color data for the neopixel.
"""
import board
import time
import supervisor

################################################################
# init board's LEDs for visual output
# replace with your own pins and stuff
################################################################

pix = None
if hasattr(board, "NEOPIXEL"):
    import neopixel
    pix = neopixel.NeoPixel(board.NEOPIXEL, 4)
    pix.fill((32, 16, 0))
else:
    print("This board is not equipped with a Neopixel.")

################################################################
# loop-y-loop
################################################################

while True:
    # read the secondary serial line by line
    # when there's data, with a timeout
    status = False
    while supervisor.runtime.serial_connected:
        if status == False:
            pix.fill((0, 16, 0))
            status = True
        if supervisor.runtime.serial_bytes_available:
            data_in = input()
            # try to convert the data to a dict (with JSON)
            data = None
            if len(data_in) > 0:
                print(data_in)
                if(data_in[0]=='a'):
                    pix.fill((0, 0, 16))

    pix.fill((16, 0, 0))

    time.sleep(0.01)