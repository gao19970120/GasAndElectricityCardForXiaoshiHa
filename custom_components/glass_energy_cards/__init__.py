"""Frontend-only registration for Glass energy cards."""

from __future__ import annotations

import logging

from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant

DOMAIN = "glass_energy_cards"
LOCAL_URL = "/glass_energy_cards-local"
CARD_FILES = (
    "glass-state-grid-card.js",
    "glass-gas-card.js",
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Register static frontend card assets."""
    static_path = hass.config.path(f"custom_components/{DOMAIN}/www")
    await hass.http.async_register_static_paths(
        [StaticPathConfig(LOCAL_URL, static_path, True)]
    )

    for filename in CARD_FILES:
        add_extra_js_url(hass, f"{LOCAL_URL}/{filename}?v=1.0.0")

    _LOGGER.info("Glass energy cards frontend resources registered")
    return True
