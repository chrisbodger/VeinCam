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
  * [Programming](#programming)
* [Project Management](#project-management)
  * [Milestones and Deliverables](#milestones-and-deliverables)
    * [Audit 1](#audit-1)
    * [Audit 2](#audit-2)
    * [Audit 3](#audit-2)
  * [Timelines](#timelines)
  * [Work Breakdown Structure](#work-breakdown-structure)
* [Deliverables](#deliverables)
* [Risk Analysis](#risks-analysis)
* [References](#references)

## Project Vision
The VeinCam is based on the [Venenfinder project](https://hackaday.io/project/26158-assistance-system-for-vein-detection) submitted during the 2017 HackADay event. The goal was to create an affordable device that produces a clear image of a suitable vein for superficial venous puncture, a procedure that is a requirement for patient blood testing and the delivery of external drug administration. 

### Value Proposition
Our VeinCam device will help medical professionals who want to perform intravenous procedures by externally visualising a patient’s veins. It will increase the likelihood of successfully accessing those veins to reduce patient discomfort and increase medical staff efficiency and proficiency with the procedure.

### Project Scope
The project aims to build on what was achieved in the Venenfinder project; automating and adding to some of the functions while remaining a cost effective solution. Ideally, the device will be able to be built and used by patients with chronic diseases that regularly require personal drug administration.

The device should be portable, hands-free and wireless. Veins will be illuminated using near-infrared light, and the scattering from this light detected by a Raspberry Pi device equipped with a PiCam module.

Due to the variation in human skin in its absorption of different wavelengths of light, an unclear image can be produced, a proper candidate may be undetected. Having an auto-switch feature to automatically adjust the wavelength emitted will build on what has already been achieved. This adjusts the contrast of the image to allow for the easier detection of veins, with minimal to no input from the user.

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
| Christopher Bodger | Lead Mechanical Engineer |
| Alexander Ollman | Lead Programmer |
| Stephanie Pratt | Stakeholder Liaison |
| Jonathan McPhail | Secretary |

Ben Healey is our client for this project, currently an ANU Medical Student, and employee of ACT Health.

## Resources
### Funding
The project brief informs us that we will need to take out a microgrant of around $100, with the client willing to fund us a further $300 should it be required. at most, the project should cost no more than the $400 proposed, but ideally, the project should cost less than this.

### Tools
Several Tools will be used for this project, and they are listed below

#### Project Administration
* GitHub
* GitHub Pages
* Google Drive
* Facebook Messenger Platform

#### Manufacturing and Testing
**TABLE OF MATERIALS GOES HERE**
* Ian Ross Design Studio
* ANU Makerspace

#### Programming
* Source code from the Venenfinder HackADay project has been utilised, as it achieves close to the client's desired deliverable. This code will then be modified to achieve the client's desired features, including auto-vein focus. 

## Project Management
### Milestones 
Milestones are yet to be determined. clear goals will be made after our meeting with our client.

An initial milestone layout:
**Milestone 1:** Construct Functional prototype based off of Venenfinder design.  
**Milestone 2:** Configure software to auto-focus and design hardware to reduce product's form factor.
**Milestone 3:** Initial AutoCAD design of 3D-printable chassis, maximize auto-focus function for clear image definition.
**Milestone 4:** Final AutoCAD design and phyiscal print-out of chassis, accompanying web/smartphone appication to display camera image, contain adjustable settings.

### Deliverables
#### Audit 1

#### Audit 2

#### Audit 3
The project will hope to achieve a finalised prototype that meets a cost effective target of AU$300, can be easily assembled, and produce results equivalent to devices currently in use in hospitals that cost several magnitudes more than the VeinCam.

The device should conform to hospital hygiene practices, as well as their Information Communication Technology Services Policy.

#### Poster and Presentation 

### Timelines
Project timelines are yet to be determined.

### Work Breakdown Structure
1. Requirements Analysis  
   1.1. Review PoC  
   1.2. Perform risk analysis  
   1.3. Brainstorm requirements (in-house)  
   1.4. Develop requirements with client  
   1.5. Develop requirements with target users  
   1.6. Finalise requirements  
2. Prototyping  
   2.1. Design hardware  
   2.2. Manufacture and construct hardware  
   2.3. Design software  
   2.4. Integrate software  
3. Validation & Verification  
   3.1. Test prototyype in-house  
   3.2. Test prototype with users  
   3.3. Conduct performance review  
4. Documentation  
   4.1. ConOps  
   4.2. Milestones  
   4.3. Budgeting  
   4.4. Requirements  
   4.5. Prototype design  
   4.6. Validation and verification

## Risk Analysis
At this initial project stage, the risks involved with this project lie within the governance of the project itself. Risks associated with the product and its physical development will be stated in ConOps prior to Audit 2.

Risk:
Not clearly understanding or defining client's requirements for the project.
Consequence(s):
Product does not meet client requirements, client disatisfied, requires redoing work, going over budget and schedule to redesign

Risk:
Not defining scope of project and setting clear and achieveable milestones.
Consequence(s):
no clear definition of project progress, feature creep over time results in lack of physical product, no clear "stopping point" for project or completed product, client disatisifed, product does not meet customer requirements, likely to be overbudget.
                                               

## References
[Venenfinder Github](https://github.com/Myrijam/Venenfinder)

[Venenfinder HackAThon Page](https://hackaday.io/project/26158-assistance-system-for-vein-detection)



This Project is licensed under the Creative Commons license.
