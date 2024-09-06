#  Steganographic Images

This project aims to detect and extract hidden messages embedded within steganographic images using various steganalytic forensic techniques. The primary focus is on LSB (Least Significant Bit) and group-parity steganography. Additionally, the project incorporates Huffman Coding and Run-Length Encoding (RLE) for compressing the hidden messages before embedding them in images.

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
  - [Steganography Techniques](#steganography-techniques)
  - [Payload Location](#payload-location)
- [Message Extraction](#message-extraction)
  - [LSB Steganography](#lsb-steganography)
  - [Group-parity Steganography](#group-parity-steganography)
- [Cover Estimation](#cover-estimation)
- [Algorithms](#algorithms)
  - [Least Significant Bit (LSB) Steganography](#least-significant-bit-lsb-steganography)
  - [Huffman Coding](#huffman-coding)
  - [Run-Length Encoding (RLE)](#run-length-encoding-rle)
- [Experimental Results](#experimental-results)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Steganography is the practice of concealing messages within digital images. This project explores techniques to identify and extract these hidden messages, focusing on the residual differences between original (cover) and modified (stego) images. The project also demonstrates the use of Huffman Coding and Run-Length Encoding (RLE) for compressing the text before embedding it into images, providing a compact and secure way to hide messages.

## Background
Steganography, derived from the Greek words "steganos" (covered) and "graphia" (writing), has been used for covert communication for centuries. In the digital age, steganography involves hiding data within digital media such as images, audio, and video files. This project focuses on digital image steganography, specifically using the Least Significant Bit (LSB) method and group-parity techniques to hide and extract hidden messages.

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

## Algorithms

### Least Significant Bit (LSB) Steganography
**Description**: The LSB technique hides information by modifying the least significant bits of the pixel values in an image. These small changes are imperceptible to the human eye, making it a popular method for steganography.

**Steps**:
1. Convert the message to its binary representation.
2. Flatten the image into a 1D array of pixel values.
3. For each bit of the message, replace the least significant bit of the current pixel with the message bit.
4. Continue this process until the entire message is hidden.
5. Save the modified image.

### Huffman Coding
**Description**: Huffman Coding is a lossless data compression algorithm. It assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

**Steps**:
1. Calculate the frequency of each character in the text.
2. Build a binary tree (Huffman Tree) based on these frequencies.
3. Assign binary codes to each character by traversing the tree.
4. Replace each character in the text with its corresponding binary code to get the encoded message.
5. To decode, reverse the process using the Huffman Tree.

### Run-Length Encoding (RLE)
**Description**: RLE is a simple form of lossless data compression where sequences of the same data value (runs) are stored as a single data value and count.

**Steps**:
1. Traverse the text and count consecutive occurrences of each character.
2. Replace each sequence with the character followed by the count.
3. To decompress, repeat each character according to its count.

## Experimental Results
- Validates the proposed techniques through experiments.
- Demonstrates the effectiveness of the methods in logically ordering and extracting hidden messages.

## Conclusion
This project successfully demonstrates the implementation of image steganography using the LSB technique, combined with Huffman Coding and RLE for data compression. While LSB steganography is effective for embedding large messages with minimal impact on image quality, its vulnerability to simple attacks and image modifications emphasizes the need for secure environments when using this technique.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rathod-yuvraj/steganography-message-extraction.git
   cd steganography-message-extraction
