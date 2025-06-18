## Introduction
Soft grippers are typically made of silicone and are expensive to manufacture. In this project, our team designed and implemented soft grippers for vegetable harvesting at a cost of **less than $130 (100,000 KRW).**

## Literature review

<figure>
  <img width="600" alt="mit_0" src="https://github.com/user-attachments/assets/060cbc35-b87d-46e3-b8e0-a409cf41780e" />
  <figcaption></figcaption>
</figure>

[A Vacuum-driven Origami “Magic-ball” Soft Gripper](https://dspace.mit.edu/handle/1721.1/120930)

<img width="600" alt="mit_1" src="https://github.com/user-attachments/assets/6cc9777f-af55-46dd-a630-2ef7609fb9f5" />
<img width="600" alt="mit_2" src="https://github.com/user-attachments/assets/d717cf41-d2bd-4dbb-9f2d-61a9c957e522" />

Our team reviewed lots of papers, including those on grippers using shape memory sponges, but we needed to find a cost-effective solution.
Inspired by a vacuum-driven origami ‘magic-ball’ soft gripper, we came up with the idea of implementing a gripper **by folding real paper.**

## Implementation process
<img width="600" alt="shape" src="https://github.com/user-attachments/assets/e2267aa5-9076-46b8-b4bd-2589e8901f91" />

Origami has actually been practiced using various types of paper.

<img width="600" alt="idea" src="https://github.com/user-attachments/assets/a57a5566-47ae-4dd2-9a08-c092f262e7a0" />

Initially, we considered using balloons to replace the silicone part, but since the balloons burst quickly, we looked for another material, **fishing line.**

### Detailed structural analysis
<img width="600" alt="final_shape_0" src="https://github.com/user-attachments/assets/8596628b-0646-464e-a093-2156af1b1764" />

<img width="600" alt="final_shape_1" src="https://github.com/user-attachments/assets/e4231bf6-8986-4e52-b293-765424db1abd" />

The structure is designed so that pulling a fishing line through a small hole in the paper produces the same force as applied through the holes on the other side.

## Analyze gripper performance

### Oriental melon
<img width="600" alt="melon" src="https://github.com/user-attachments/assets/e6e85111-6e3b-4132-9c70-088534f7a468" />

Success

### Potato
<img width="600" alt="potato" src="https://github.com/user-attachments/assets/483c9c56-4c8a-4ec8-9202-dde7f5b4fa2a" />

Success

### Blueberry
<img width="600" alt="blueberry" src="https://github.com/user-attachments/assets/d94dea60-4877-4d6e-a1fa-4ddd8f568afc" />

Fail

### Egg
<img width="600" alt="egg" src="https://github.com/user-attachments/assets/9848df50-67a7-4d3d-8e79-e61b47ce5f16" />

Success

### Banana
<img width="600" alt="banana" src="https://github.com/user-attachments/assets/89a9604b-73f1-474e-982b-5724f60be986" />

Attempt 1: Fail / Attempt 2: Success

### A paper cup filled with water
<img width="600" alt="cup" src="https://github.com/user-attachments/assets/b1e7f64a-e958-4c32-be06-823981bab0f1" />

Success

https://github.com/user-attachments/assets/f6dce16f-ea30-49ea-9890-a1c62b69019a

In order to respect portrait rights, I'm sharing a partial version of the demo video.  

## Gripper Software
<img width="600" alt="qt" src="https://github.com/user-attachments/assets/159138eb-4f6d-488c-b79d-3d62dc182d2c" />

Implemented to run without significant GUI changes in various environments.

<br/>
<img width="600" alt="class_diagram" src="https://github.com/user-attachments/assets/ecf1b22f-bfcd-4f21-93de-3068764df13d" />

Class diagram is as above.

## Additional info
<img width="600" alt="hardware" src="https://github.com/user-attachments/assets/fce43304-8238-409d-954b-57baa3390553" />

Hardware information is as above.
