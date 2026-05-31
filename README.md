# Glass Energy Cards

适用于 Home Assistant 的玻璃拟态电费、燃气费前端卡片集成。

本项目仅提供 Lovelace 前端卡片资源，不采集、不创建、不修改任何传感器数据；需要配合已有的数据集成使用。

## 项目说明

本卡片修改自 xiaoshi 相关 Home Assistant 卡片/集成，主要调整为透明液态玻璃风格，并优化了图表显示、触屏交互和低性能设备上的渲染流畅度。

为了避免影响原版集成，本项目使用独立的 `glass-*` 卡片名称和独立的 `glass_energy_cards` 前端资源路径，可以与原版卡片同时安装、同时使用。

## 依赖

请先安装并配置下列数据来源集成：

- 电费数据依赖：[xiaoshi930/qweather](https://github.com/xiaoshi930/qweather)
- 燃气数据依赖：[gao19970120/gas-balance-mqtt](https://github.com/gao19970120/gas-balance-mqtt)

## 卡片名称

- `custom:glass-state-grid-card`
- `custom:glass-state-grid-button`
- `custom:glass-gas-card`

## 安装方式

将 `custom_components/glass_energy_cards` 复制到 Home Assistant 的 `custom_components` 目录，然后重启 Home Assistant。

集成会自动注册以下前端资源：

- `/glass_energy_cards-local/glass-state-grid-card.js`
- `/glass_energy_cards-local/glass-gas-card.js`

## 使用示例

电费卡片：

```yaml
type: custom:glass-state-grid-card
entities:
  - entity_id: sensor.your_electricity_entity
theme: off
```

燃气卡片：

```yaml
type: custom:glass-gas-card
entities:
  - entity_id: sensor.your_gas_entity
theme: off
```

电费按钮卡片：

```yaml
type: custom:glass-state-grid-button
entities:
  - entity_id: sensor.your_electricity_entity
theme: off
```

## 注意事项

- 本项目是前端卡片集成，不包含数据采集逻辑。
- 如果卡片无数据显示，请先确认依赖集成的数据实体是否正常。
- 如果浏览器仍显示旧卡片样式，请清理 Home Assistant 前端缓存或强制刷新页面。
