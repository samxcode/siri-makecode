def on_forever():
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)

def on_forever2():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(1000)
basic.forever(on_forever2)
