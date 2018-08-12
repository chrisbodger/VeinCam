# Concept of Operations

## Table of Contents
* [Project Vision](#project-vision)
  * [Value Proposition](#value-proposition)
  * [Project Scope](#project-scope)
* [Stakeholders](#stakeholders)
  * [Project Team](#project-team)
* [Resources](#resources)
  * [Funding](#funding)
  * [Tools](#tools)
  * [Project Administration](#project-administration)
  * [Manufacturing and Testing](#manufacturing-and-testing)
    * [Bill of Materials](#bill-of-materials)
  * [Programming](#programming)
* [Project Management](#project-management)
  * [Deliverables](#deliverables)
  * [Milestones](#milestones)
  * [Audit Goals](#audit-goals)
  * [Timelines](#timelines)
  * [Work Breakdown Structure](#work-breakdown-structure)
* [Risk Analysis](#risk-analysis)
  * [Safety Risk Analysis](#safety-risk-analysis)
* [References](#references)

---

## Project Vision
The VeinCam is based on the [Venenfinder project](https://hackaday.io/project/26158-assistance-system-for-vein-detection) submitted during the 2017 HackADay event. The goal was to create an affordable device that produces a clear image of a suitable vein for superficial venous puncture, a procedure that is a requirement for patient blood testing and the delivery of external drug administration.

### Value Proposition
Our VeinCam device will help both medical professionals and patients who want to perform intravenous procedures by externally visualising forearm veins. It will increase the likelihood of successfully accessing those veins to reduce patient discomfort and increase medical staff efficiency and introvenous compentency.

### Project Scope
The project aims to greatly extend and refine what was achieved in the Venenfinder HackADay project; automating and adding to some of the functionality while remaining a cost effective solution. Ideally, the device will be able to be built and used by patients with chronic diseases that regularly require personal drug administration.

The device should be portable, hands-free and wireless. Veins will be illuminated using near-infrared light, and the scattering from this light detected by a Raspberry Pi device equipped with a PiCam module.

Due to the variation in human skin in its absorption of different wavelengths of light, an unclear image can be produced, a proper candidate may be undetected. The software from the Venenfinder project will be heavily modified, incorporating intelligent OpenCV scripts to perform automatic adjustments to the lighting and contrast settings.  This adjusts the contrast of the image to allow for the easier detection of veins, with minimal to no input from the user.

A physical potentiometer and/or smartphone app interface will act as the manual control for adjusting light settings to get the clearest image possible.

### Project Comparison
Given that this project is continuing on from the Veinfinder project, it is worth noting what we are building upon.

#### Venenfinder Features
The Venenfinder team were able to produce a device that was able to use a near-Infrared light to illuminate a patient's veins. The device uses a Raspberry Pi, a noIR camera module, and a 3x3 array of IR LEDs. Brightness of the LEDs and contrast ratios were manually adjusted using potentiometers to adjust intercepted voltages between the array and the RPi. The camera image is then streamed to a secondary web enabled device through a web browser. This method works for devices ranging from mobile phones to desktop PCs.  Unfortunately, the device was quite large and bulky, and required an external power source to power the device.

#### VeinCam Core Features
The VeinCam project hopes to utilise similar hardware to the Venenfinder project (Raspberry Pi, PiCam, IR LEDs) and extend the software's capabilities to automatically adjusts the infrared light filtration, brightness and contrast to produce the clearest image possible without manual adjustment.

In further adding to the Venenfinder project, our aim is to produce a device that is battery powered, completely wireless and reduce the size of the device to be comfortably held in one hand. Being a wireless device, we need to ensure the device is as power efficient as possible and does not require recharging more than what it is used. As part of the new housing for the device, a mounting system will be integrated, and a mount be devised for hands-free use.

#### VeinCam Testing and Future Development Plans
Once our core device has reached the prototype stage, extensive testing will be completed on varying skin conditions and appearances - ranging from light skin to dark skin, clean, tattooed areas and other skin irritations, all in effort to enhance the effectiveness of the device. Further this, we plan to incorporate subject detection algorithms to help nominate suitable veins, should time allow.

Requiring further investigation and implementation, the device may be able to be shrunk to a smaller platform, such as the Raspberry Pi Zero. This would allow for the device to become a lot cheaper to build, reducing the size to something that fits into the palm of your hand, and be able to conserve more power. Implementations and performance would need to be investigated, as the Pi Zero may not be able to process the video stream as effectively as the it's larger cousin.

#### Feature Summary
| Venenfinder | VeinCam | Future Development |
| --- | --- | --- |
| IR Illumination | IR Illumination | Various Skin Conditions |
| Camera | Camera | Vein Identification |
| Manual Brightness Adjustment | Auto Brightness Adjustment | Smaller Platform |
| Manual Contrast Adjustment | Auto Contrast Adjustment | Extended Battery Life |
| Manual IR Adjustment | Auto IR Adjustment |   |
|   | Wireless |   |
|   | Portable |   |
|   | Smaller Footprint |   |
|   | AI Image Processing |   |

---

## Stakeholders
The following groups have been identified as stakeholders for this project:
* Project Client - Provides feedback on project progress
* Project Team - Produces the Project Output and actions constructive feedback from other stakeholders
* Shadow Team - Observes the Project and provides constructive feedback
* Course Tutor - Provides feedback on project progress
* Course Convener - Provides feedback on project progress

### Project Team
The project team consists of four undergraduate engineers:

| Name | Role |
| --- | --- |
| Christopher Bodger | Lead Hardware Engineer |
| Alexander Ollman | Lead Programmer |
| Stephanie Pratt | Stakeholder Liaison |
| Jonathan McPhail | Secretary |

Ben Healey is our client for this project, currently an ANU Medical Student, and employee of ACT Health.

---

## Resources
### Funding
At most, the project should cost no more than the $400 proposed in the design brief. This will include the hardware and components necessary.

Ideally, the project should cost less than this. A [Bill of Materials](#bill-of-materials) with associated can be seen below.

### Tools

Tools likely to be used throughout this project include:
- Soldering Iron
- 3D Printer
- Laser Cutter
- Dremmel
- Screwdriver, screws, nuts and bolts.

All safety precautions outlined by the ANU Makerspace's Terms and Conditions will be followed during the use of instrument or tool, regardless of where and how it is used. A safety risk analysis has been performed at the bottom of this document.

#### Project Administration
* GitHub
* GitHub Pages
* Google Drive
* Facebook Messenger Platform

#### Manufacturing and Testing
* Ian Ross Design Studio
* ANU Makerspace

##### Bill of Materials
An initial Bill of Materials has been drafted below of what we expect the project to cost.

| Component | Cost (AUD) | Supplied By Client |
| --- | :---: | :---: |
| Raspberry Pi 3 | $65 | Y |
| Raspberry Pi Zero | $20 | Y |
| Raspberry PiCam | $50 | Y |
| Raspberry Pi Battery Module | $90 | Y |
| 940nm near-Infrared LEDs | $15 | N |
| 220 Ohm Resistors | $5 | N |
| 40 Pin Female Header | $2 | N |
| Neodymium Magnets | $5 | N |
| IR Filter | $10 | N |
| Sub-Total (Minus Client Provided Materials) | $37 |  |
| Total | $262 |   |


#### Programming
* Source code from the Venenfinder HackADay project has been utilised, as it achieves close to the client's desired deliverable. This code will then be modified to achieve the client's desired features, including auto-vein focus.

---

## Project Management
### Deliverables
The initial deliverables are as follows:  

#### Baseline Deliverable
* Configure device based on Venenfinder to be able to automatically adjust contrast.
* Design and manufacture a prototype chassis to house Pi modules to allow for handsfree real time visualization

#### Stretch Deliverables
* Configure device to run off of Pi Zero module
  - Offload image processing to secondary device
* Optimise for different use-case scenarios (e.g. tattooed skin, dark skin)
* Optimise device to visualise blood flow to identify best candidate vein

### Milestones
#### Milestone 1
Construct Functional prototype based off of Venenfinder design.

#### Milestone 2
Configure software to auto-focus and design hardware to reduce product's form factor.

#### Milestone 3
Initial AutoCAD design of 3D-printable chassis, maximize auto-focus function for clear image definition.

#### Milestone 4
Final AutoCAD design and phyiscal print-out of chassis, accompanying web/smartphone appication to display camera image, contain adjustable settings.

### Audit Goals
#### Audit 1
* Complete ConOps Version 1

#### Audit 2
* Update ConOps to Version 2
* Complete requirements analysis
* Reach Milestone 2

#### Audit 3
* Achieve Milestone 3/4 with accompanying verification and validation

Milestones are subject to change as the project evolves.

### Timelines
An [indicative schedule](https://docs.google.com/spreadsheets/d/1nfNqFCF2ieP5CyVmqDSeZ3oXegxcCG4hojdd6fMcq9Y/edit?usp=sharing) has been drafted for the project.

### Work Breakdown Structure
1. Requirements Analysis  
   1.1. Review PoC  
   1.2. Perform risk analysis  
   1.3. Brainstorm requirements (in-house)  
   1.4. Develop requirements with client  
   1.5. Finalise requirements  
2. Prototyping  
   2.1. Design hardware  
   2.2. Manufacture and construct hardware  
   2.3. Design baseline software  
   2.4. Integrate software  
   2.5. Update software with stretch deliverables
3. Validation & Verification  
   3.1. Test prototype in-house  
   3.2. Test prototype with users  
   3.3. Conduct performance review  
4. Documentation  
   4.1. Write ConOps v1  
   4.2. Update ConOps v2  
   4.3. Create poster  
   4.4. Organise repository  

---

## Risk Analysis
All risk analysis performed throughout this project will be in accordance to the Australian and New Zealand Industry Standard AS/NZS 4360:2004.

![Risk Matrix](https://github.com/chrisbodger/VeinCam/blob/master/images/ConOps/risk-matrix.png)

Potential risks to the success of the project have been brainstormed in order to understand them and mitigate either there severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Not clearly understanding or defining client's requirements for the project. | Product does not meet client requirements, client disatisfied, requires redoing work, going over budget and schedule to redesign | D | 3 | Maintain regular contact with client regarding progress and milestone completion. |
| Not defining scope of project and setting clear and achieveable milestones. | No clear definition of project progress, feature creep over time results in lack of physical product, no clear "stopping point" for project or completed product, client disatisifed, product does not meet customer requirements, likely to be overbudget. | C | 3 | Defining scope early and ensuring we stick to milestones and their respective outputs to ensure we do not deviate on a project tangent. |
| Device cannot be utilized as a medical device due to not meeting medical certification criteria. | Unable to deliver product to medical professionals, which is client's ultimate goal for the project. | C | 2 | Ensure client is aware of potential certification issues, and that they verify during devlopment whether the device can be used with and/or without the medical classification. |

### Safety Risk Analysis
In developing the prototype there is a chance of injury, similar to above these risks have been listed and steps taken to mitigate their severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Personal harm whilst using listed tools (incl. burns, shocks, cuts) | Pain, discomfort and possible medical attention. | D | 3 | Ensuring all team members are familiar with the safety training of the ANU Makerspace/Engineering workshop, supervision by one other team member when using potentially dangerous tools. |
| Damage to Hardware due to physical impact or electrostatic discharge (ESD) | Loss of data, hardware faliure, schedule delays to order and replace damaged hardware. | E | 4 | Ensuring hardware is never placed in an area where it is likely to be damaged, always in full visible sight. Observing proper ESD safety techniques, such as regularly grounding ourselves and only contacting circuitry by edges. |

---

## References
[Venenfinder Github](https://github.com/Myrijam/Venenfinder)

[Venenfinder HackAThon Page](https://hackaday.io/project/26158-assistance-system-for-vein-detection)


This Project is licensed under the Creative Commons license.
