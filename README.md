# LLM-MCP Car Detection Pipeline

## Overview
This application uses an LLM to parse a natural language mission, uses MCP to coordinate services (Image DB + YOLO), and returns images with detected vehicles (cars, buses, trucks, motorbikes) within a given time range.


For this prompt: "detect all buses and cars in images between 11:00 and 11:05"
and using the 3 images uploaded in this directory: "image1.jpg", "image2.jpg", "image3.jpg"
we got this result:

![image](https://github.com/user-attachments/assets/8719eb02-ecd6-4e09-880a-7bccc559450c)

## Bonus - NIM Detection Integration
To use a prebuilt NIM detection service:
- Replace `yolo_service.py` with a client calling the NIM detection API.
- No local model inference needed.
- MCP orchestrator stays mostly the same, but calls `nim_service.detect()` instead.

