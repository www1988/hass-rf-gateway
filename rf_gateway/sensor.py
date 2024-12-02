"""Support for RF Gateway sensors."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components import mqtt
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.const import CONF_NAME

from .const import (
    DOMAIN,
    TOPIC_RECEIVED,
    TOPIC_DEBUG,
    NAME_RECEIVED_SIGNAL,
    NAME_DEBUG_INFO,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up RF Gateway sensors."""
    config = config_entry.data
    base_name = config[CONF_NAME]

    entities = [
        RFGatewaySensor(
            f"{base_name} {NAME_RECEIVED_SIGNAL}",
            TOPIC_RECEIVED,
            "mdi:radio-tower",
            config_entry.entry_id,
        ),
        RFGatewaySensor(
            f"{base_name} {NAME_DEBUG_INFO}",
            TOPIC_DEBUG,
            "mdi:bug",
            config_entry.entry_id,
        ),
    ]

    async_add_entities(entities)

class RFGatewaySensor(SensorEntity):
    """Representation of a RF Gateway Sensor."""

    def __init__(
        self,
        name: str,
        topic: str,
        icon: str,
        entry_id: str,
    ) -> None:
        """Initialize the sensor."""
        self._attr_name = name
        self._attr_unique_id = f"{entry_id}_{topic}"
        self._attr_icon = icon
        self._topic = topic
        self._attr_native_value = None

    async def async_added_to_hass(self) -> None:
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""
            self._attr_native_value = message.payload
            self.async_write_ha_state()

        await mqtt.async_subscribe(
            self.hass, self._topic, message_received, 1
        ) 