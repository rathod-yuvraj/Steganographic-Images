# Extracting-Hidden-Messages-in-Steganographic-Images
# Extracting Hidden Messages in Steganographic Images

This project aims to detect and extract hidden messages embedded within steganographic images using various steganalytic forensic techniques. The primary focus is on LSB (Least Significant Bit) and group-parity steganography.

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
  - [Steganography Techniques](#steganography-techniques)
  - [Payload Location](#payload-location)
- [Message Extraction](#message-extraction)
  - [LSB Steganography](#lsb-steganography)
  - [Group-parity Steganography](#group-parity-steganography)
- [Cover Estimation](#cover-estimation)
- [Experimental Results](#experimental-results)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Steganography is the practice of concealing messages within digital images. This project explores techniques to identify and extract these hidden messages, focusing on the residual differences between original (cover) and modified (stego) images.

## Background
### Steganography Techniques
- **LSB Steganography:** Embeds message bits into the least significant bits of pixel values, making changes difficult to detect.
- **Group-parity Steganography:** Embeds message bits based on the parity of groups of pixel values.

### Payload Location
- Detects modified pixels by analyzing the residuals (differences between cover and stego images).
- Utilizes these residuals to locate the message bits without requiring the embedding key.

## Message Extraction
### LSB Steganography
- Calculates mean residuals of pixels to order and extract hidden message bits.
- Uses the residual values to determine the logical sequence of the embedded message.

### Group-parity Steganography
- Applies similar principles to groups of pixels.
- Orders payload bits based on descending mean residual values.

## Cover Estimation
When the original cover image is unavailable, a cover estimation approach is used:
- Utilizes Markov Random Fields (MRF) to reconstruct the cover image from the stego image.
- Computes residuals from the estimated cover image to locate and extract the hidden message.

## Experimental Results
- Validates the proposed techniques through experiments.
- Demonstrates the effectiveness of the methods in logically ordering and extracting hidden messages.

## Conclusion
The project reveals that mean residuals can be used to logically order and extract hidden messages in stego images, highlighting a vulnerability in current steganographic methods.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/steganography-message-extraction.git
   cd steganography-message-extraction
