from entities import player

def log_action(func):
    def wrapper(*args, **kwargs):
        # args[0] — это объект Player, так как декоратор применяется к его методам
        player = args[0]

        action_name = func.__name__.replace('_', ' ').upper()

        print("\n" + "=" * 45)
        print(f" [ACTION] {player.name} -> {action_name}")
        print("=" * 45)

        result = func(*args, **kwargs)

        print("." * 45 + "\n")
        return result

    return wrapper


def stat_change_alert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("--- STATUS UPDATE SUCCESSFUL ---")
        return result

    return wrapper