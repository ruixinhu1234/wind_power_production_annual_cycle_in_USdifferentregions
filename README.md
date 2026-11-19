
# US Wind Power: Annual Cycle and Transmission Smoothing

Course project for EN.530.637 Energy Meteorology, 2026Fall, Johns Hopkins University.
This project examines the typical annual cycle of wind power production in different regions of the United States and explores how increased transmission capacity could smooth out its variability. Monthly plant-level wind generation from the U.S. Energy Information Administration (EIA) is converted to capacity factors, aggregated by region, and compared across regions. The analysis then quantifies how much the variability of pooled (interconnected) regions is reduced relative to individual regions, using Wyoming to California as an example case.

The project is organized around four questions:

1. What is the typical annual cycle of wind power production in different parts of the US?
2. How can increased transmission smooth out this variability, and by how much?
3. Why does smoothing work (physical and statistical mechanisms)?
4. What are the limitations of this approach?

## Data
- **EIA-923** (monthly plant-level generation): https://www.eia.gov/electricity/data/eia923/
  Wind plants are selected using fuel code `WND` and prime mover `WT`.
- **EIA-860** (plant location and nameplate capacity): https://www.eia.gov/electricity/data/eia860/
- Raw files are not stored in this repository because of size; download them from the links above and place them in the `data/` folder.
