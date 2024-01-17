import pandas as pd


class StockTransactions:
    def __init__(self) -> None:
        self.details_dataframe = None

    def create_stock_dataframe(
            self,
            columns: list):
        '''
        This function creates dataframe
        that will store details of transactions.

        Arguments:
            columns -> list
        '''

        self.details_dataframe = pd.DataFrame(columns=columns)
        self.details_dataframe.set_index(columns[0], inplace=True)
        return self.details_dataframe

    def new_transaction(self,
                        order: str,
                        type: str,
                        price: float,
                        quantity: int):
        '''
        This function appends details of new transaction
        to DataFrame with transaction details, prints and returns it.

        Arguments:
            order -> str
            type -> str
            price -> float
            quantity -> int
        '''
        new_transaction_details = {'Order': order, 'Type': type,
                                   'Price': price, 'Quantity': quantity}
        self.details_dataframe = self.details_dataframe.append(
            new_transaction_details, ignore_index=True)

        return self.details_dataframe

    def display_details(self):
        '''
        This functions displays current state
        of dataframe with transactions details.
        '''
        print(self.details_dataframe)


# Create StockTransaction object
StockTransactionsDetailsObject = StockTransactions()

# Create DataFrame
StockTransactionsDetailsObject.create_stock_dataframe(['Id', 'Order', 'Type',
                                                       'Price', 'Quantity'])

# Add new transactions
StockTransactionsDetailsObject.new_transaction('Buy', 'Add', 20.0, 100)
StockTransactionsDetailsObject.new_transaction('Sell', 'Add', 25.0, 200)
StockTransactionsDetailsObject.new_transaction('Buy', 'Add', 23.0, 50)
StockTransactionsDetailsObject.new_transaction('Buy', 'Add', 23.0, 70)
StockTransactionsDetailsObject.new_transaction('Buy', 'Remove', 23.0, 50)
StockTransactionsDetailsObject.new_transaction('Sell', 'Add', 28, 100)

# Display details of transactions
StockTransactionsDetailsObject.display_details()
