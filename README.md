# plotter

Code for a 36" x 48" drawing robot.

### TODO (higher denotes priority
- [ ] Drive motors
- [ ] write motor calibration software
- [ ] determine the motor direction schema
- [ ] convert image to the correct dimensions
- [ ] convert lines to individual commands
- [ ] write controller software (determine library)
- [ ] cv2 image processing to lines

### System Electronics
- Raspberry Pi (one with bluetooth for controllers? maybe wired is fine too)
- 2 vertical steppers (or maybe a drill?)
- x and y axis steppers
- servo or mini-solenoid for pen up/down
- compatible motor drivers
- power supply?

#### Rough power requirements
Most of the power will come from the steppers and drivers. (figure out this)

### Interaction
I plan on having an XBOX controller mode and a preset mode.

The controller mode would allow live control of the pen which raises the
system's vertical axis speed requirement. (cool party trick, might need the
drill motor for this.

The preset mode would be inputting some sort of file either self-defined (easier)
or GCODE (can rip other people's files).


