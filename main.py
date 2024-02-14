class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents
        # TODO: add code to parse weight and parents fields

    def __str__(self):
      return f"{self.txid}\n"

    def parse_mempool_csv(self):
        """Parse the CSV file and return a list of MempoolTransactions."""
        with open('mempool.csv') as f:
          return [MempoolTransaction(*line.strip().split(',')) for line in f.readlines()]

    def write_output_file(self, output_file):
      transactions = self.parse_mempool_csv()

      with open(output_file, 'w') as block_data_file:
        for transaction in transactions:
          # If parents are present, add them before the current transaction ID
          if transaction.parents:
            parent_txids = transaction.parents.split(',')
            for parent_txid in parent_txids:
                parent_tx = next((tx for tx in transactions if tx.txid == parent_txid), None)
                if parent_tx:
                    block_data_file.write(str(parent_tx))
            block_data_file.write(str(transaction))
          else:
            block_data_file.write(str(transaction))


mempool_tx = MempoolTransaction(
  '79c51c9d4124c5cbb37a85263748dcf44e182dff83561fa3087f0e9e43f41c33', 
  682, 
  1136, 
  '6eb38fad135e38a93cb47a15a5f953cbc0563fd84bf1abdec578c2af302e10bf'
)

output_file = 'block_data.txt'
mempool_tx.write_output_file(output_file)

# print(mempool_tx.parse_mempool_csv()[0])