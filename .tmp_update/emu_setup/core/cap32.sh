#!/bin/sh

EMU_DIR="$(dirname "$0")"
CONFIG="$EMU_DIR/config.json"
SYS_OPT="$EMU_DIR/system.opt"

update_core_config_name() {
    if [ -f "$CONFIG" ]; then
        sed -i 's|"name": "✓ Core is cap32"|"name": "Change core to cap32"|g' "$CONFIG"
        sed -i 's|"name": "✓ Core is crocods"|"name": "Change core to crocods"|g' "$CONFIG"
        sed -i 's|"name": "Change core to cap32"|"name": "✓ Core is cap32"|g' "$CONFIG"
    fi
}

update_core_config_name

sed -i 's/CORE=.*/CORE=\"cap32\"/g' "$SYS_OPT"
