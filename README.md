## Introduction
Soft grippers are typically made of silicone and are expensive to manufacture. In this project, our team designed and implemented soft grippers for vegetable harvesting at a cost of **less than $130 (100,000 KRW).**

## Literature review
<img width="810" height="466" alt="mit_0" src="https://github.com/user-attachments/assets/85eb05d8-b3df-43d1-9d2b-61c06928a3d1" />

[A Vacuum-driven Origami “Magic-ball” Soft Gripper](https://dspace.mit.edu/handle/1721.1/120930)

<img width="810" alt="mit_1" src="https://github.com/user-attachments/assets/c688b6f7-4eba-4b42-9977-a587b5ac754a" />
<img width="810" alt="mit_2" src="https://github.com/user-attachments/assets/a7bcf945-ae53-4b98-b5d2-82b4f0cb0a6e" />

[Origami Robot Gripper](https://www.youtube.com/watch?v=byqGFH6AZuk)

<br/>

Our team reviewed lots of papers, including those on grippers using shape memory sponges, but we needed to find a cost-effective solution.
Inspired by a vacuum-driven origami ‘magic-ball’ soft gripper, we came up with the idea of implementing a gripper **by folding real paper.**


## Implementation process

<img width="750" alt="shape" src="https://github.com/user-attachments/assets/e51194a8-078c-4711-b27d-cc7b949ba2a7" />

Origami has actually been practiced using various types of paper.

<img width="750" alt="idea" src="https://github.com/user-attachments/assets/04407902-7a68-49b5-9294-83b0a7bc58ae" />

Initially, we considered using balloons to replace the silicone part, but since the balloons burst
quickly, we looked for another material, **fishing line.**

### Detailed structural analysis

<img width="750" height="415" alt="final_shape_0" src="https://github.com/user-attachments/assets/a4d9c412-7ff4-4d9b-99bf-3cf667393d69" />
<img width="750" height="415" alt="final_shape_1" src="https://github.com/user-attachments/assets/8ceb95aa-aa81-478f-93b1-4e89bb66fc18" />

The structure is designed so that pulling a fishing line through a small hole in the paper produces
the same force as applied through the holes on the other side.

## Analyze gripper performance

### Oriental melon
<img width="540" alt="melon" src="https://github.com/user-attachments/assets/b6acc67b-e373-44ba-8f1b-92a6d94f2186" />

Success

### Potato
<img width="540" alt="potato" src="https://github.com/user-attachments/assets/238cf439-8bd8-4581-8df3-c5addef1bc83" />

Success

### Blueberry
<img width="540" alt="blueberry" src="https://github.com/user-attachments/assets/bd1eab30-5e62-4f3c-8ac7-9abc797c7b2b" />

Fail

### Egg
<img width="540" alt="egg" src="https://github.com/user-attachments/assets/f14ebc9e-c2fd-49a3-a148-1c84af1ca4b0" />


Success

### Banana
<img width="540" alt="banana" src="https://github.com/user-attachments/assets/0d2a4b8c-ab55-4721-a160-1eb220c06925" />

Attempt 1: Fail / Attempt 2: Success

### A paper cup filled with water
<img width="540" alt="cup" src="https://github.com/user-attachments/assets/3e133d04-2915-4d42-82d9-981c286a2deb" />

Success

https://github.com/user-attachments/assets/60b9a3cd-7fc3-4989-a64e-6834bc627b8f

In order to respect portrait rights, I'm sharing a partial version of the demo video.  

## Gripper Software

<img width="550" alt="qt" src="https://github.com/user-attachments/assets/a64fc0a6-df15-494c-98c7-6e96e2f58cda" />

Implemented to run without significant GUI changes in various environments.

<br/>

<img width="550" alt="class_diagram" src="https://github.com/user-attachments/assets/6ea02f4b-4819-42cb-adef-11648157705d" />

Class diagram is as above.

## Additional info

<img width="810" alt="hardware" src="https://github.com/user-attachments/assets/f14c181b-382f-4a0e-83e6-eb7f2c5d8e12" />

Hardware information is as above.
