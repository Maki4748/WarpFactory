# List of Current Question Marks
- metricGet_ModifiedTime randomly uses a variable called 'GridScale' which is not given

# WarpFactory

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

WarpFactory is a powerful numerical toolkit written in MATLAB for analyzing warp drive spacetimes using Einstein's theory of General Relativity. Its unique focus lies in providing a numerical framework to analyze the physicality of spacetime.

## Key Features

- 3D finite difference solver for the stress-energy tensor
- Energy condition evaluations for the point-wise Null, Weak, Dominant, and Strong Energy Conditions
- Metric scalar evaluation for the shear, expansion, and vorticity
- Momentum flow visualizations
- GPU utilization for accelerated computations

|![Stress Energy Tensor Animation](Visualizer/images/AlcubierreMomentumFlow.gif)|
|:------------------------------:|
|*Animation of the stress-energy tensor. Lighter regions in the cross-section correspond to higher energy densities. The blue lines demonstrate the direction of momentum flow within the warp drive.*|

## Documentation

For comprehensive documentation and usage instructions, please visit the [WarpFactory Documentation](https://applied-physics.gitbook.io/warp-factory).

[CQG Paper](https://iopscience.iop.org/article/10.1088/1361-6382/ad2e42)

[arxiv](https://arxiv.org/abs/2404.03095)

## Installation

To set up WarpFactory, follow these steps:

1. Install Git from the official [Git website](https://git-scm.com/).
2. Install MATLAB from the official [MATLAB website](https://www.mathworks.com/products/matlab.html). During installation, ensure that you select the "Parallel Computing Toolbox" component.
3. Clone the WarpFactory repository: git clone https://github.com/NerdsWithAttitudes/WarpFactory.git
4. Launch MATLAB and navigate to the cloned project folder.
5. Add the project folder and its subfolders to the MATLAB path.

For detailed installation instructions, please refer to the [Installation Guide](https://applied-physics.gitbook.io/warp-factory/overview/installing-warp-factory).

## Development Team

- Christopher Helmerich
- Jared Fuchs

We would like to extend our gratitude to the following individuals for their contributions and code reviews:
- Alexey Bobrick
- Luke Sellers
- Brandon Melcher
- Justin Feng
- Gianni Martire

## License

WarpFactory is released under the [MIT License](https://opensource.org/licenses/MIT). We kindly request that all users of WarpFactory [cite their use of the code in published work.](https://applied-physics.gitbook.io/warp-factory/general/citing-warp-factory)

