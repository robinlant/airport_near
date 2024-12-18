# Airport Finder

This project provides a simple website that allows users to find the nearest airports by entering an address. It uses a CSV file of worldwide airports to compute and display the closest airports based on the provided information.

## Features
- **Search by City Name**: Searches for airports worldwide.
- **Search by Postal Code**: Restricts the search to airports in Germany.
- **Search by City & Postal Code**: Provides worldwide results with enhanced accuracy.

## Data Source
The airport data is based on the [OurAirports](https://davidmegginson.github.io/ourairports-data/airports.csv) dataset. The default CSV file (`large_medium_airports.csv`) is included in the project, but you can replace it with your own.

---

## Prerequisites
- Docker installed on your system.
- Python 3.11 or higher if running locally.

---

## Installation and Usage

### 1. **Run with Docker**

#### Clone the repository and navigate to the project directory:
```bash
git clone git@github.com:robinlant/airport_near.git
cd airport_near
```

#### Build the Docker Image
```bash
docker build -t airport-finder .
```

#### Run the Docker Container
```bash
docker run -p 8000:8000 airport-finder
```

The application will be available at: [http://localhost:8000](http://localhost:8000)

---

### 2. **Provide a Custom Airport CSV File**
If you want to use a different CSV file for airports:
1. Create a volume to mount the custom CSV file.
2. Specify the file path as an environment variable `AIRPORTS_FILE`.

#### Example
Assume your CSV file is located at `/path/to/your/airports.csv`. Run the container as follows:
```bash
docker run -p 8000:8000 \
    -v /path/to/your/airports.csv:/app/app/static/data/custom_airports.csv \
    -e AIRPORTS_FILE=/app/app/static/data/custom_airports.csv \
    airport-finder
```

---

## Configuration
The application supports the following configuration options via environment variables:

| Variable          | Description                                         | Default Value                                  |
|--------------------|-----------------------------------------------------|-----------------------------------------------|
| `SECRET_KEY`       | Secret key for session management.                 | `secret_key_for_testing_only`                 |
| `AIRPORTS_FILE`    | Path to the airport data CSV file.                 | `/app/static/data/large_medium_airports.csv`  |

---

## Development Setup (Without Docker)
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone git@github.com:robinlant/airport_near.git
   cd airport_near
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   flask run --debug
   ```
4. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Data Attribution
This project uses the airport data provided by [OurAirports](https://ourairports.com/data/).