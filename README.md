# Bitcoin Block Constructor

## Overview

The Mempool Transaction Parser is a Python script designed to parse mempool transaction data from a CSV file and organize it into a block format. This project aims to assist in block construction by providing a tool to manage mempool transactions efficiently.

## Features

- **CSV Parsing**: Parses transaction data from a CSV file.
- **Transaction Organization**: Organizes transactions into a block format, considering parent transactions if present.
- **Output File Generation**: Writes the organized transactions into an output file for further processing.

## Usage

### Requirements

- Python 3.x

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:isaack-njama/bitcoin-block-constructor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd bitcoin-block-constructor
   ```

### Running the Script

1. Ensure you have a CSV file named `mempool.csv` with transaction data in the following format:

   ```
   txid,fee,weight,parents
   tx1,1000,2000,tx2,tx3
   tx2,500,1000,
   ```

   - `txid`: Transaction ID
   - `fee`: Transaction fee
   - `weight`: Transaction weight
   - `parents`: Parent transactions (if any), comma-separated

2. Execute the script with the following command:

   ```bash
   python main.py
   ```

3. Check the generated output file named `block_data.txt` for the organized transactions.

## Example

```python
# Instantiate MempoolTransaction object
mempool_tx = MempoolTransaction(
  '79c51c9d4124c5cbb37a85263748dcf44e182dff83561fa3087f0e9e43f41c33', 
  682, 
  1136, 
  '6eb38fad135e38a93cb47a15a5f953cbc0563fd84bf1abdec578c2af302e10bf'
)

# Write output file
output_file = 'block_data.txt'
mempool_tx.write_output_file(output_file)
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or fixes.

## Contact

For any inquiries or feedback, please contact me at <isaacknjama@proton.me>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
