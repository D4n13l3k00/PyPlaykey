import time
from rich.console import Console
import os
from api import API, run_client
from config import Config

__version__ = "1.0.0b"

c = Console()


def main():
    cfg = Config().read()
    if not cfg:
        c.print("[yellow b]Конфиг не найден! Создаём новый...[/]")
    if not cfg or not cfg["Playkey"]["token"]:
        c.print(
            "[yellow b]Не указан Playkey Token в конфиге! Пожалуйста укажите его[/]"
        )
        return
    api = API(cfg["Playkey"]["token"])
    c.print("[green b]Playkey Launcher by D4n13l3k00[/]")
    c.print("[cyan b]Версия:[/] [yellow]v{}[/]".format(__version__))
    platforms = {
        "nt": "Windows",
        "posix": "Linux",
        "darwin": "MacOS",
    }
    c.print("[cyan b]ОС:[/] [yellow]{}[/]".format(platforms[os.name]))
    if os.name == "darwin":
        c.print("[cyan b]MacOS не поддерживается! У него есть официальный клиент[/]")
        return

    with c.status("[green b]Получаем информацию об аккаунте...[/]"):
        account = api.getAccountInfo()
        if account.error.code != 0:
            c.print("[red b]Ошибка:[/] [yellow]{}[/]".format(account.error.message))
            return
    c.print("\n[green b]➤ Аккаунт:[/]")
    c.print("[cyan b]Email:[/] [yellow]{}[/]".format(account.email))
    c.print("[cyan b]ID:[/] [yellow]{}[/]\n".format(account.id))

    # Получаем список категорий
    with c.status("[green b]Получаем список категорий...[/]"):
        categories = api.getCategories()
        if categories.error.code != 0:
            c.print("[red b]Ошибка:[/] [yellow]{}[/]".format(account.error.message))
            return
    while True:
        for i, category in enumerate(categories.categories, 1):
            c.print(
                "[white b][{}][/] [cyan b]{}[/]".format(i, category.name, category.code)
            )
        chosed_category = c.input("\n[green b]Выберите категорию:[/] ")
        if chosed_category == "dbg":
            with c.screen():
                c.print(account, "\n")
                c.print(categories, "\n")
                c.input()
            continue
        elif (
            not chosed_category
            or not chosed_category.isdigit()
            or int(chosed_category) > len(categories.categories)
        ):
            c.print("[red b]Не указана категория![/]")
            c.input()
            continue
        chosed_category = int(chosed_category) - 1
        break

    # Получаем категорию с её играми
    with c.status("[green b]Получаем информацию об категории...[/]"):
        games = api.getGamesByCategory(categories.categories[chosed_category].code)
        if games.error.code != 0:
            c.print("[red b]Ошибка:[/] [yellow]{}[/]".format(game.error.message))
            return

    while True:
        for i, game in enumerate(games.game_shipments_any, 1):
            c.print("[white b][{}][/] [cyan b]{}[/]".format(i, game.title, game.code))
        chosed_game = c.input("\n[green b]Выберите игру:[/] ")
        if chosed_game == "dbg":
            with c.screen():
                c.print(account, "\n")
                c.print(categories, "\n")
                c.print(games, "\n")
                c.input()
            continue
        elif (
            not chosed_game
            or not chosed_game.isdigit()
            or int(chosed_game) > len(games.game_shipments_any)
        ):
            c.print("[red b]Не указана игра![/]")
            c.input()
            continue
        chosed_game = int(chosed_game) - 1
        break

    with c.status("[green b]Получаем информацию об игре...[/]"):
        game = api.getFullGame(games.game_shipments_any[chosed_game].code)
        if game.error.code != 0:
            c.print("[red b]Ошибка:[/] [yellow]{}[/]".format(game.error.message))
            return
        game = game.game_shipments_any[0]

    c.print("[green b]Название:[/] [yellow]{}[/]".format(game.title))
    c.print(
        "[green b]Категории:[/] [yellow]{}[/]".format(
            ", ".join(i.name for i in game.categories)
        )
    )
    c.print(
        "[green b]Жанры:[/] [yellow]{}[/]".format(
            ", ".join(i.name for i in game.genres)
        )
    )
    c.print("[green b]Год выхода:[/] [yellow]{}[/]".format(game.year))
    val_from_res = lambda x, y: next(
        filter(lambda x: x.parameter == y, res.parameters)
    ).value
    run_codes = []
    if game.child_games:
        for subgame in game.child_games:
            for res in subgame.run:
                width = val_from_res(res.parameters, "WIDTH")
                height = val_from_res(res.parameters, "HEIGHT")
                fps = val_from_res(res.parameters, "FPS")
                # nmin_bitrate = val_from_res(res.parameters, "NMIN_BITRATE")
                run_codes.append(
                    (
                        f"{subgame.game_platform.name} | {width}x{height}_{fps}FPS",
                        subgame.code,
                        res.code,
                    )
                )

    else:
        for res in game.run:
            width = val_from_res(res.parameters, "WIDTH")
            height = val_from_res(res.parameters, "HEIGHT")
            fps = val_from_res(res.parameters, "FPS")
            # nmin_bitrate = val_from_res(res.parameters, "NMIN_BITRATE")
            run_codes.append(
                (
                    f"{width}x{height}_{fps}FPS",
                    game.code,
                    res.code,
                )
            )
    for i, (text, _, _) in enumerate(run_codes, 1):
        c.print(
            "[white b][{}][/] [cyan b]{}[/]".format(i, text),
        )
    while True:
        chosed_res = c.input("\n[green b]Выберите разрешение/платформу:[/] ")
        if chosed_res == "dbg":
            with c.screen():
                c.print(account, "\n")
                c.print(categories, "\n")
                c.print(games, "\n")
                c.print(run_codes, "\n")
                c.input()
            continue
        if (
            not chosed_res
            or not chosed_res.isdigit()
            or int(chosed_res) > len(run_codes)
        ):
            c.print("[red b]Некорректный выбор![/]")
            c.input()
            continue
        break
    chosed_res = run_codes[int(chosed_res) - 1]
    run_url = api.getRunUrl(chosed_res[1], chosed_res[2])
    run_client(run_url.play_url)


if __name__ == "__main__":
    main()
