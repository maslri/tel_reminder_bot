from constant import START_HALEP


def get_started_test(user_first_name, user_last_name):
    return (f"Hello dear {user_first_name} {user_last_name}! "
            f"Welcome to the WMT bot. "
            f"You can use the following commands:\n{START_HALEP}")
