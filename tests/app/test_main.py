from src.app.main import get_user, deposit
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_Main:

    def test_get(self):
        repo = UserRepositoryMock()
        response = get_user()
        assert response == repo.get_user(1).to_dict()

    def test_post_deposit(self):
        transaction_repo = TransactionRepositoryMock()
        user_repo = UserRepositoryMock()

        response = deposit(request={"2": 1,
                                    "5": 2,
                                    "10": 0,
                                    "20": 0,
                                    "50": 5,
                                    "100": 0,
                                    "200": 0})

        total_expected_value = 1*2 + 2*5 + 0*10 + 0*20 + 5*50 + 0*100 + 0*200 + user_repo.get_user(1).current_balance

        assert total_expected_value == response.get("current_balance")
