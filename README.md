# Crypto Benchmarking Tool

## Description
This project is designed to benchmark the performance of various cryptographic algorithms, including AES, Blowfish, ChaCha20, and Camellia. It measures the CPU and memory usage during the encryption and decryption processes for different file types and sizes, ranging from text files to multimedia content.

## Features
- Supports multiple cryptographic algorithms with varying key sizes.
- Capable of processing a wide range of file sizes and types.
- Outputs performance metrics such as CPU usage and memory consumption.
- Results are saved in an Excel file for easy analysis.

## Installation
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Usage
To run the benchmarking, execute the `main.py` script. This script will perform encryption and decryption on predefined files with the specified algorithms and key sizes. The results will be stored in an Excel file.

### Running the main application
```bash
python main.py
```

The benchmarking results will be appended to an Excel file named `results.xlsx`, with details such as file path, size, algorithm used, and resource usage.

## Data
### System Settings
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/97618b18-cb29-4d2f-a221-64c4630dec4a">

### AES
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/38882e34-6e98-4c12-bec9-adba402abea3">

### Blowfish
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/00713fd2-fc6b-4481-ab9b-edf3258ade77">

### ChaCha20
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/9ce111e4-55df-4d10-895f-f7832a79735e">

### Camellia
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/eff27288-6361-45a8-8cc9-8cd3ad9f87aa">

### Graphs
<img width="364" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/842d84ef-2a8d-40ed-9334-ae667098f421">
<img width="367" alt="image" src="https://github.com/brendankariniemi/CryptographicAlgoComparison/assets/138073658/387e0224-42a7-4d67-ac38-e5c9badfb345">

