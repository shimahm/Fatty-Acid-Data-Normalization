# Fatty-Acid-Data-Normalization

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/pandas-1.0%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple Python script for normalizing fatty acid concentration data to percentage of total.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Format](#input-format)
- [Output](#output)
- [Customization](#customization)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description
This script processes Excel files containing fatty acid measurements, normalizing each fatty acid value to a percentage of the total sum. This is particularly useful for comparing relative abundances across samples.

## Features
- Processes common fatty acids from C14 to C24
- Preserves original data structure
- Simple configuration
- Fast processing with pandas
- Excel input/output support

## Requirements
- Python 3.7+
- pandas
- openpyxl

## Installation
```bash
pip install pandas openpyxl
