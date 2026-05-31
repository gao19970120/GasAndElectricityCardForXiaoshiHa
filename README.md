# Glass Energy Cards

A frontend-only Home Assistant custom integration that provides glass-style electricity and gas Lovelace cards.

This repository only registers frontend card assets. It does not replace or modify the original data integrations that provide your electricity or gas sensors.

## Cards

- `custom:glass-state-grid-card`
- `custom:glass-state-grid-button`
- `custom:glass-gas-card`

## Installation

Copy `custom_components/glass_energy_cards` into your Home Assistant `custom_components` directory, then restart Home Assistant.

The integration registers these resources automatically:

- `/glass_energy_cards-local/glass-state-grid-card.js`
- `/glass_energy_cards-local/glass-gas-card.js`

## Example

```yaml
type: custom:glass-state-grid-card
entities:
  - entity_id: sensor.your_electricity_entity
theme: off
```

```yaml
type: custom:glass-gas-card
entities:
  - entity_id: sensor.your_gas_entity
theme: off
```

## Notes

- Keep your existing sensor integrations installed and configured.
- These cards read data from the entities you pass in Lovelace config.
- Card names intentionally use the `glass-*` prefix so they can coexist with the original cards.
