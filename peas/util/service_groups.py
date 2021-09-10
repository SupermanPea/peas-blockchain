from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "peas_harvester peas_timelord_launcher peas_timelord peas_farmer peas_full_node peas_wallet".split(),
    "node": "peas_full_node".split(),
    "harvester": "peas_harvester".split(),
    "farmer": "peas_harvester peas_farmer peas_full_node peas_wallet".split(),
    "farmer-no-wallet": "peas_harvester peas_farmer peas_full_node".split(),
    "farmer-only": "peas_farmer".split(),
    "timelord": "peas_timelord_launcher peas_timelord peas_full_node".split(),
    "timelord-only": "peas_timelord".split(),
    "timelord-launcher-only": "peas_timelord_launcher".split(),
    "wallet": "peas_wallet peas_full_node".split(),
    "wallet-only": "peas_wallet".split(),
    "introducer": "peas_introducer".split(),
    "simulator": "peas_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
