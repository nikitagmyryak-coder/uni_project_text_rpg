from entities import player
import functools

def log_action(func):
    @functools.wraps(func) # saves original func name
    def wrapper(*args, **kwargs):
        player = args[0]

        action_name = func.__name__.replace('_', ' ').upper()

        print("\n" + "=" * 45)
        print(f" [ACTION] {player.name} -> {action_name}")
        print("=" * 45)

        result = func(*args, **kwargs)

        print("\n")
        return result

    return wrapper


def stat_change_alert(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\n--- STATUS UPDATE SUCCESSFUL ---")
        return result

    return wrapper