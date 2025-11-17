# Eming_GIF_Display  
**Raspberry Pi 3 Animated GIF Display**

## Project Overview  
Eming_GIF_Display is a lightweight GIF-rendering system running on a **Raspberry Pi 3**, designed for cosplay props, small displays, and interactive installations. The project loads and plays animated GIFs smoothly using Python, a connected display module, and simple GPIO controls.  

The goal is to embed animated visuals into wearable electronics or props while keeping the system easy to configure and modify.

---

## Features  
- Plays animated GIFs on a connected display (SPI/I2C/TFT depending on setup).  
- Python-based playback loop optimized for Raspberry Pi hardware.  
- Pushbutton input to switch between different GIF animations.  
- Works with custom or preloaded GIF assets.  
- Easily integratable into props, costume pieces, or small enclosures.

---

## Hardware  
- **Raspberry Pi 3 Model B**  
- Small TFT/OLED display (SPI recommended for speed)  
- Momentary pushbutton (wired to GPIO for mode switching)  
- Optional: custom 3D-printed housing (Fusion 360)

---

## Software  
- Python 3  
- `Pillow` for GIF decoding  
- GPIO library (e.g., `RPi.GPIO` or `gpiozero`)  
- Frame-timing logic for smooth animated playback  
- Folder-based GIF management system (swap GIFs easily)

---

## Setup Instructions  

### 1. Clone the Repository  
```bash
git clone https://github.com/asibarra/Eming_GIF_Display.git
cd Eming_GIF_Display
