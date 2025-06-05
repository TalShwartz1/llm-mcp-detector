# LLM-MCP Car Detection Pipeline

## Overview
This application uses an LLM to parse a natural language mission, uses MCP to coordinate services (Image DB + YOLO), and returns images with detected vehicles (cars, buses, trucks, motorbikes) within a given time range.

## Bonus - NIM Detection Integration
To use a prebuilt NIM detection service:
- Replace `yolo_service.py` with a client calling the NIM detection API.
- No local model inference needed.
- MCP orchestrator stays mostly the same, but calls `nim_service.detect()` instead.

