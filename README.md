# Event Timer
## Description
Run countdown for your event from your computer based on event details. Lets say there is some event and you want all that stuff being displayed in terminal or your are too lazy to visit certain website then Event Timer comes to rescue.

## Features
1. Nepali && Indian && UTC Countdown
2. Multiple number of events now supported
3. Multiple time formats `GMT/UTC`, `EST|EDT`, `PCT` support.

## Configuration
Edit lib/Globals.py for event management. See wiki for more data.

## Usage
`python3 EventTimer.py`

## Error and Warning
See Warning.md. See Event Wiki. Sometime base10 int error means event is finished and must be removed or commented out

## Todo
1. Send notification `libnotifysend` and `slack notification` when timer is reached.
2. IST Time format to be added

