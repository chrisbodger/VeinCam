# Device Specification Verification
The prototype device must be verified against the specifications as developed from the [Requirements](REQUIREMENTS.md) to ensure a successful prototype. A series of tests have been created to verify the design:

## Tests
Test IDs correlate with specification IDs found in the [Requirements](REQUIREMENTS.md) document. At this stage venous puncture is not permitted for testing and there is no stand to address a number of specifications, though tests have been considered.

| ID | Device/User Testing | Test |
| --- | --- | --- |
| 1 | D | The estimated material cost of the prototype. This includes pre-purchased materials but does not include labour. |
| 2.1 | D | User judgement on the distance at which the picture is most in focus. |
| 2.2 | D | Device set to minimum and maximum height and must remain stable for at least 1 minute. |
| 2.3 | D | Device set to operate and not interfered with until failure or a 10 minute limit reached |
| 2.4 | D | Measure the time taken for the device to use a full charge when left to stream indefinitely. |
| 3.1 | D | User judgement of significant packet loss when increasing the distance from camera device to streaming device. |
| 3.2 | D | TBA |
| 4 | D | Measure the maximum dimensions of the prototype |
| 5.1 | U | A yes/no judgement of a user who teaches anatomy (or a similar subjects) on whether or not they would "use the device". |
| 5.2 | D | Measure the time taken from switching on the device to streaming |
| 5.3 | D | Test the stream on a number of different devices and OS (e.g. windows desktop, apple tablet etc.) |
| 6.1 | D | The number of steps of how to construct the device, dictated by an independent user being able to construct the device |
| 6.2 | U | Provide a set of instructions to an independent individual and measure how long it takes them to construct the device |
| 7.1-5 | U | A yes/no judgement from the user on whether veins can be clearly seen. Minimum sample size n=10 for each use case (dark complexion, high BMI, thick hair or tattoos covering veins) |
| 7.6 | U | Similar to above |

## Results Table Template
As prototypes are tested the results will be updated here. Raw data can be found [here](https://docs.google.com/spreadsheets/d/18sSy89GIRTKhPBCF92-t4Pr2AGmHzw_IFHvKGeLFWAo/edit?usp=sharing).

| ID | Specification | Metric | Benchmark | Result |
| --- | --- | --- | --- | --- |
| 1 | Total Cost | $ | <250 | |
| 2.1 | Camera Focal Length | mm | 300-500 | |
| 2.2 | Adjustable Set Height | mm | 300-500 | |
| 2.3 | Handsfree Operation | min | >5 | |
| 2.4 | Battery Life | min | >60 | |
| 3.1 | Wireless Range | m | >1 | |
| 3.2 | Stream Delay | ms | <1000 | |
| 4 | Form Factor | mm | <150 x 90 x 70 | |
| 5.1 | User Acceptance | % | >90 | |
| 5.2 | Boot Time | s | <15 | |
| 5.3 | OS Compatibility | # | >2 | |
| 6.1 | Construction Steps | # | <5 | |
| 6.2 | Construction Time | hrs | <2 | |
| 7.1 | Automatic Contrast Adjustment (for ideal scenario) | % | >90 | |
| 7.2 | Automatic Contrast Adjustment (for any complexion) | % | 80 | |
| 7.3 | Automatic Contrast Adjustment (for high BMI/obesity) | % | 80 | |
| 7.4 | Automatic Contrast Adjustment (for any amount of hair) | % | 80 | |
| 7.5 | Automatic Contrast Adjustment (for tattooed area) | % | 80 | |
| 7.6 | Visualise Vascular Blood Flow | % | 80 | |

## Change Log
| Date | Change | Justification |
| --- | --- | --- |
| 29/9/18 | Changes made in-line with requirements changes | Verification reflects requirements/specifications. |
| 29/9/18 | Added device/user testing specification. | Need to differentiate between what can be tested with/without ethics approval. Device testing will not require ethics approval while user testing would. |
