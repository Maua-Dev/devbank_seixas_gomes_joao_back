from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .enums.transaction_type_enum import TransactionTypeEnum

from .entities.transaction import Transaction

app = FastAPI()

in_use_id = 1

user_repo = Environments.get_user_repo()
transaction_repo = Environments.get_transaction_repo()

@app.get("/")
def get_user():

    user = user_repo.get_user(user_id=in_use_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user.to_dict()

@app.get("/history")
def get_history():

    transactions = transaction_repo.get_all_transactions()

    transaction_dict = {"transactions": []}

    for transaction in transactions:

        transaction_dict["transactions"].append(transaction.to_dict())

    return transactions


handler = Mangum(app, lifespan="off")
