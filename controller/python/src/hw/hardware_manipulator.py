from gpiozero import LED

# side c1 lights
red_c1 = LED(2)
yellow_c1 = LED(2)
green_c1 = LED(3)

# side c2 lights
red_c2 = LED(17)
yellow_c2 = LED(17)
green_c2 = LED(27)

# side b1 lights
red_b1 = LED(5)
yellow_b1 = LED(6)
green_b1 = LED(6)

# side b2 lights
red_b2 = LED(13)
yellow_b2 = LED(13)
green_b2 = LED(19)

# side d1 lights
red_d1 = LED(23)
yellow_d1 = LED(23)
green_d1 = LED(24)

# side d2 lights
red_d2 = LED(8)
yellow_d2 = LED(8)
green_d2 = LED(7)

# side a1 lights
red_a1 = LED(12)
yellow_a1 = LED(12)
green_a1 = LED(16)

# side a2 lights
red_a2 = LED(20)
yellow_a2 = LED(20)
green_a2 = LED(21)

green_lights: [LED] = [
    green_a1,
    green_a2,
    green_b1,
    green_b2,
    green_c1,
    green_c2,
    green_d1,
    green_d2,
]
yellow_lights: [LED] = [
    yellow_a1,
    yellow_a2,
    yellow_b1,
    yellow_b2,
    yellow_c1,
    yellow_c2,
    yellow_d1,
    yellow_d2,
]
red_lights: [LED] = [
    red_a1,
    red_a2,
    red_b1,
    red_b2,
    red_c1,
    red_c2,
    red_d1,
    red_d2,
]


def turn_greens_on(on_led_s: [int]):
    for index in range(0, 8):
        if index in on_led_s:
            red_lights[index].off()
            green_lights[index].on()
        else:
            yellow_lights[index].off()
            red_lights[index].on()
    pass


def turn_yellows_on(on_led_s: [int]):
    for index in range(0, 8):
        if index in on_led_s:
            green_lights[index].off()
            yellow_lights[index].on()
    pass
