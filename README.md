# Home Assistant RF Gateway Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub Release][releases-shield]][releases]
![Project Maintenance][maintenance-shield]

这是一个用于 Home Assistant 的 RF 网关集成组件，支持通过 ESP 设备接收和发送 RF 信号。

## 功能

- 🔍 实时接收和显示 RF 信号
- 📡 发送自定义 RF 信号
- 💾 保存和管理常用的 RF 代码
- 🔄 自动记录接收到的信号
- 📊 调试信息显示

## 安装

### HACS 安装（推荐）

1. 确保已经安装了 [HACS](https://hacs.xyz/)
2. 点击 HACS 中的 "Integrations"
3. 点击右上角的 "+" 按钮
4. 搜索 "RF Gateway"
5. 点击 "Download"
6. 重启 Home Assistant

### 手动安装

1. 下载此仓库
2. 将 `custom_components/rf_gateway` 文件夹复制到你的 Home Assistant 的 `custom_components` 目录中
3. 重启 Home Assistant

## 配置

1. 在 Home Assistant 的集成页面中点击 "添加集成"
2. 搜索 "RF Gateway"
3. 按照配置向导完成设置：
   - 输入设备名称
   - 设置 MQTT 主题前缀（默认为 esp-rf）

## 使用方法

### 接收 RF 信号

- 当设备接收到 RF 信号时，会自动显示在传感器中
- 可以在历史记录中查看所有接收到的信号

### 发送 RF 信号

1. 在输入框中输入要发送的 RF 代码（16位十六进制，格式：FD******DF）
2. 点击发送按钮

### 仪表板配置示例

```yaml
type: vertical-stack
cards:
  - type: entities
    title: RF 网关
    entities:
      - sensor.rf_gateway_received_signal
      - input_text.rf_code
      - button.rf_gateway_send_code
  - type: history-graph
    title: 接收历史
    entities:
      - sensor.rf_gateway_received_signal
```

## 硬件要求

- ESP8266/ESP32 设备
- RF 接收器（如 RXB6/RXB8）
- RF 发射器（如 FS1000A）

## 调试

如果遇到问题，可以查看以下信息：

1. Home Assistant 日志
2. MQTT 调试信息（sensor.rf_gateway_debug_info）
3. ESP 设备日志

## 常见问题

**Q: 为什么接收不到信号？**
A: 请检查：
1. ESP 设备是否正常工作
2. MQTT 连接是否正常
3. RF 接收器接线是否正确

**Q: 发送信号没有反应？**
A: 请确认：
1. RF 代码格式是否正确（FD******DF）
2. MQTT 连接是否正常
3. RF 发射器接线是否正确

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

[releases-shield]: https://img.shields.io/github/release/www1988/hass-rf-gateway.svg
[releases]: https://github.com/www1988/hass-rf-gateway/releases
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg 