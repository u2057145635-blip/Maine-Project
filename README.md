# Main Project
## Diamine PES Benchmark
The program will read XYZ geometries for the four minima (M1–M4) and the available transition states. After checking atom ordering and aligning the structures, it will use principal component analysis (PCA) to project the geometries onto two axes. Each point will represent one stationary structure, with color indicating its relative electronic energy in eV and marker shape distinguishing minima from transition states.
It will also be used to benchmark 17 DFT functionals and several coupledcluster method for a diamine radical cation. It will assess which stationary points each functional reproduces and compare relative energies and barriers on common geometries.

## Code-Structure

```text
diamine_pes_benchmark/
|----- __init__.py
|----- models.py        # Methods, stationary points, and Calculation Result classes
|----- csv_io.py        # Read/write (Read and validate calculation records and write summary CSVs
|----- geometry_io.py   # matching class (Read XYZ files and match each geometry to its calculation record)
|----- coverage.py      # Report which minima and transition states each functional reproduces
|----- energetics.py    # comparing class (Compare relative energies and barriers on shared geometries)
|----- projection.py    # Aligning class (Aligning geometries and compute their PC1 and PC2 coordinates)
|----- plotting.py      # Plotting class (Plot coverage, energy comparisons, and PCA maps of stationary points)
|----- cli.py           # benchmark class (Select the coupled-cluster reference and run the benchmark)

```
## Mathematical Formulation

### 1. Relative Energies & Barrier Heights
For a given electronic-structure method $m$ and basis set $b$, the relative electronic energy $\Delta E_i^{(m,b)}$ of stationary point $i$ (in $\text{eV}$) is referenced to the global minimum ($M_4$):

$$\Delta E_i^{(m,b)} = \left( E_i^{(m,b)} - E_{M_4}^{(m,b)} \right) \times 27.211386$$

where $E$ is the electronic energy in Hartree ($E_h$). Error metrics (MAE and RMSE) are evaluated on common stationary points against the Coupled-Cluster reference ($\Delta E_i^{\text{ref}}$):

$$\text{MAE}^{(m)} = \frac{1}{N_{\text{shared}}} \sum_{i=1}^{N_{\text{shared}}} \left\vert{} \Delta E_i^{(m)} - \Delta E_i^{\text{ref}} \right\vert{}$$

### 2. Structural Alignment & Principal Component Analysis (PCA)


## Potential Surface Visualization
### Spin-Density

![Spin-Density](dae-spin-density.png)

#

