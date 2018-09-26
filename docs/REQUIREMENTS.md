# Device Requirements and Design Specifications
Requirements were gathered from the client and refined into measurable specifications. The sets of both requirements and specifications should be considered evolutionary and may change through prototyping and testing.

## Requirements
Requirements have been developed through conversation with the project client resulting in a total of eight that would make the VeinCam a success.

| ID | Requirement |
| --- | --- |
| 1 | The device must be inexpensive compared to devices that have similar functions |
| 2 | The device must be handsfree |
| 3 | The device must be able to wirelessly connect to an external device with a screen |
| 4 | The device must be portable and mobile |
| 5 | The device must be simple to use |
| 6 | The device must be simple to construct |
| 8* | The device must improve venous puncture success in all use-cases (e.g dark-skinned, tattooed, hairy) |

*Requirement 8 is part of a stretch deliverable for the project.

## Specifications
The requirements were broken down into specifications that will provide validation for the project and can be verified through testing.

| ID | Specification | Metric | Benchmark |
| --- | --- | --- | --- |
| 1 | Total Cost | $ | <250 |
| 2.1 | Automatic Contrast Adjustment (for ideal scenario) | % | >90 |
| 2.2 | Camera Focal Length | mm | 300-500 |
| 2.3 | Adjustable Set Height | mm | 300-500 |
| 2.4 | Handsfree Operation | min | >5 |
| 2.5 | Battery Life | min | >60 |
| 3.1 | Wireless Range | m | >1 |
| 3.2 | Stream Delay | ms | <1000 |
| 4 | Form Factor | mm | <150 x 90 x 70 |
| 6.1 | User Acceptance | % | >90 |
| 6.2 | Boot Time | s | <15 |
| 6.3 | OS Compatibility | # | >2 |
| 7.1 | Construction Steps | # | <5 |
| 7.2 | Construction Time | hrs | <2 |
| 8.1 | Automatic Contrast Adjustment (for any complexion) | % | 80 |
| 8.2 | Automatic Contrast Adjustment (for high BMI/obesity) | % | 80 |
| 8.3 | Automatic Contrast Adjustment (for any amount of hair) | % | 80 |
| 8.4 | Automatic Contrast Adjustment (for tattooed area) | % | 80 |
| 8.5 | Visualise Vascular Blood Flow | % | 80 |

### Description
**1. Total Cost -** The total cost of all components necessary to construct the VeinCam

**2.1. Automatic Contrast Adjustment (for ideal scenario) -** The success rate of the device to automatically adjust the contrast of the streamed image such that a candidate vein can be selected. Ideal situation is with a patient with a light complexion, against a white background.

**2.2. Camera Focal Length -** The focal length of the camera used in the device. Must have an image in focus at a height where it will not interfere with the user or the sterile field.

**2.3. Adjustable Set Height -** The heights that the device can be held still without human interaction once set in the appropriate position (i.e within the camera focal length).

**2.4. Handsfree Operation -** The time that both the physical device and the software interface can operate without human interaction.

**2.5. Battery Life -** The amount of time the device can be used (while streaming) without needing to be plugged in to recharge.

**3.1. Wireless Range -** The range that the device is able to communicate wirelessly with an external device.

**3.2. Stream Delay -** The time taken for the recorded image to be processed and appear on the external device.

**4. Form Factor -** The size and shape of the device.

**5.1. Surface Roughness -** The surface roughness of the device casing. Must allow for simple cleaning.

**5.2. Gapless Case -** The size of gaps in the case. Must be small to ensure protection of electronics from wiping.

**6.1. User Acceptance -** The success rate that the device with users. Measured by user testing and feedback.

**6.2. Boot Time -** The time taken from switching the device on to an image being produced.

**6.3. OS Compatibility -** The number of operating systems that the device is compatible with.

*Note - More specifications may be generated for Requirement 6 after initial testing.*

**7.1. Construction Steps -** The number of steps needed to construct the device from scratch.

**7.2. Construction Time -** The time taken for an independent user to construct the device from scratch. To be tested by independent users.

**8.1-4. Automatic Contrast Adjustment (for various use cases) -** Similar to 2.1. however in scenarios where vein detection has been shown to be more difficult.

**8.5. Visualise Vascular Blood FLow -** The ability of the device to visualise real-time blood flow through candidate veins. Measured through success rate in user testing.

| Date | Section | Change | Justification |
| --- | --- | --- | --- |
| 26/8/18 | [Requirements](#requirements) | Remove sterilisation requirement and associated specifications: gapless case and surface roughness. | The device is to be used as an educational tool as opposed to a medical device. |
| 26/8/18 | [Requirements](#requirements) |  |  |
