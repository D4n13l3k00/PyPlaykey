from __future__ import annotations

import os
import subprocess
from typing import *

import requests
from pydantic import BaseModel


def run_client(url: str):
    if os.name == "nt":
        subprocess.call(["client/Playkey.exe", url])
    elif os.name == "posix":
        subprocess.call(["wine", "client/Playkey.exe", url])


class Error(BaseModel):
    code: int
    message: str


class Category(BaseModel):
    code: str
    name: str
    type: str
    metadata: Any


class CategoriesModel(BaseModel):
    error: Error
    categories: List[Category]


class KohortParameter(BaseModel):
    name: str
    value: str


class Kohort(BaseModel):
    kohort_code: str
    kohort_type_code: str
    kohort_parameters: List[KohortParameter]


class ExternalGamePlatforms(BaseModel):
    Steam: str


class AccountInfoModel(BaseModel):
    error: Error
    email: str
    login: str
    id: int
    is_confirmed: bool
    region_code: str
    is_anonymous: bool
    kohorts: List[Kohort]
    is_active_referral: bool
    partners: List
    external_game_platforms: ExternalGamePlatforms


class GameShipmentsAnyItem(BaseModel):
    title: str
    cover: str
    category_codes: List[str]
    preview: Optional[str] = None
    code: str
    status: str
    platforms: List[str]


class GamesFromCategoryModel(BaseModel):
    error: Error
    game_shipments_any: List[GameShipmentsAnyItem]


class Error(BaseModel):
    code: int
    message: str


class ContentItem(BaseModel):
    type: str
    links: List[str]


class Genre(BaseModel):
    code: str
    name: str
    is_main: bool
    metadata: Any


class Product(BaseModel):
    code: str
    name: str


class InputDevice(BaseModel):
    code: str
    name: str


class Category(BaseModel):
    code: str
    name: str
    type: Any
    metadata: Any


class Parameter(BaseModel):
    parameter: str
    value: str


class RunItem(BaseModel):
    name: str
    code: str
    priority: int
    parameters: List[Parameter]


class GamePlatform(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: Optional[str]
    icon20: Optional[str]
    text: Optional[str]


class GamePlatform1(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: Optional[str]
    icon20: Optional[str]
    text: Optional[str]


class Parameter1(BaseModel):
    parameter: str
    value: str


class RunItem1(BaseModel):
    name: str
    code: str
    priority: int
    parameters: List[Parameter1]


class GamePlatform2(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: Optional[str]
    icon20: Optional[str]
    iconGray40: Optional[str]
    text: Optional[str]


class GamePlatform3(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: Optional[str]
    icon20: Optional[str]
    iconGray40: Optional[str]
    text: Optional[str]


class CardInfo(BaseModel):
    game_card_type: str
    has_play_attempt: bool


class ChildGame(BaseModel):
    code: str
    game_status_code: str
    run: List[RunItem1]
    game_platforms: List[GamePlatform2]
    game_platform: GamePlatform3
    platform_code: str
    card_info: CardInfo


class Parameter2(BaseModel):
    parameter: str
    value: str


class RunItem2(BaseModel):
    name: str
    code: str
    priority: int
    parameters: List[Parameter2]


class GamePlatform4(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: Optional[str]
    icon20: Optional[str]
    iconGray40: Optional[str] = None
    text: Optional[str]


class GamePlatform5(BaseModel):
    code: str
    name: str
    link: Optional[str]
    img: Optional[str]
    badge: Optional[str]
    circle: Optional[str]
    icon68: Optional[str]
    iconNewCatalog: str
    icon20: Optional[str]
    iconGray40: Optional[str] = None
    text: Optional[str]


class CardInfo1(BaseModel):
    game_card_type: str
    has_play_attempt: bool


class ChildGame1(BaseModel):
    code: str
    game_status_code: str
    run: List[RunItem2]
    game_platforms: List[GamePlatform4]
    game_platform: GamePlatform5
    platform_code: str
    card_info: Optional[CardInfo1]


class CardInfo2(BaseModel):
    game_card_type: str
    has_play_attempt: bool


class GameFullShipmentsAnyItem(BaseModel):
    code: str
    title: str
    description: str
    year: int
    plot_outline: Optional[str]
    tag_line: Optional[Any]
    writer: Optional[str]
    premiered: Optional[str]
    top250: Optional[Any]
    rating: Optional[int]
    votes: Optional[Any]
    mpaa: Optional[str]
    demo_time: Optional[int]
    rightholder: Optional[str]
    content: Optional[List[ContentItem]]
    genres: Optional[List[Genre]]
    products: Optional[List[Product]]
    count_players: Optional[int]
    input_devices: Optional[List[InputDevice]]
    categories: Optional[List[Category]]
    metadata: Optional[Any]
    buy: Optional[List]
    run: Optional[List[RunItem]]
    game_platforms: Optional[List[GamePlatform]]
    game_platform: Optional[GamePlatform1]
    platform_code: Optional[str]
    game_status: Optional[str]
    child_game: Optional[Optional[ChildGame]]
    child_games: Optional[List[ChildGame1]]
    available_in_regions: Optional[List[str]]
    game_shipment_any_type: Optional[str]
    is_dlc_available_without_game: Optional[Any]
    main_game_code: Optional[str]
    main_game_title: Optional[str]
    bundles: Optional[List]
    card_info: Optional[CardInfo2]


class FullGameModel(BaseModel):
    error: Error
    game_shipments_any: List[GameFullShipmentsAnyItem]


class GetRunURLModel(BaseModel):
    error: Error
    key: str
    active_to: str
    play_url: str


class RequestModel(BaseModel):
    lang: str = "ru"
    filter_name: Optional[str]
    filter_codes: Optional[List[str]]
    filter_categories_and_genres: Optional[List[str]]
    offset: Optional[int]
    limit: Optional[int]
    play_config: Optional[str]
    code_game: Optional[str]
    token: str
    ga_clientId: str


class API:
    def __init__(self, token: str) -> None:
        self.token = token

    def getAccountInfo(self) -> AccountInfoModel:
        rq = RequestModel(token=self.token, ga_clientId="ga don't initialize")
        return AccountInfoModel.parse_raw(
            requests.post(
                "https://api.playkey.net/rest/PlaykeyAPI.svc/user/info", json=rq.dict()
            ).text
        )

    def getCategories(self) -> CategoriesModel:
        rq = RequestModel(token=self.token, ga_clientId="no counters")
        return CategoriesModel.parse_raw(
            requests.post(
                "https://api.playkey.net/rest/PlaykeyAPI.svc/games/categories",
                json=rq.dict(),
            ).text
        )

    def getGamesByCategory(self, category: str) -> GamesFromCategoryModel:
        rq = RequestModel(
            token=self.token,
            filter_name="",
            ga_clientId="ga doesn't have clientId",
            filter_categories_and_genres=[category],
            offset=0,
            limit=1000,
        )
        return GamesFromCategoryModel.parse_raw(
            requests.post(
                "https://api.playkey.net/rest/PlaykeyAPI.svc/gameshipments/all/catalog-category/auth",
                json=rq.dict(),
            ).text
        )

    def getFullGame(self, game_code: str) -> FullGameModel:
        rq = RequestModel(
            token=self.token,
            filter_codes=[game_code],
            filter_name="",
            ga_clientId="ga doesn't have clientId",
            offset=0,
            limit=1000,
        )
        return FullGameModel.parse_raw(
            requests.post(
                "https://api.playkey.net/rest/PlaykeyAPI.svc/gameshipments/all/auth",
                json=rq.dict(),
            ).text
        )

    def getRunUrl(self, code: str, play_conf: str) -> GetRunURLModel:
        rq = RequestModel(
            token=self.token,
            code_game=code,
            play_config=play_conf,
            ga_clientId="ga doesn't have clientId",
            offset=0,
            limit=1000,
        )
        return GetRunURLModel.parse_raw(
            requests.post(
                "https://api.playkey.net/rest/PlaykeyAPI.svc/games/play", json=rq.dict()
            ).text
        )
