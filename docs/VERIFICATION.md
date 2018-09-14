# Device Specification Verification
The prototype device must be verified against the specifications as developed from the [Requirements](REQUIREMENTS.md) to ensure a successful prototype. A series of tests have been created to verify the design:

## Tests
Test IDs correlate with specification IDs found in the [Requirements](REQUIREMENTS.md) document. At this stage venous puncture is not permitted for testing and there is no stand to address a number of specifications, though tests have been considered.

| ID | Test |
| --- | --- |
| 1 | The estimated material cost of the prototype. This includes pre-purchased materials but does not include labour. |
| 2.1 | A yes/no judgement from the user on whether a candidate vein can be clearly seen. Minimum sample size n=10. |
| 2.2 | User judgement on the distance at which the picture is most in focus. |
| 2.3 | Device set to minimum and maximum height and must remain stable for at least 1 minute. |
| 2.4 | Device set to operate and not interfered with until failure or a 10 minute limit reached |
| 2.5 | Measure the time taken for the device to use a full charge when left to stream indefinitely. |
| 3.1 | User judgement of significant packet loss when increasing the distance from camera device to streaming device. |
| 3.2 | TBA |
| 4 | Measure the maximum dimensions of the prototype |
| 5.1 | Theoretical estimate based on 3D printing finishing procedure data |
| 5.2 | Measurement of all gaps in the closed device and recording of the maximum |
| 6.1 | A yes/no judgement of a user who performs routine venous puncture on whether or not they would "use the device". |
| 6.2 | Measure the time taken from switching on the device to streaming |
| 6.3 | Test the stream on a number of different devices and OS (e.g. windows desktop, apple tablet etc.) |
| 7.1 | The number of steps of how to construct the device, dictated by an independent user being able to construct the device |
| 7.2 | Provide a set of instructions to an independent individual and measure how long it takes them to construct the device |
| 8.1-4 | Similar to 2.1 but ensuring the potential patient has a dark complexion, high BMI, thick hair or tattoos covering candidate veins |
| 8.5 | Similar to 2.1 |

## Results Table Template
As prototypes are tested the results will be updated here. Raw data can be found [here](https://docs.google.com/spreadsheets/d/18sSy89GIRTKhPBCF92-t4Pr2AGmHzw_IFHvKGeLFWAo/edit?usp=sharing).

| ID | Specification | Metric | Benchmark | Result |
| --- | --- | --- | --- | --- |
| 1 | Total Cost | $ | <250 | |
| 2.1 | Automatic Contrast Adjustment (for ideal scenario) | % | >90 | |
| 2.2 | Camera Focal Length | mm | 300-500 | |
| 2.3 | Adjustable Set Height | mm | 300-500 | |
| 2.4 | Handsfree Operation | min | >5 | |
| 2.5 | Battery Life | min | >60 | |
| 3.1 | Wireless Range | m | >1 | |
| 3.2 | Stream Delay | ms | <1000 | |
| 4 | Form Factor | mm | <150 x 90 x 70 | |
| 5.1 | Surface Roughness (R<sub>a</sub>) | &mu;m | <10 | |
| 5.2 | Gapless Case | mm | <1 | |
| 6.1 | User Acceptance | % | >90 | |
| 6.2 | Boot Time | s | <15 | |
| 6.3 | OS Compatibility | # | >2 | |
| 7.1 | Construction Steps | # | <5 | |
| 7.2 | Construction Time | hrs | <2 | |
| 8.1 | Automatic Contrast Adjustment (for any complexion) | % | 80 | |
| 8.2 | Automatic Contrast Adjustment (for high BMI/obesity) | % | 80 | |
| 8.3 | Automatic Contrast Adjustment (for any amount of hair) | % | 80 | |
| 8.4 | Automatic Contrast Adjustment (for tattooed area) | % | 80 | |
| 8.5 | Visualise Vascular Blood Flow | % | 80 | |
