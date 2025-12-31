import board
import busio
import digitalio
import espcamera

i2c = busio.I2C(board.GPIO39, board.GPIO40)

picButton = digitalio.DigitalInOut(board.GPIO1)
picButton.direction = digitalio.Direction.INPUT
picButton.pull = digitalio.Pull.UP

recButton = digitalio.DigitalInOut(board.GPIO2)
recButton.direction = digitalio.Direction.INPUT
recButton.pull = digitalio.Pull.UP
cam = espcamera.Camera(
    data_pins=[
        board.GPIO15,  # DVP_Y2
        board.GPIO17,  # DVP_Y3
        board.GPIO18,  # DVP_Y4
        board.GPIO16,  # DVP_Y5
        board.GPIO14,  # DVP_Y6
        board.GPIO12,  # DVP_Y7
        board.GPIO11,  # DVP_Y8
        board.GPIO48,  # DVP_Y9
    ],
    external_clock_pin=board.GPIO10,   # XMCLK
    pixel_clock_pin=board.GPIO13,      # DVP_PCLK
    vsync_pin=board.GPIO38,            # DVP_VSYNC
    href_pin=board.GPIO47,             # DVP_HREF
    pixel_format=espcamera.PixelFormat.RGB565,
    frame_size=espcamera.FrameSize.R240X240,
    i2c=i2c,
    external_clock_frequency=20_000_000,
    framebuffer_count=2,
    grab_mode=espcamera.GrabMode.WHEN_EMPTY
)

while True:
    if not picButton.value:
        print("Picture button pressed")
        
    if not recButton.value:
        print("Record button pressed")