# Meeting Minutes - 4/8/2018

| Attending: | Absent: |
| :---: | :---: |
| Joey McPhail | |
| Steph Pratt | |
| Chris Bodger | |
| | Alex Ollman |
| Ben Healey | |
---

## Agenda - Things to discuss with Client
* Organisation and Communication
  * When and how would you like to be updated? Only when there are Major goals/setbacks or weekly? By email or in person? Regular meeting on Saturdays or over email?
  * Any issues with accessing/understanding the github repository/landing page?
  * Steph will be your main point of communication
  * Role assignment for the rest of the team
  * Concept of operations (ConOps) - Basically a detailed plan for how we are going to tackle and break down this project. Need a sign off from all stakeholders everytime there is a change to the ConOps - we think this can just be digital. 

* Project goals
  * Are you happy with our project vision? 
  * What are the minimum aims (base goals) of the advice? (primary deliverables)
  * What the aspects of the device that are optional reach goals?
 
* Requirements
  * Aspects of the user interface?
    * Simple operation, minimal steps required for setup... etc?
  * What are the privacy (patient confidentiality) and safety standards that need to be met? (hospital policy) Where could we find this information?
  * Hardware and software features
    * potential embedded screen?
    * bluetooth connection or WiFi hotspot?
  * What hardware do you have already exactly?
    
  * Costing limitations
    * Cost of hardware and additional parts? How much are you happy for us to spend? Can get about $100 microgrant
    * Range of final cost of manufacturing the device?
  * Testing requirements? Any ideas if/how we could do this?

---

## Organisation and Communication
* Happy with email as the main form of communication
  * This is in both directions - if Ben needs to send us something
  * In the future feedback forms through google forms

---

## Project Goals
* Ben happy with current vision statement etc.
* Baseline goal:
  * Have the adjustable contrast function of the device working.
    * Might be necessary to get multiple LEDs to supply different wavelengths for focus and contrast.
* Stretch goals:
  * Have a case and setup that allows the camera to remain still
  * Be able to be used on multiple patients (address tattoos, different skin colour, youth)
    * There is pre-existing research on patients that make identification more difficult
  * Be able to run off the PiZero module and have the external device handle processing (to reduce total costs)
  * Be able to visualize blood flow so a candidate vein with high flow can be selected
  * Have different modes to address image processing to ensure real time visualization.

---

## Hardware
* Already have:
  * Raspberry Pi 3: Module B+
  * PiJuice Battery
  * NoIR camera
  * LED (850nm)
  * PiZero
  * Charger and MicroUSB cable
  * Example stand
  * White sheet to simulate hospital bed covers
  * Tourniquet

* Ben can source:
  * Bluey (to be used for contrast tests)

* Might Need:
  * Different wavelenght LEDs (780, 940 nm)
  * PCB

* Have most of what we need and shouldn't need to apply for the microgrant

---

## Requirements
* Total cost of finished product: $200-$250
* Happy with blutooth or wifi, or whatever wireless communications will work best.
* Policy:
  * Should be fine as it should not be interfering with the sterile part of the procedure (sterilitiy begins after finding the vein)
  * As long as its able to be cleaned.
  * Recording not allowed, but should be fine if it is just streaming
  * Can review in detail getting policy documents from Ben
* Testing:
  * On ourselves or volunteers
  * Ben can take to the hospital
  * Stretch goal: user testing to ensure acceptance/usefulness can be done in the hospital
