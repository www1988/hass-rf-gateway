"""Support for RF Gateway buttons."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components import mqtt
from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import CONF_NAME

from .const import DOMAIN, TOPIC_SEND, NAME_SEND_CODE

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up RF Gateway buttons."""
    config = config_entry.data
    base_name = config[CONF_NAME]

    async_add_entities([
        RFGatewaySendButton(
            f"{base_name} {NAME_SEND_CODE}",
            TOPIC_SEND,
            "mdi:remote",
            config_entry.entry_id,
        )
    ])

class RFGatewaySendButton(ButtonEntity):
    """Representation of a RF Gateway Send Button."""

    def __init__(
        self,
        name: str,
        topic: str,
        icon: str,
        entry_id: str,
    ) -> None:
        """Initialize the button."""
        self._attr_name = name
        self._attr_unique_id = f"{entry_id}_send_button"
        self._attr_icon = icon
        self._topic = topic

    async def async_press(self) -> None:
        """Handle the button press."""
        code = self.hass.states.get("input_text.rf_code")
        if code and code.state:
            await mqtt.async_publish(
                self.hass,
                self._topic,
                code.state,
            ) 