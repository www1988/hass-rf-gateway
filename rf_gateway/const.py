"""Constants for the RF Gateway integration."""

DOMAIN = "rf_gateway"

# MQTT Topics
TOPIC_RECEIVED = "esp-rf/received"
TOPIC_DEBUG = "esp-rf/debug"
TOPIC_SEND = "esp-rf/send"

# Configuration
CONF_DEVICE_ID = "device_id"
CONF_MQTT_TOPIC = "mqtt_topic"

# Default values
DEFAULT_MQTT_TOPIC = "esp-rf"

# Entity names
NAME_RECEIVED_SIGNAL = "RF Received Signal"
NAME_DEBUG_INFO = "RF Debug Info"
NAME_SEND_CODE = "Send RF Code"
NAME_RF_CODE = "RF Code" 