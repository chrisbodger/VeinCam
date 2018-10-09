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
| 7* | The device must display veins in as many use-cases as possible (e.g dark-skinned, tattooed, hairy) |

*Requirement 7 has elements of a stretch deliverable for the project.

## Specifications
The requirements were broken down into specifications that will provide validation for the project and can be verified through testing.

| ID | Specification | Metric | Benchmark |
| --- | --- | --- | --- |
| 1 | Total Cost | $ | <250 |
| 2.1 | Camera Focal Length | mm | 300-500 |
| 2.2 | Adjustable Set Height | mm | 300-500 |
| 2.3 | Handsfree Operation | min | >5 |
| 2.4 | Battery Life | min | >60 |
| 3.1 | Wireless Range | m | >1 |
| 3.2 | Stream Delay | ms | <1000 |
| 4 | Form Factor | mm | <150 x 90 x 70 |
| 5.1 | User Acceptance | % | >90 |
| 5.2 | Boot Time | s | <15 |
| 5.3 | OS Compatibility | # | >2 |
| 6.1 | Construction Steps | # | <5 |
| 6.2 | Construction Time | hrs | <2 |
| 7.1 | Automatic Contrast Adjustment (for ideal scenario) | % | >90 |
| 7.2 | Automatic Contrast Adjustment (for any complexion) | % | 80 |
| 7.3 | Automatic Contrast Adjustment (for high BMI/obesity) | % | 80 |
| 7.4 | Automatic Contrast Adjustment (for any amount of hair) | % | 80 |
| 7.5 | Automatic Contrast Adjustment (for tattooed area) | % | 80 |
| 7.6 | Visualise Vascular Blood Flow | % | 80 |

### Description
**1. Total Cost -** The total cost of all components necessary to construct the VeinCam

**2.1. Camera Focal Length -** The focal length of the camera used in the device. Must have an image in focus at a height where it will not interfere with the users.

**2.2. Adjustable Set Height -** The heights that the device can be held still without human interaction once set in the appropriate position (i.e within the camera focal length).

**2.3. Handsfree Operation -** The time that both the physical device and the software interface can operate without human interaction.

**2.4. Battery Life -** The amount of time the device can be used (while streaming) without needing to be plugged in to recharge.

**3.1. Wireless Range -** The range that the device is able to communicate wirelessly with an external device.

**3.2. Stream Delay -** The time taken for the recorded image to be processed and appear on the external device.

**4. Form Factor -** The size and shape of the device.

**5.1. User Acceptance -** The success rate that the device with users. Measured by user testing and feedback.

**5.2. Boot Time -** The time taken from switching the device on to an image being produced.

**5.3. OS Compatibility -** The number of operating systems that the device is compatible with.

*Note - More specifications may be generated for Requirement 5 after initial testing.*

**6.1. Construction Steps -** The number of steps needed to construct the device from scratch.

**6.2. Construction Time -** The time taken for an independent user to construct the device from scratch. To be tested by independent users.

**7.1-5. Automatic Contrast Adjustment (for various use cases) -** The success rate of the device to automatically adjust the contrast of the streamed image such that veins can be clearly seen, as judged by the user. Ideal situation is with a patient with a light complexion, against a white background. Other scenarios are where vein detection has been shown to be more difficult.

**7.6. Visualise Vascular Blood FLow -** The ability of the device to visualise real-time blood flow. Measured through success rate in user testing.

## Change Log

| Date | Section | Change | Justification |
| --- | --- | --- | --- |
| 26/9/18 | [Requirements](#requirements) | Remove sterilisation requirement and associated specifications: gapless case and surface roughness. | The device is to be used as an educational tool as opposed to a medical device. |
| 26/9/18 | [Requirements](#requirements) | The device does not need to improve venous puncture but still work for as many use cases as possible | As above. |
| 29/9/18 | [Specifications](#specifications) | Moved automatic contrast adjustment (ideal scenario) to requirement 7. | Testing has to be split up between device and user, this groups more user testing together. |
