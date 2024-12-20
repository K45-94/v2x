# v2x
CLI tool to simplify the process of managing and working with large datasets.


# ELD - Extremely Large Data Handling Tool

## Overview

ELD is a command-line tool designed to handle, query, and visualize extremely large datasets. It supports ingestion from CSV and JSON files, simple querying, and basic visualization.

## Installation

1. Clone the repository:
git clone [(https://github.com/K45-94/v2x.git)]
cd v2x


2. Set up the virtual environment:
python -m venv eld_env
   source eld_env/bin/activate  # On Windows use eld_env\Scripts\activate
   pip install -r requirements.txt


## Usage

### Ingest Data
eld ingest [FileName].[FileType]


### Query Data
eld query [FileName] [Column] [Operator] [Value]
- Example: `eld query sample.csv Age > 45` `eld query sample.json Date > 2024`

### Visualize Data
eld visualize [Field1] [Field2]... [FileName] --chart [Type]
- Example: `eld visualize Category sample.csv --chart bar`

## Running Tests:
Run tests using pytest:
### bash
####    pytest tests/


## Contributing

Contributions are welcome! Please fork the repository and submit pull requests. You can submit poor code.
## License

(https://unlicense.org)

