from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "weed_harvester weed_timelord_launcher weed_timelord weed_farmer weed_full_node weed_wallet".split(),
    "node": "weed_full_node".split(),
    "harvester": "weed_harvester".split(),
    "farmer": "weed_harvester weed_farmer weed_full_node weed_wallet".split(),
    "farmer-no-wallet": "weed_harvester weed_farmer weed_full_node".split(),
    "farmer-only": "weed_farmer".split(),
    "timelord": "weed_timelord_launcher weed_timelord weed_full_node".split(),
    "timelord-only": "weed_timelord".split(),
    "timelord-launcher-only": "weed_timelord_launcher".split(),
    "wallet": "weed_wallet weed_full_node".split(),
    "wallet-only": "weed_wallet".split(),
    "introducer": "weed_introducer".split(),
    "simulator": "weed_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
