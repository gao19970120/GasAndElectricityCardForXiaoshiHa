const baseUrl = new URL("./", import.meta.url).href;

window.GlassEnergyCardsBaseUrl = baseUrl;

const loadModule = (filename) => {
  const existing = document.querySelector(`script[data-glass-energy-card="${filename}"]`);
  if (existing) return;

  const script = document.createElement("script");
  script.type = "module";
  script.src = new URL(filename, baseUrl).href;
  script.dataset.glassEnergyCard = filename;
  document.head.appendChild(script);
};

loadModule("glass-state-grid-card.js");
loadModule("glass-gas-card.js");
