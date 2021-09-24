from setuptools import setup

dependencies = [
    "blspy==1.0.5",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the weed processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="weed-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@weed.net",
    description="Weed blockchain full node, farmer, timelord, and wallet.",
    url="https://weed.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="weed blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "weed",
        "weed.cmds",
        "weed.clvm",
        "weed.consensus",
        "weed.daemon",
        "weed.full_node",
        "weed.timelord",
        "weed.farmer",
        "weed.harvester",
        "weed.introducer",
        "weed.plotting",
        "weed.pools",
        "weed.protocols",
        "weed.rpc",
        "weed.server",
        "weed.simulator",
        "weed.types.blockchain_format",
        "weed.types",
        "weed.util",
        "weed.wallet",
        "weed.wallet.puzzles",
        "weed.wallet.rl_wallet",
        "weed.wallet.cc_wallet",
        "weed.wallet.did_wallet",
        "weed.wallet.settings",
        "weed.wallet.trading",
        "weed.wallet.util",
        "weed.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "weed = weed.cmds.weed:main",
            "weed_wallet = weed.server.start_wallet:main",
            "weed_full_node = weed.server.start_full_node:main",
            "weed_harvester = weed.server.start_harvester:main",
            "weed_farmer = weed.server.start_farmer:main",
            "weed_introducer = weed.server.start_introducer:main",
            "weed_timelord = weed.server.start_timelord:main",
            "weed_timelord_launcher = weed.timelord.timelord_launcher:main",
            "weed_full_node_simulator = weed.simulator.start_simulator:main",
        ]
    },
    package_data={
        "weed": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp"],
        "weed.util": ["initial-*.yaml", "english.txt"],
        "weed.ssl": ["weed_ca.crt", "weed_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
