# Network Security - Phishing Detection Project

## Overview

This is a Network Security project focused on phishing data detection and prevention. The system analyzes malicious websites, emails, or links that attempt to steal sensitive user information. By leveraging machine learning models, it classifies sources as phishing or legitimate, helping organizations enhance threat detection and protect users from credential theft and fraud.

## Features

- **Data Ingestion**: Automated collection and processing of network data including URLs, domain information, and email headers.
- **Data Transformation**: Preprocessing and feature engineering to extract relevant attributes like domain age, URL patterns, and content analysis.
- **Data Validation**: Ensuring data quality and integrity before model training.
- **Machine Learning Classification**: Utilizes advanced ML algorithms to classify phishing vs. legitimate sources.
- **MongoDB Integration**: Stores processed data and results in MongoDB for scalable data management.
- **Docker Support**: Containerized deployment for easy setup and portability.
- **Comprehensive Logging**: Built-in logging system for monitoring and debugging.

## Project Structure

```
network_security/
├── cloud/                          # Cloud-related components
├── components/                     # Core ML pipeline components
│   ├── data_ingestion.py          # Data collection and loading
│   ├── data_transformation.py     # Feature engineering and preprocessing
│   └── data_validation.py         # Data quality checks
├── constant/                       # Configuration constants
├── entity/                         # Data entities and configurations
│   ├── artifact_entity.py          # ML artifacts definitions
│   └── config_entity.py            # Configuration entities
├── exception/                      # Custom exception handling
├── logging/                        # Logging utilities
├── pipeline/                       # ML pipeline orchestration
└── utils/                          # Utility functions

data_schema/
└── schema.yaml                     # Data schema definitions

network_data/
└── phisingData.csv                 # Phishing dataset

notebooks/                          # Jupyter notebooks for analysis
demo.ipynb                          # Demonstration notebook
Dockerfile                          # Docker configuration
main.py                             # Main application entry point
push_data.py                        # Data pushing utilities
requirements.txt                    # Python dependencies
setup.py                            # Package setup
test_MongoDB.py                     # MongoDB testing utilities
```

## Installation

### Prerequisites

- Python 3.8+
- MongoDB
- Docker (optional)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd NetworkSecurity
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MongoDB connection (update configuration in `entity/config_entity.py`)

4. Run the setup:
   ```bash
   python setup.py install
   ```

### Docker Setup

Build and run using Docker:
```bash
docker build -t network-security .
docker run -p 8000:8000 network-security
```

## Usage

### Running the Application

Execute the main script:
```bash
python main.py
```

### Data Processing

Push data to MongoDB:
```bash
python push_data.py
```

### Testing

Run MongoDB tests:
```bash
python test_MongoDB.py
```

### Jupyter Notebook

Explore the demo notebook:
```bash
jupyter notebook demo.ipynb
```

## Data Analysis

The project analyzes various features for phishing detection:
- URL structure and patterns
- Domain age and registration details
- Email header analysis
- Content-based features
- SSL certificate information

## Machine Learning Pipeline

1. **Data Ingestion**: Load and preprocess raw network data
2. **Feature Engineering**: Extract and transform features for model input
3. **Model Training**: Train classification models on labeled data
4. **Validation**: Evaluate model performance and accuracy
5. **Deployment**: Deploy trained models for real-time prediction

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset source: [Mention data source if applicable]
- Built with Python, scikit-learn, and MongoDB