import utils.helper as helper
import utils.setup as setup


class LogInLogOut:

    def __init__(self):
        self.correct_email = helper.get_random_email()
        self.incorrect_email = helper.get_random_string()
        self.user = None

    def login_correct_email(self):
        try:
            self.user = setup.User()
            self.user.login_view.login(driver=self.user.chrome_driver, email=self.correct_email, success=True)
            helper.logout(driver=self.user.chrome_driver)
            self.user.teardown()
            return True
        except Exception as e:
            self.user.teardown()
            raise Exception(f"Login with correct email test failed: {e}")


if __name__ == "__main__":
    test = LogInLogOut()
    test.login_correct_email()
